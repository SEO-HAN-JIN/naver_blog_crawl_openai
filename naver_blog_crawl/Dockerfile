# 1. Java 17 기반 이미지 사용
FROM openjdk:17-jdk-alpine

# 2. JAR 복사 (Gradle 빌드된 결과물)
COPY build/libs/*.jar app.jar

# 3. 애플리케이션 실행
ENTRYPOINT ["java", "-jar", "/app.jar"]

# ./gradlew build
# docker-compose up --build
# 이후부터는 코드 변경이 없으면 그냥 docker-compose up만 해도 돼.
# 2️⃣ 기존 컨테이너가 있으면 어떻게 할까?
# 👉 기존 컨테이너가 삭제(destroy) 됐다가 새로 생성됨
# 새 이미지가 만들어졌으니까, 그걸 기반으로 새 컨테이너를 만들기 때문이야.
# 이때 기존 컨테이너는 삭제되고, 이름은 같지만 새로운 컨테이너로 교체됨.

# 그럼 언제 mariadb 컨테이너가 꺼졌다가 다시 시작될까?
# docker-compose down으로 전체 내려버린 경우
# mariadb의 설정이 변경된 경우 (예: .env 파일이나 환경변수)
# volume이나 네트워크 설정이 바뀐 경우


# 💡 안정적인 방법
# springboot만 다시 배포하고 싶다면 이렇게 하면 돼:
# docker-compose build springboot
# docker-compose up -d springboot