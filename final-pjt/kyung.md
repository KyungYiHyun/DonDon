## 경이현

#### 2024.11.18

- 게시글 및 댓글 CRUD 기능 관련 url, view 파일 편집 
- 기능 테스트 해야함 - 완료

#### 해결한 오류

```ImportError: cannot import name 'User' from 'article.models' (C:\Users\ME\OneDrive\바탕 화면\관관\10-pjt\final-pjt\final_pjt_back\article\models.py)``` 

- article / admin.py 파일에 ```from models import User``` 를 ```from accounts.models import User```로 바꿔 해결

#### 다음할일

- Comment 테이블에 userId 추가할지 말지 선택 - 완료


#### 2024.11.20

- 예금, 적금 전체조회
- 추천 예금, 추천 적금 조회
- 환율계산기 기능 추가
- vue 로그인, 회원가입 기능

#### 해결한 오류

- 환율계산기 기능을 구현할 때 인풋박스 2개로 v-model을 이용해서 구현하려고 했다.
그런데 1번 인풋의 값이 바뀌면 다른 2번 인풋값도 바뀌는데 그러면 또 2번 인풋값이 바뀌니까 1번 인풋값도 바뀌려고 한다.
이런 무한루프가 발생했다. 

- 해결방법 : flag 변수를 도입해서 1번 인풋값이 다 바뀌면 2번 인풋값이 바뀌도록 할려고 했는데 이것도 잘 안먹혔다 계산하는 함수가 실행되기 이전에 flag 변수를 바꾸는 코드가 비동기적으로 실행되어서 그런 것 같다.
그래서 setTimeOut 함수를 써서 계산함수가 다 끝나고 2번 인풋값이 바뀌면 flag 변수가 바뀌도록 하였다.


#### 2024.11.21

- 게시판 기능 완료
- 프로필페이지 조회 ,수정 완료


#### 해결한 오류

- 회원정보 수정 요청을 보낼 때 서버에서 patch 메서드로 구현했기 때문에 
vue에서도 axios 요청을 put이 아니라 patch로 보내야 한다.

