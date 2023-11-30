# For Your Date[데이트를 부탁해]👫
- 데이트 코스를 고민하는 대한민국 커플들을 위해 자동으로 데이트 코스를 추천해주는 서비스입니다

## 목차
1. [프로젝트 목표](#1-프로젝트-목표)
2. [요구사항 분석 및 기능명세서](#2-요구사항-분석-및-기능명세서)
3. [개발 일정](#3-개발-일정)
4. [개발 환경 및 배포](#4-개발-환경-및-배포)
5. [URL 구조](#5-URL-구조)
6. [프로젝트 구조](#6-개발-일정-및-프로젝트-구조)
7. [ERD](#7-ERD)
8. [프로토타입](#8-프로토타입)
9. [구현 내용](#9-구현-내용)
10. [트러블슈팅](#10-트러블슈팅)
11. [후기](#11-후기)

## 1. 프로젝트 목표
데이트 예정인 장소와 시간, 계절, 이동수단 등을 입력받아 ChatGPT로부터 데이트 코스를 추천받습니다.  
이 프로젝트는 [이전 프로젝트](https://github.com/Nam-Younghoon/For_Your_Date)를 확장하는 프로젝트이며, DRF(Django REST Framework)을 사용하여 회원가입, 로그인, 로그아웃, 데이터 요청 및 저장 등이 가능하게 API를 제공해주는 목표를 가지고 있습니다.  

## 2. 요구사항 분석 및 기능명세서
### 기본 요구사항
- DRF을 이용하여 구현한다
- API만 구현한다 (Front-End는 포함시키지 않는다)
- 회원가입, 로그인을 구현한다
- 기본적인 CRUD를 구현한다
- ChatGPT로 요청을 보내는 API를 구현한다

### 추가 요구사항
- Front-End를 따로 구현하고, UI를 적용한다
- 챗봇 API는 로그인을 한 유저만 사용가능하다
- 챗봇 API는 각 사용자마다 하루 5번만 요청할 수 있도록 구현한다
- 채팅내용을 데이터베이스에 저장한다
- 저장된 채팅내역을 조회할 수 있도록 구현한다
- 저장된 채팅내역은 로그인을 한 본인만 볼 수 있게 한다
- AWS에 배포한다
- URL을 연결한다

### 기능명세서
![기능명세서](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/d909e0cb-61b8-47db-84ec-e019a78fe5f3)

### 마인드맵
![mindmap](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/a54b532f-6c3e-45a4-9dad-543ad4d436a5)

## 3. 개발 일정
2023.11.21 ~ 2023.11.30

![wbs](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/35d97cbf-6ed7-41f5-9b94-f189a2c8410c)

## 4. 개발 환경 및 배포

### 개발
#### Frontend
<span><img src="https://img.shields.io/badge/html-E34F26?style=for-the-badge&logo=html5&logoColor=white"></span>
<span><img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"></span>
<span><img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white"></span>
<span><img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white"></span>

#### Backend
<span><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"></span>
<span><img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"></span>

### AWS
![distribution](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/83ac58aa-80bf-4266-bb0b-eef7202184fe)

### 배포
[For Your Date](https://d3fjqjyzc4n459.cloudfront.net/)
```
Test 계정 정보
ID : test@test.com
PW : test1234!@#$
```

## 5. URL 구조

|구분|HTTP|URL|설명|비고|
|---|---|---|---|---|
|chat|GET|/chat/chat/|추천 전체 리스트 API|나의 글만 조회 가능
||POST|/chat/chat/|추천 내역 저장 API|로그인 유저만 가능
||GET|/chat/chat/{id}/|추천 상세내역 API|나의 글만 조회 가능
||DELETE|/chat/chat/{id}/|추천 내역 삭제 API|나의 글만 삭제 가능
||POST|/chat/chatbot/|OpenAI api 호출 API|로그인 유저만 가능, 1일 요청 5회 제한
|user|POST|/user/join/|회원가입 API|accessToken, refreshToken 발급
||POST|/user/login/|로그인 API|accessToken, refreshToken 발급
||POST|/user/logout/|로그아웃 API|accessToken, refreshToken 만료
||POST|/user/token/refresh/|사용자 accessToken 갱신 API|accessToken 갱신
||POST|/user/token/verify/|사용자 accessToken 유효성 검사 API|
||GET|/user/user/|사용자 정보 조회 API|
  
![swagger](https://github.com/Nam-Younghoon/for_your_date_front/assets/58909988/0ade1f8c-cec5-43bf-97ba-3b944380de68)

[Swagger로 테스트하기](https://api-for-your-date.kro.kr/api/schema/swagger-ui/)


## 6. 프로젝트 구조
```
📦for_your_date_api
 ┣ 📂.config
 ┃ ┣ 📂nginx
 ┃ ┃ ┗ 📜foryourdate.conf
 ┃ ┗ 📂uwsgi
 ┃ ┃ ┣ 📜foryourdate.ini
 ┃ ┃ ┗ 📜uwsgi.service
 ┣ 📂chat
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📂migrations
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜commons.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜permissions.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜throttlings.py
 ┃ ┣ 📜urls.py
 ┃ ┗ 📜views.py
 ┣ 📂foryourdate
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┗ 📜wsgi.py
 ┣ 📂user
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📂migrations
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜adapters.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜managers.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┗ 📜views.py
 ┣ 📜.env
 ┣ 📜.gitignore
 ┣ 📜README.md
 ┣ 📜db.sqlite3
 ┣ 📜manage.py
 ┗ 📜requirements.txt
```

## 7. ERD
![erd](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/9c117afa-5dea-4361-8737-57b8be038f38)


## 8. 프로토타입


## 9. 구현 내용

## 10. 트러블슈팅

## 11. 후기