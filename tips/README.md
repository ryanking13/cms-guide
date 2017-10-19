## Contest Management System Tips

### 설치 직후에 해야할 일

  - 어드민 추가
```
$ cmsAddAdmin name
```

  - 어드민 서버(페이지) 실행 (default = 8889 port)
```
$ cmsAdminWebServer
```

  - 이후는 어드민 페이지에서 관리 가능

### 콘테스트 관리

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

### 자주 하는 실수

##### Q. 컴파일은 되는데 채점이 안 돼요!
  - Task에 time limit, memory limit이 지정되어 있지 않으면 채점이 진행되지 않습니다.

##### Q. 여러 번 제출했는데 그 중에서 최고점을 점수로 하고 싶어요.  
  - Task의 Score mode 디폴트가 `Use best among tokened and last submissions (IOI 2010-2012)` 인데, 이 방식은 마지막에 받은 점수가 자신의 점수가 됨. 전체 제출 중 최고점을 점수로 하려면 `Use best among all submissions (IOI 2013-)`로 고쳐주어야 합니다.

##### Q. `cmsResourceService` 실행했는데 웹 페이지가 안나와요.

  - 실행 중인 `cmsResourceService`를 끄고, 아래 커맨드를 실행한 뒤 다시 `cmsResourceService`를 켜보세요.
```
$ cmsContestWebServer
```

##### Q. 패스워드를 바꾸고 싶어요

  - 어드민 페이지에서 변경이 가능합니다.
  - 유저가 직접 변경하는 것은 불가능합니다.

##### Q. 제출했는데 점수가 안보여요

  - 테스트 케이스를 public으로 한 경우에만 점수가 유저에게 공개됩니다.


### 에러가 일어나는 케이스

  - 테스트 케이스 이름 (codename)에 띄어쓰기가 있으면 파싱하는 과정에서 에러가 납니다.
