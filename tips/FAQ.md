## 자주 하는 실수, 궁금증

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

##### Q. 부분문제를 다 맞추지 않은 경우 0점으로 표시되게 하고 싶어요.

  - Task의 Score Type을 GroupMin으로 수정하고, Score Parameters를 아래와 같이 변경해주세요.
  - `[[<맞을 경우 보일 점수>, <테스트 케이스 개수>]]`
  - ex) [[100, 5]]

##### Q. 유저가 여러 파일을 제출하게 하고 싶어요

  - Task 설정에서 Submission Format을 고쳐주면 됩니다.
  - ['file_name.%l', 'file_name2.%l', ... , 'file_nameN.%l']

##### Q. 한 서버에서 여러 콘테스트를 동시에 열고 싶어요.
  - https://github.com/cms-dev/cms/issues/362

## 여러 파일 컴파일 하기

유저가 제출한 파일 + 서버에서 제출한 파일을 함께 컴파일 하고 싶은 경우 _(ex- 유저는 함수만 제출하고, 서버에서 메인 함수를 실행)_

1. Task의 Task type-Compilation을 `Submissions are compiled with a grader`로 바꿉니다.

2. 함께 컴파일될 파일(`Manager`)를 추가합니다.
    - 이 때 메인함수를 포함하는 파일의 이름은 반드시 grader.* 여야 합니다.

__예시.__

```c
// grader.c - Manager
#include "user_function.h"

int main(){
  foo();
}
```

```c
// user_function.h - Manager
void foo();
```

```c
// user_function.c - users submission
// 파일 이름은 submission format에서 지정
void foo(){
  printf("foo!");
}
```

## 에러가 일어나는 케이스

  - 테스트 케이스 이름 (codename)에 띄어쓰기가 있으면 파싱하는 과정에서 에러가 납니다.
  - 동일한 컨테스트의 여러 Task가 동일한 파일 이름으로 제출 받을 경우(Submission Format이 동일할 경우) 에러가 납니다.
