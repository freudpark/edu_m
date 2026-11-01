# agent-desktop: AI 에이전트용 데스크톱 화면 조작 도구

- 원본: https://github.com/vercel-labs/agent-desktop (Vercel Labs, Apache-2.0, 커밋 9eb9b29, 2026-10-31)
- 분석일: 2026-11-01
- 판정: ✅ 유지. **설치는 보류**합니다 (윈도우 PC를 연결한 뒤 설치).
- 보관 방식: 원본이 약 67MB라서 사본은 넣지 않았습니다. 이 문서와 SOURCE.txt만 보관합니다.

## 목적
운영체제의 접근성 정보(accessibility tree)로 화면 구성을 읽고, AI가 버튼 클릭, 입력, 창 조작을 하게 해 주는 CLI와 C 라이브러리입니다. 이미지 인식 방식이 아니라서 빠르고 정확합니다.
- 기본은 마우스를 실제로 움직이지 않는 백그라운드 조작입니다.
- 명령은 60개입니다: 클릭·입력·스크롤, 앱 실행·종료, 창 관리, 알림, 클립보드, 스크린샷 등.
- 지원: macOS, Windows, Linux 데스크톱(AT-SPI)

## 보안 점검
- 외부 전송 코드가 없습니다. "telemetry"는 내부 기록용 이름이고, 접속 대상은 127.0.0.1뿐입니다.
- npm postinstall이 GitHub Releases에서 실행 파일을 받고 체크섬으로 검증합니다.
- 주의:
  - AI가 실제 PC를 조작합니다. 잘못 클릭하면 삭제, 발송, 주문까지 될 수 있습니다.
  - 화면을 읽은 결과에 사적인 내용이 들어갈 수 있습니다.
  - 부가 기능 `jev-desktop`은 화면 설명을 외부 서비스(api.typesafe.ai)로 보내므로 **사용하지 않습니다.**

## 이 환경에서
- 휴대폰(Termux PRoot)에는 그래픽 데스크톱이 없어서 쓸 수 없습니다.
- 윈도우 PC(또는 GUI가 있는 우분투 노트북)에서 쓸 수 있습니다. → plans/orchestra.md 3단계 참고

## 나중에 설치하는 방법 (윈도우 PC)
1. `npm install -g agent-desktop` → `agent-desktop version`
2. `agent-desktop skills get desktop`, `agent-desktop skills get platform`
3. 메모장으로 시험: snapshot → click/type → snapshot
4. 규칙 추가: "주문, 삭제, 메시지 발송, 결제 동작은 실행 전 반드시 사용자 확인"
