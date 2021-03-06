># 아파트 관리비 시스템 보고서 API
아파트 관리비 확인용 페이지로써 관리비 관리를 위한 페이지입니다.
* 관리자 : 각 세대의 관리비 확인 가능
* 입주민 : 개별 관리비 내역 확인 가능

> ## 폴더 구조
```
.
├── Dockerfile
├── README.md
├── api
│   ├── admins
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── publics
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── urls.py
├── aptment
│   ├── asgi.py
│   ├── permissions.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── clients
│   └── token-auth-test.py
├── docker-compose.yml
├── manage.py
├── my_settings.py
└── requirements.txt
```


>## 관리자 권한 API
- 전 세대별 관리비 확인용 관리자 생성을 할 수 있습니다.

>## 보고서 API
1. 관리자는 세대별 관리비를 확인할 수 있습니다. (관리사무소용 API)
    - 관리자 권한 API에서 만든 관리용 아이디와 비밀번호 통과해야만 이 API에 접근할 수 있습니다.
2. 각 세대별로 자신의 관리비를 확인할 수 있습니다. (세대별 관리비 API)
    - 각 호수와 정해진 비밀번호를 통과해야만 이 API에 접근할 수 있습니다.

>## 기능 요구사항
- API 요청과 응답은 JSON 형태이며, 메서드와 상태 코드는 HTTP 스펙을 따릅니다.
- 최대 1,000 세대가 거주하는 아파트 단지입니다.
- 세대별 고유번호는 네 자리입니다. (ex. 1층 첫 세대 = 0101호, 25층 마지막 세대 = 2509호)
- 세대 비밀번호와 관리용 비밀번호는 네 자리입니다.
- Django Rest Framework으로 작성하였습니다.
- docker를 사용해서 docker가 설치된 환경에서 바로 `docker-compose`를 사용하여 server를 실행시킬 수 있도록 만듭니다.


> ## 설치 방법

docker 설치 (다운로드)

https://www.docker.com/products/docker-desktop

git clone 실행
```
git clone https://github.com/araaaaan/apartment-system.git
```
docker compose 실행 
```
$ docker-compose up
```

>## 사용 방법 

 1. api/admin/register 에서 관리자 권한의 username / password 입력 
 2. 인증 후 api/admin에서 전체 호수 관리비 확인 및 관리비 입력가능
 3. api/publics에서  자신의 호수(4자리)와 부여 받은 비밀번호 입력 후 개인 관리비 확인가능

[관리자 계정 생성]

<img width="700" alt="스크린샷 2021-07-23 오후 5 14 28" src="https://user-images.githubusercontent.com/81959334/126760986-e881e215-d82b-4cdc-bc98-0f5bccc3c93c.png">

[관리자 계정 로그인 후 관리비 입력]

<img width="700" alt="스크린샷 2021-07-23 오후 5 12 23" src="https://user-images.githubusercontent.com/81959334/126761019-3e04429e-c2c5-418f-989f-8c10dcb107d3.png">

[개별 호수 계정 입력]

<img width="700" alt="스크린샷 2021-07-23 오후 5 13 33" src="https://user-images.githubusercontent.com/81959334/126761013-67168d8a-885e-4b33-a12a-5741af07774e.png">

[개별 호수 관리비 확인]

<img width="700" alt="스크린샷 2021-07-23 오후 5 13 46" src="https://user-images.githubusercontent.com/81959334/126761000-540174cb-965c-42a1-a835-db64e3af51c1.png">

 **기능 별 url**
|기능|URL|
|:---:|:---:|
|관리자 권한 부여|api/admin/register|
|전체 관리비 확인|api/admin|
|호수 별 관리비 확인|api/publics|
 
