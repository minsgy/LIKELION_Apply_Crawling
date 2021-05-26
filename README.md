# LIKELION_Apply_Crawling

🦁 9th LikeLion at SCH apply page Selenium crawling

## 제작자

- 순천향대학교 16학번 컴퓨터소프트웨어공학과 [최민석](https://github.com/minsgy)

## DEMO GIF

<img src="./crawling_demo.gif" width='500px'>

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

### 2. 가상 환경 생성 및 실행 후, 종속성 다운로드

- `python -m venv <가상환경 이름>`
- `. <가상환경 이름>/script/activate`, mac:`. <가상환경 이름>/bin/activate`
- `pip install -r requirements.txt`

### 3.기본 세팅

학교 별 아이디. 비밀번호 설정 필요

1. 루트 디렉토리에 `secret.json` 파일 생성
2. `json` 형태로 작성함.
3. 지원서 운영진 아이디 : `APPLY_ID`, 지원서 운영진 비밀번호 : `APPLY_PW` 작성

※ 예시

- ![image](https://user-images.githubusercontent.com/64149514/108707484-66101f00-7553-11eb-9173-4e613f667043.png)

### 4. 실행 과정

- `python made_find.py` 실행
- 크롬이 켜지면서, 크롤링 과정을 거치고 Chrome 종료.
- `UserList.csv` 파일 생성 (이름/전화번호/합불 여부)

### 5. 도음을 주신 분들께 감사를 표합니다.

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Woo-Yeol"><img src="https://avatars.githubusercontent.com/u/63551948?v=4" width="100px;" alt=""/><br /><sub><b>Woo-Yeol</b></sub></a><br />
    </td>
    <td align="center"><a href="https://github.com/Mactto"><img src="https://avatars.githubusercontent.com/u/64149514?v=4" width="100px;" alt=""/><br /><sub><b>Mactto</b></sub></a><br />
    </td>
    <td align="center"><a href="https://github.com/ygnaiih1680"><img src="https://avatars.githubusercontent.com/u/48740869?v=4" width="100px;" alt=""/><br /><sub><b>ygnaiih1680</b></sub></a><br />
    </td>
    <td align="center"><a href="https://github.com/ndaemy"><img src="https://avatars.githubusercontent.com/u/18691542?v=4" width="100px;" alt=""/><br /><sub><b>ndaemy</b></sub></a><br />
    </td>
    <td align="center"><a href="https://github.com/noah0316"><img src="https://avatars.githubusercontent.com/u/63908856?v=4" width="100px;" alt=""/><br /><sub><b>ndaemy</b></sub></a><br />
    </td>
    <td align="center"><a href="https://github.com/13circle"><img src="https://avatars.githubusercontent.com/u/25195384?v=4" width="100px;" alt=""/><br /><sub><b>13circle</b></sub></a><br />
    </td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
