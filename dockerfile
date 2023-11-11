FROM mcr.microsoft.com/playwright/python:v1.39.0-jammy

WORKDIR /playwright_docker

COPY requirements.txt ./

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "pytest" ]
