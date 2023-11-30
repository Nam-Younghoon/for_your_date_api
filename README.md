# For Your Date [데이트를 부탁해]👫
- 데이트 코스를 고민하는 대한민국 커플들을 위해 자동으로 데이트 코스를 추천해주는 서비스입니다

## 목차
1. [프로젝트 목표](#1-프로젝트-목표)
2. [요구사항 분석 및 기능명세서](#2-요구사항-분석-및-기능명세서)
3. [개발 일정](#3-개발-일정)
4. [개발 환경 및 배포](#4-개발-환경-및-배포)
5. [URL 구조](#5-URL-구조)
6. [프로젝트 구조](#6-프로젝트-구조)
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
- DRF을 이용하여 구현
- 회원가입, 로그인을 구현
- 기본적인 CRUD를 구현
- ChatGPT로 요청을 보내는 API를 구현
- Front-End를 따로 구현, UI 적용
- 챗봇 API는 로그인을 한 유저만 사용가능
- 챗봇 API는 각 사용자마다 하루 5번만 요청 가능
- 채팅내용을 데이터베이스에 저장
- 저장된 채팅내역을 조회할 수 있도록 구현
- 저장된 채팅내역은 로그인을 한 본인만 볼 수 있게 구현
- AWS에 배포
- URL을 연결

### 추가 요구사항
- 개인 도메인을 등록하여 https 추가
    - Certbot을 사용하여 HTTPS 추가
- Frontend와 Backend 따로 배포
    - Frontend는 AWS의 S3 + CloudFront 채택
    - Backend은 AWS의 Lightsail 채택

### 마인드맵
![mindmap](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/a54b532f-6c3e-45a4-9dad-543ad4d436a5)

### 기능명세서
![기능명세서](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/d909e0cb-61b8-47db-84ec-e019a78fe5f3)


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

- Frontend Repository: [For_Your_Date_Front](https://github.com/Nam-Younghoon/for_your_date_front)


#### Backend
<span><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"></span>
<span><img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"></span>

### AWS
![distribution](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/83ac58aa-80bf-4266-bb0b-eef7202184fe)

### 배포
URL : [For Your Date](https://d3fjqjyzc4n459.cloudfront.net/)
```
Test 계정 정보
ID : test@test.com
PW : test1234!@#$
```

## 5. URL 구조
BASE_URL : https://api-for-your-date.kro.kr/
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
|||
|---|---|
|![oven_index](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/288e1bd1-d069-43a8-9f22-da8fb93ddf6a)홈페이지|![oven_login](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/e6a22d21-702b-4482-b444-35b8ef4c17fb)로그인|
|![oven_register](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/2e1ee324-070b-4f77-a81a-2c21cc81a96e)회원가입|![oven_list](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/392204d5-640e-49f5-b10a-471d7d168295)전체 리스트|
|![oven_detail](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/c2a0b5a8-df12-46ad-a44a-6ff504daa5b1)게시물 상세|![oven_create](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/81acf261-1d15-4ccb-8833-788d1a1bad2e)게시물 생성|
|![oven_result](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/d944f5f3-44a2-4c6d-8927-5416e0745773)추천 결과|

[카카오오븐](https://ovenapp.io/view/kwbjeFLha1aJL2YahIlDtwaDOspVckKM/YFn6w)


## 9. 구현 내용

### 홈페이지
![gif_main](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/5f4f0518-a612-4fc4-8595-0bc7850d0e38)
- 대문 페이지입니다
- 로그인, 회원가입 및 메인페이지로 이동할 수 있습니다

### 회원가입
![gif_register](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/e638879c-906c-48a0-a229-9bd8f0651767)
- 아이디, 닉네임, 비밀번호, 비밀번호 확인을 입력받아 회원가입을 진행합니다
- 회원가입 성공 시, 서버는 AccessToken과 RefreshToken을 발행합니다

### 로그인
![gif_login](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/72b5c9c3-7b93-4d2d-84de-a8aee4a300ea)
- 아이디, 비밀번호를 입력받아 로그인을 진행합니다
- 로그인 성공 시, 서버는 AccessToken과 RefreshToken을 클라이언트에게 반환해주고 클라이언트는 localStorage에 저장합니다

### 게시글 조회 및 상세보기
![gif_detail](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/470c8c3f-47d1-46cf-8963-5a6e1ddeec71)
- 내가 추천받았던 데이트 코스들과 그 상세 내용을 볼 수 있습니다
- 로그인이 되어있지 않다면 Login 페이지로 Redirect되고, 로그인한 사용자라면 내가 저장한 데이트코스들만 조회할 수 있습니다
- 다른 사용자의 게시물에 접근을 시도한다면, statusCode 403번을 반환해주고 열람 권한이 없음을 사용자에게 알려줍니다

### 게시물 삭제
![gif_delete](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/03204e6c-b9bb-40d8-ae0b-60a508c50aed)
- 내가 저장한 데이트코스를 삭제할 수 있습니다
- 서버는 사용자가 작성자임을 확인하고, 해당 글의 작성자임이 검증된다면 글을 삭제합니다

### 데이트 추천받기
![gif_recommand_](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/7afaf63c-f2e8-4fb8-84ab-cdee928d51d1)
- 데이트 장소, 계절, 시간, 교통수단을 입력받아 데이트 코스를 추천받습니다
- 서버는 OpenAI API를 통해 ChatGPT에게 요청하고, 받은 응답값을 클라이언트에게 전달합니다

### API 호출 제한
![gif_limit](https://github.com/Nam-Younghoon/for_your_date_api/assets/58909988/15a2a426-5ca1-4889-aeb5-f860e8b4cf1a)
- 사용자는 데이트코스를 하루 최대 5회만 추천받을 수 있습니다
- 5회를 초과하게 된다면, 서버는 statusCode 429_Too Many Request를 응답하여 사용자에게 횟수 초과를 알려줍니다

## 10. 트러블슈팅
### 504 Gateway Time-out  
OpenAI API를 사용하는 [POST] "/chat/chatbot/"에서 로컬에선 문제가 없었는데,
배포하고 난 후 실제 클라이언트에서 간헐적으로 504 Gateway Time-out이 발생하면서 응답이 제대로 오지 않는 상황이 발생하였습니다.  
해당 케이스를 테스트해본 결과, 요청 후 정확히 1분이 초과되는 순간 해당 에러가 발생하였는데 이는 AWS의 CloudFront에서 자체적으로 오랜시간 응답이 없는 연결이 지속될 경우 연결을 끊어버려서 발생하는 문제임을 확인했습니다.  

해당 문제를 해결하기 위해
```
1. 해당 API로부터 504 에러가 발생될 시 성공할 때까지 데이터 그대로 재요청하기  
2. 사용자에게 실패를 알리고 재시도를 요청하기  
3. AWS Support팀을 통해 60초 제한을 늘려보기  
4. OpenAI API의 응답을 더 빠르게 만들어보기  
```
라는 방법을 생각해보았으며, 4번 방법을 채택하여 해결해보기로 했습니다.    

OpenAI 공식 사이트의 docs와 포럼 내용을 토대로 기존 사용했던 OpenAI의 모델인 "gpt-3.5-turbo"를 "gpt-3.5-turbo-1106"으로 변경함으로서 3-4분정도 걸리는 응답속도를 15-17초 정도로 줄여 문제를 해결할 수 있었습니다.

## 11. 후기
이번 프로젝트는 프론트엔드와 백엔드로 나누어서 진행한 프로젝트였습니다.  
확실히 두가지를 한꺼번에 진행하는 모놀리식보다 마이크로식이 좀 더 공수가 들고, 애먹었던 상황이 있었던 것 같습니다.  
하지만 클라이언트, 서버를 따로 개발함으로서 각 영역별로 나누어서 개발한다면 유지보수와 관리 측면에서 더 높은 효율을 낼 수 있겠다라는 생각이 들었습니다.  
또, JWT를 이용한 사용자 인증 관리 및 외부 API를 내 서비스에 적용해봄으로서 재미를 느낄 수 있었습니다.