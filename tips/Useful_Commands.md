## CMS Useful Console Commands

### Essential Commands

---

- 어드민 추가
```
$ cmsAddAdmin name
```

- 어드민 웹페이지 실행
```
$ cmsAdminWebServer
```

- 콘테스트 실행
```  
$ cmsResourceService -a
```

- 로그 띄우기
```
$ cmsLogService
```

---

### Web/Console Commands

웹페이지에서도 할 수 있지만 자동화시킬 수 있는 커맨드

---

- 유저 추가하기 ([사용 스크립트](https://github.com/ryanking13/cms-guide/blob/master/scripts/cms_user_adder.py))

```
$ cmsAddUser

usage: cmsAddUser [-h] [-p PASSWORD] [-e EMAIL] [-t TIMEZONE] [-l LANGUAGES]
                  first_name last_name username

Add a user to CMS.

positional arguments:
  first_name            given name of the user
  last_name             family name of the user
  username              username used to log in

optional arguments:
  -h, --help            show this help message and exit
  -p PASSWORD, --password PASSWORD
                        password, leave empty to auto-generate
  -e EMAIL, --email EMAIL
                        email of the user
  -t TIMEZONE, --timezone TIMEZONE
                        timezone of the user, e.g. Europe/London
  -l LANGUAGES, --languages LANGUAGES
                        comma-separated list of preferred languages

```

- 유저 삭제하기 ([사용 스크립트](https://github.com/ryanking13/cms-guide/blob/master/scripts/cms_user_remover.py))

```
$ cmsRemoveUser

usage: cmsRemoveUser [-h] username

Remove a user from a contest in CMS.

positional arguments:
  username    username of the user

optional arguments:
  -h, --help  show this help message and exit
```

- 유저 콘테스트에 등록하기 ([사용 스크립트](https://github.com/ryanking13/cms-guide/blob/master/scripts/cms_user_participater.py))

```
$ cmsAddParticipation

usage: cmsAddParticipation [-h] [-c CONTEST_ID] [-i IP] [-d DELAY_TIME]
                           [-e EXTRA_TIME] [-p PASSWORD] [-t TEAM] [-n] [-u]
                           username

Add a participation to CMS.

positional arguments:
  username              username to add to the contest

optional arguments:
  -h, --help            show this help message and exit
  -c CONTEST_ID, --contest-id CONTEST_ID
                        id of the contest the users will be attached to
  -i IP, --ip IP        ip address of this user
  -d DELAY_TIME, --delay_time DELAY_TIME
                        how much the contest is shifted, in seconds
  -e EXTRA_TIME, --extra_time EXTRA_TIME
                        how much additional time, in seconds
  -p PASSWORD, --password PASSWORD
                        how much additional time, in seconds
  -t TEAM, --team TEAM  code of the team for this participation
  -n, --hidden          if the participation is hidden
  -u, --unrestricted    if the participation is unrestricted
```

- 유저 콘테스트 등록 취소하기

```
$ cmsRemoveParticipation

usage: cmsRemoveParticipation [-h] [-c CONTEST_ID] username

Remove a participation from a contest in CMS.

positional arguments:
  username              username of the user

optional arguments:
  -h, --help            show this help message and exit
  -c CONTEST_ID, --contest-id CONTEST_ID
                        id of contest the user is in

```

---

### Console Only Commands

웹에서는 같은 기능을 할 수 없는 커맨드

---

- 제출 파일 export 하기

```
$ cmsExportSubmissions

usage: cmsExportSubmissions [-h] [-c CONTEST_ID] [-t TASK_ID] [-u USER_ID]
                            [-s SUBMISSION_ID] [--utf8] [--add-info]
                            [--min-score MIN_SCORE] [--filename FILENAME]
                            [--unique | --best]
                            output_dir

Export CMS submissions to a folder.

positional arguments:
  output_dir            directory where to save the submissions

optional arguments:
  -h, --help            show this help message and exit
  -c CONTEST_ID, --contest-id CONTEST_ID
                        id of contest (default: all contests)
  -t TASK_ID, --task-id TASK_ID
                        id of task (default: all tasks)
  -u USER_ID, --user-id USER_ID
                        id of user (default: all users)
  -s SUBMISSION_ID, --submission-id SUBMISSION_ID
                        id of submission (default: all submissions)
  --utf8                if set, the files will be encoded in utf8 when
                        possible
  --add-info            if set, information on the submission will be added in
                        the first lines of each file
  --min-score MIN_SCORE
                        ignore submissions which scored strictly less than
                        this (default: 0.0)
  --filename FILENAME   the filename format to use (default: {id}.{name}{ext})
  --unique              if set, only the earliest best submission will be
                        exported for each (user, task)
  --best                if set, only the best submissions will be exported for
                        each (user, task)

```

__사용 예시__

    cmsExportSubmissions directory -c 6 -t 24 --utf8 --add-info --min-score 100 --filename {user}.{id}.{name}{ext}

`--utf8 --add-info` 파라미터를 추가하면 아래와 같은 정보가 제출 파일 최상단에 포함됨.

```
/**
* user:  <username>
* fname: <first name>
* lname: <last name>
* task:  <task name>
* score: <score>
* date:  <timestamp>
*/
```

`--filename`에서 지정할 수 있는 파라미터

| parameter | description   |
| ----------|-------------- |
| {id}      | submission ID |
| {name}    | submitted file name (submission format)|
| {user}    | username |
| {ext}     | extension |
| {time}    | submission time |
