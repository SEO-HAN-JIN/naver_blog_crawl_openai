### 도커: 이미지 빌드
>  docker-compose -f docker-compose.dev.yml build

### 도커: 기존 컨테이너 삭제
 > docker rm -f my-mariadb

### 도커: 컨테이너 생성
 > docker-compose up -d <br>
 > docker-compose -f docker-compose.dev.yml up -d (특정 파일)

### 도커: 컨테이너 다시시작
>  docker-compose restart <컨테이너명 or 컨테이너ID>

### `docker-compose up 과 restart 차이`
- `up` : `build context`나 설정이 반영된다. 그리고 컨테이너 ID도 달라지고, 초기화된 상태로 시작된다.
  - Dockerfile, docker-compose.yml 바뀜 / volume 재적용 / 환경변수 수정됨
- `restart` : 설정/코드 변경이 반영되지 않고 컨테이너가 초기화 되지 않는다.
  - 단순재시작용

### 도커: 로그 확인
 > - 모든 컨테이너의 로그 출력 <br>
 >   - docker-compose -f docker-compose.dev.yml logs -f (-f: 특정파일)
 > - 특정 컨테이너 로그 출력
 >   - docker logs -f <컨테이너명 or 컨테이너ID>

### 도커: 네트워크 생성
> docker network create mynetwork

mariadb와 spring boot app에 대한 docker-compose를 따로 관리하려고 하는데 처음에 mariadb의 docker-compose.yml에 `driver: bridge`을 하고 spring boot app의 docker-compose의 network을 아래와 같이 설정했는데 에러남

그 이유는 mariadb의 docker-compose.yml에서 설정한 `mynetwork`는 mariadb의 docker compose 프로젝트만의 내부 네트워크로만 만들어졌기 때문에 spring boot 컨테이너는 해당 네트워크에 붙지 못하는 상황
```dockerfile
networks:
  mynetwork:
    external: true  # 외부 네트워크로 관리
```
## 해결
### 도커: 네트워크 생성
> docker network create mynetwork

mariadb와 spring boot의 docker-compose.yml에 모두 위와 같이 `external: true`로 설정함.

### 도커: 네트워크 종류 확인
> docker network ls        

### 도커: 특정 네트워크 상태 확인
>  docker network inspect mynetwork

### 도커: 특정 컨테이너 bash 접속
> docker exec -it <컨테이너ID> bash
