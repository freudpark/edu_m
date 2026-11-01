# GitHub 저장소 검증 목록

휴대폰 서버(Termux PRoot Ubuntu)에서 분석, 설치, 검증한 저장소 기록입니다.
쓸만한 저장소는 `success/날짜_저장소명_목적/`에 보관합니다.

| 날짜 | 저장소 | 목적 | 검증 결과 | 판정 | 설치 위치 | 보관 폴더 |
|---|---|---|---|---|---|---|
| 2026-11-01 | [muxuuu/serenity-skill](https://github.com/muxuuu/serenity-skill) | AI 에이전트용 공급망 병목 투자 리서치 스킬 | 형식 검사 OK, Claude Code 인식·호출 OK, 오프라인 시험 OK | ✅ 유지 | `/root/.claude/skills/serenity-skill` | [success/2026-11-01_serenity-skill_공급망병목-투자리서치](success/2026-11-01_serenity-skill_공급망병목-투자리서치/) |
| 2026-11-01 | [tourmind-com/Tourmind-Booking-Skills](https://github.com/tourmind-com/Tourmind-Booking-Skills) (@c540361) | AI 에이전트용 호텔·항공 검색·예약·결제 스킬 (TourMind 서비스 연동) | 분석만 함, 설치·실행 안 함. 악성 코드는 없음. 예약 시 개인정보(여권·이메일)를 중국 도메인(airxapi.hlzinterface.cn)으로 전송, 호텔 관련 질문을 모두 가져가는 MUST USE 설정, 원격 자체 업데이트, Stripe 수수료 3.5% 환불 불가·항공권 환불 불가 | ❌ 삭제 | 없음 | 없음 |
