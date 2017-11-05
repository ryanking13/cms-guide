## 설치 직후에 해야할 일

  - Admin 추가
```
$ cmsAddAdmin name
```

  - Admin 서버(페이지) 실행 (default = 8889 port)
```
$ cmsAdminWebServer
```

Admin 웹 페이지를 킨 순간부터 기본적인 작업은 대부분 웹 페이지에서 수행 가능합니다.


## 콘테스트 관리

  - 어드민 페이지에서 Contest 생성
  - Task를 생성한 뒤 Contest에 Task를 추가하는 방식

  - 콘테스트 실행
```  
$ cmsResourceService -a
```

  - 로그를 보고 싶을 때
```
$ cmsLogService
```
