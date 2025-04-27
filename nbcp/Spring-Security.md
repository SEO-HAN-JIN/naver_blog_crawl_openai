## Iframe
```java
http.headers(headers -> headers.frameOptions(HeadersConfigurer.FrameOptionsConfig::deny));
```
- 타임리프를 쓰든 아니든, `frameOptions().deny()` 설정이 있으면 모든 iframe 사용이 막혀서 브라우저에서 iframe 안에 페이지를 띄우는 건 불가능해진다.
- `frameOptions().deny()`는 HTTP 응답 헤더에 다음을 추가한다.
  - `X-Frame-Options: DENY`
  - 이 헤더는 브라우저에 `이 페이지는 어떤 ifrmae에도 절대 포함하지마!` 라고 말하는 것과 같다.
- 다른 방법
  - 완전히 허용(보안낮음) : `http.headers(headers -> headers.frameOptions(HeadersConfigurer.FrameOptionsConfig::disable));`
  - SAMEORIGIN만 허용 : `http.headers(headers -> headers.frameOptions().sameOrigin());`

## CSRF
- **CSRF(사이트 간 요청 위조)** 는 사용자가 인증된 상태에서 악성 사이트가 사용자 대신 요청을 보내게 만드는 공격방식
>예시:<BR>
> 어떤 쇼핑몰에 로그인한 상태에서 다른 악성 사이트에 접속했는데 그 사이트가 몰래 나의 쿠키로 주문 결제를 요청해버리는 식
- Spring Security의 기본 CSRF 방어 방법
  - **POST, PUT, DELETE** 요청 등에 대해 **숨겨진 토큰(_csrf)을 요청 파라미터나 헤더로 보내야만 처리함.**
  - 이것이 없으면 403 오류를 발생시켜 요청을 막음
- `disable`하는 이유
  - **REST API 서버** 에서는 일반적으로
    - 세션 기반 인증이 아닌 JWT 토큰 기반 인증을 사용함.
    - 브라우저가 자동으로 쿠키를 보내는 구조가 아님.
    - CSRF 공격의 위험이 상대적으로 낮아짐.
- CSRF는 세션 + 브라우저 쿠키 기반 인증일 때 유효하다.
>예시\
> - 사용자가 bank.com에 로그인 -> 세션 ID 쿠키가 생김
> - 공격자가 만든 evil.com에 접속
> - 그 안에 <form action=http://bank.com/transfer" method="POST"> 같은게 자동 실행됨
> - 사용자의 세션 쿠키가 자동으로 전송
> - 서버는 유효한 요청이라 판단 -> 공격성공 
### CSRF 보호의 기본 원리
서버가 클라이언트에게 CSRF 토큰을 발급하고, 클라이언트가 다음 요청 시 그 토큰을 함께 보내는지 검사하는 방식
### 동작흐름
#### 1. 클라이언트가 페이지 요청(GET)
```html
GET /form
Cookie: JESSIONID=abc123
```
- 서버는 세션을 통해 사용자 인증 확인.
- 서버는 CSRF 토큰을 생성해서 HTML에 넣어줌 (ex: hidden input)
```html
<form method="POST" action="/transfer">
  <input type="hidden" name="_csrf" value="csrf-token-xyz">
</form>
```
#### 2. 사용자가 form 제출 (POST)
```html
POST /transfer
Cookie: JSESSIONID=abc123
Content-Type: application/x-www-form-urlencoded

_csrf=csrf-token-xyz&amount=10000
```
- 서버는 세션 쿠키(JESSIONID)로 사용자 인증
- 동시에 `_csrf`값이 세션에 저장된 토큰과 일치하는지 확인
- 일치하면 -> 정상처리
- 다르면 -> 403 Forbidden (CSRF 공격 의심)

### 사용법
#### 1. form방식
Spring Security와 Thymelea 연동하면 자동으로 태그를 넣어준다.
```html
<form th:action="@{/submit}" method="post">
    <input type="text" name="example">
    <button type="submit">제출</button>
</form>
```
이렇게만 써도 렌터링된 HTML에 자동으로 아래가 붙음
```html
<input type="hidden" name="_csrf" value="토큰값">
```
`thymeleaf-extrax-springsecurity5`를 쓰면 `<form>`태그 안에 자동으로 CSRF가 삽입된다.
#### 2. JS로 요청시 
`fetch`, `axios`, `jQuery.ajax()`등을 쓸 경우에 해더에 직접 넣어줘야한다.
```javascript
fetch('/api/save', {
  method: 'POST',
  headers: {
    'X-CSRF-TOKEN': csrfTokenValue, // 서버에서 받은 CSRF 값
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
});
```
#### 대안: meta 태그에 심어두기
> 화면마다 CSRF hidden 태그를 다 넣는게 아니라,\
> 화면 처음 불러올 때 한 곳에만  넣어두고, JS에서 그걸 전역처럼 쓰면된다.
```html
<!-- layout.html의 <head> 안에 공통으로 들어감 -->
<meta name="_csrf" th:content="${_csrf.token}"/>
<meta name="_csrf_header" th:content="${_csrf.headerName}"/>

```
```javascript
const csrfToken = document.querySelector('meta[name="_csrf"]').content;
const csrfHeader = document.querySelector('meta[name="_csrf_header"]').content;

// AJAX 요청 보낼 때
fetch('/api/save', {
    method: 'POST',
    headers: {
        [csrfHeader]: csrfToken,
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ msg: 'hello' })
});

```
## CORS
> `Cross-Origin Resource Sharing`\
> 브라우저는 보안상의 이유로 다른 Origin(도메인, 포트 프로토콜이 다르면)에서 온 요청을 기본적으로 차단(CORS 정책 위반) 한다.

### 두 가지의 경우
1. 프론트엔드 서버와 백엔드 서버가 다를경우 (SPA 방식)
    - 클라이언트가 로그인 시도 시 백엔드 로그인 API가 호출될 것이다. 이때 백엔드에서 프론트엔드 도메인을 CORS허용 설정하지 않으면 접근이 차단된다.
2. 프론트엔드와 백엔드가 같이 구동되는 경우 (SRR 방식)
    - 하나의 아이피에 프론트와 백엔드가 같이 구동되기 때문에 상관없다.

#### 예시:
 1. 동작방식은 프론트엔드에서 백엔드로 API호출한다.
```javascript
fetch("http://api.example.com.user", {
    method: "GET",
    credentials: "includde" // <- 쿠키 포함(세션 기반 인증 시 필수)
})
- `omit` : 쿠키, 인증 헤더 등을 아예 보내지 않음
- `same-origin(기본값)` : 같은 origin일 경우만 쿠키 등을 보냄
- `include`: cross-origin 요청에도 쿠키를 무조건 포함함
```
- 프론트에서 `credentials: include`로 설정했으면, 백엔드에서도 `Access-Control-Allow-Credentials: true`를 허용해줘야한다.
- SPA 구조에서는 CORS 설정이 반드시 필요하며, Spring Security와 함께 설정할 경우 `.allowCredentials(true)` + 정확한 `allowedOrigins` 설정이 핵심 포인드이다.
2. 백엔드에서 `Acess-Control-Allow-Credentials`를 헤더에 반환한다.
3. 브라우저에서 `Acess-Control-Allow-Credentials: true`를 확인한다.
    - 없으면 에러, 있으면 정상동작
   
#### CORS 응답 헤더 (서버 -> 브라우저)
- `Access-Control-Allow-Origin`: 어떤 Origin(출처)에서 온 요청을 허용할지 (* 또는 http://example.com)
- `Access-Control-Allow-Credentials`: 쿠키/인증 정보 요청 허용 여부 (true만 가능)
- `Access-Control-Allow-Methods`: 허용할 HTTP 메서드 (GET, POST, PUT, DELETE, OPTIONS 등)
- `Access-Control-Allow-Headers`: 클라이언트가 보낼 수 있는 커스텀 헤더를 명시(Authorization, Content-Type 등)
- `Access-Control-Expose-Headers`: 브라우저가 응답에서 접근 할 수 있도록 허용된 헤더 (기본 외의 헤더 노출 허용)
- `Access-Control-Max-Age`: preflist(Options) 응답을 브라우저가 캐시할 시간(초단위)
#### Spring Security 에서 허용설정
```java
@Configuration
public class WebConfig implements WebMvcCofigurer {
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")  // 모든 경로에 대해 적용
                .allowedOrigins("http://example.com")   // 허용할 출처
                .allowedMethods("GET", "POST") // 허용할 HTTP 메서드
                .allowedHeaders("*")    // 모든 헤어 허용
                .allowCredentials(true) // 쿠키 등 인증 정보 허용
                .maxAge(3600);  // preflight 요청 캐싱 시간(초)
    }
}
```

- `credentials: "include"`인데 `Access-Control-Allow-Credentials: false` 응답이 왔다면 에러 발생
- SSR(JSP, 타임리프) 같은 경우 localhost로 호출하기 때문에 클라이언트0-서버간에 CORS가 필요하지 않다. 왜냐하면 페이지가 서버에서 렌더링되어 같은 도메인에서 전달되기 떄문이다. 그러므로 CORS설정은 주로 AJAX요청 또는 API 요청에서 발생한다.
  - 외부에서 API 요청이 없다면 `configuration.addAllowedOriginPattern("http://localhost:8080")`와 같이 특정 도메인만 허용하는 방식이 가장 안전하다.
    - CORS는 다른 출처(origin)에서 서버를 리소스를 요청할 때 발생하는 보안 매커니즘이다.
- JWT와 CORS는 별개이며, CORS 설정은 프론트 서버와의 관계(Oirign 차이)에 따라 필요하다.
  - JWT는 인증을 위한 수단 (사용자 확인/권한 부여 등)
  - JWT는 보통 `Authorization 헤더`에 담아서 보내느는데 `setAllowCredentials`와는 연관이 없다.
  - 하지만 `addAllowedHeader`와는 연관이 있다.
  - CORS는 브라우저가 `다른 출처의 요청을 허용할지 말지` 결정하는 보안 정책

## 로그인 방식
### FormLogin 방식
- 웹브라우저에서 로그인 폼 띄우고 사용자 ID/PW 입력받아서 인증하는 방식
- `<form>`을 사용해서 아이디/비밀번호를 서버로 직접 제출함(POST)

### HttpBasic 방식
- 브라우저나 API 클라이언트가 HTTP 헤더에 ID/PW를 Base64로 실어서 보내는 방식 (ex. Authorization: Basic ~~)