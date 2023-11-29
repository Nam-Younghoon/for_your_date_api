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
데이트 예정인 장소와 시간, 계절, 이동수단 등을 입력받아 ChatGPT로부터 데이트 코스를 추천받는다

## 2. 요구사항 분석 및 기능명세서
### 기본 요구사항

### 요구사항 명세서

### 마인드맵

## 3. 개발 일정

## 4. 개발 환경 및 배포

### 개발
<span><img src="https://img.shields.io/badge/-HTML5-E34F26?logo=HTML5&logoColor=white"/></span>
<span><img src="https://img.shields.io/badge/css3-1658a7?logo=css3&logoColor=white"/></span>
<span><img src="https://img.shields.io/badge/javascript-F7DF1E?logo=javascript&logoColr=white"/></span>
<span><img src="https://img.shields.io/badge/bootstrap-7952B3?logo=bootstrap&logoColor=white"/></span>
<span><img src="https://img.shields.io/badge/python-0769AD?logo=python&logoColor=white"/></span>
<span><img src="https://img.shields.io/badge/django-175339?logo=django&logoColor=white"/></span>

### AWS

### 배포


## 5. URL 구조

|구분|HTTP|URL|비고|
|---|---|---|---|
|chat|GET|/chat/chat/|추천 전체 리스트 API
||POST|/chat/chat/|추천 내역 저장 API
||GET|/chat/chat/{id}/|추천 상세내역 API
||DELETE|/chat/chat/{id}/|추천 내역 삭제 API
||POST|/chat/chatbot/|OpenAI api 호출 API
|user|POST|/user/join/|회원가입 API
||POST|/user/login/|로그인 API
||POST|/user/logout/|로그아웃 API
||POST|/user/token/refresh/|사용자 accessToken 갱신 API
||POST|/user/token/verify/|사용자 accessToken 유효성 검사 API
||GET|/user/user/|사용자 정보 조회 API
  
![swagger](https://github.com/Nam-Younghoon/for_your_date_front/assets/58909988/0ade1f8c-cec5-43bf-97ba-3b944380de68)

[Swagger로 테스트하기](https://api-for-your-date.kro.kr/api/schema/swagger-ui/)


## 6. 프로젝트 구조

## 7. ERD


## 8. 프로토타입


## 9. 구현 내용

## 10. 트러블슈팅

## 11. 후기