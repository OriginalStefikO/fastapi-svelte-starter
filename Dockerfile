# In this first stage we build the frontend, after that we copy the build files to the backend, install dependencies and run the backend.
FROM node:18 AS frontendBuilder

WORKDIR /app/frontend

COPY frontend/package-lock.json frontend/package.json ./
RUN npm ci

COPY frontend/ .

RUN npm run build

FROM python:3.11.7-slim AS backendBuilder

WORKDIR /app/backend

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY --from=frontendBuilder /app/public ./public
COPY . .

EXPOSE 8080

CMD [ "python", "main.py" ]