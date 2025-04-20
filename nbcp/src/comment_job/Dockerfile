# 1. Pyton 이미지 기반 (버전은 원하는 대로 조정 가능)
FROM python:3.10-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 의존성 먼저 복사하고 설치(캐시 활용)
COPY requirements.txt .

# 4. 필요한 패키지 설치
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 5. 파이썬 스크립트 복사
COPY python_scripts/ ./python_scripts/

CMD ["python", "python_scripts/example.py"]