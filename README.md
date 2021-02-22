# LIKELION_Apply_Crawling

🦁 9th LikeLion at SCH apply page Selenium crawling

## 제작자

- 16학번 컴퓨터소프트웨어공학과 최민석
- 18학번 컴퓨터공학과 최세환

## 👨🏻‍💻 개요

- 멋쟁이사자처럼 지원자 정보 자동 추합 크롤링(Crawling) 프로그램
- 멋쟁이사자처럼 9기 모집 페이지를 이용 하면서, 지원자들의 정보를 모으고 필터 할 만한 수단이 없는 상태이다.
- "지원자들의 이름/전화 번호/합불 여부를 다루기 쉬운 `CSV` 파일로 자동 저장해주는 시스템" 을 구성했습니다.

## 🔨기술 스택

- Selenium
- Pandas

## 사용 전, 환경 세팅

1. Chrome 버전 확인 : 주소 창에 입력 - `chrome://version` ![image](https://user-images.githubusercontent.com/60251579/108708599-fd29a680-7554-11eb-845d-837ac698bbc4.png)

2. Chrome 버젼과 Chrome 드라이버 버전 맞추기.[ChromeDriver 다운 링크](https://chromedriver.chromium.org/downloads) ![image](https://user-images.githubusercontent.com/60251579/108708679-1c283880-7555-11eb-8590-0474dbf8850b.png)

3. 다운받은 `ChromeDriver` 파일을 클론받은 `Root` 폴더에 저장.

## 사용법

### 1. 깃 클론

`git clone https://github.com/minsgy/LIKELION_Apply_Crawling.git`

### 2. 종속성 다운로드

`pip install -r requirements.txt`

### 3.기본 세팅

학교 별 아이디. 비밀번호 설정 필요

1. 루트 디렉토리에 `secret.json` 파일 생성
2. `json` 형태로 작성함.
3. 지원서 운영진 아이디 : `APPLY_ID`, 지원서 운영진 비밀번호 : `APPLY_PW` 작성

※ 예시

![image](https://user-images.githubusercontent.com/64149514/108707484-66101f00-7553-11eb-9173-4e613f667043.png)
