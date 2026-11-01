# GitHub 저장소 검증 목록

휴대폰 서버(Termux PRoot Ubuntu)에서 분석, 설치, 검증한 저장소 기록입니다.
쓸만한 저장소는 `success/날짜_저장소명_목적/`에 보관합니다.

| 날짜 | 저장소 | 목적 | 검증 결과 | 판정 | 설치 위치 | 보관 폴더 |
|---|---|---|---|---|---|---|
| 2026-11-01 | [muxuuu/serenity-skill](https://github.com/muxuuu/serenity-skill) | AI 에이전트용 공급망 병목 투자 리서치 스킬 | 형식 검사 OK, Claude Code 인식·호출 OK, 오프라인 시험 OK | ✅ 유지 | `/root/.claude/skills/serenity-skill` | [success/2026-11-01_serenity-skill_공급망병목-투자리서치](success/2026-11-01_serenity-skill_공급망병목-투자리서치/) |
| 2026-11-01 | [tourmind-com/Tourmind-Booking-Skills](https://github.com/tourmind-com/Tourmind-Booking-Skills) (@c540361) | AI 에이전트용 호텔·항공 검색·예약·결제 스킬 (TourMind 서비스 연동) | 분석만 함, 설치·실행 안 함. 악성 코드는 없음. 예약 시 개인정보(여권·이메일)를 중국 도메인(airxapi.hlzinterface.cn)으로 전송, 호텔 관련 질문을 모두 가져가는 MUST USE 설정, 원격 자체 업데이트, Stripe 수수료 3.5% 환불 불가·항공권 환불 불가 | ❌ 삭제 | 없음 | 없음 |
| 2026-11-01 | (직접 제작) knowledge-sources | 신뢰 출처 10곳 기반 지식·팩트체크·정책 스킬 | 형식 검사 OK, 인식 OK, 브루킹스·FA·위키·구텐베르크·아카이브 접근 OK | ✅ 유지 | `/root/.claude/skills/knowledge-sources` | [success/2026-11-01_knowledge-sources_신뢰출처-지식스킬](success/2026-11-01_knowledge-sources_신뢰출처-지식스킬/) |
| 2026-11-01 | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) (@9eb9b29) | AI 에이전트용 데스크톱 화면 조작 (접근성 트리) | 분석 완료, 외부 전송 없음. 휴대폰엔 GUI가 없어 실행 검증 못 함 | ✅ 유지 (설치 보류: 윈도우 PC 연결 후) | 미설치 | [success/2026-11-01_agent-desktop_AI-데스크톱-화면조작](success/2026-11-01_agent-desktop_AI-데스크톱-화면조작/) |
| 2026-11-01 | (직접 제작) repo-eval | 저장소 검증 9단계 체크리스트 스킬 | 형식 검사 OK, 인식 OK, 실사용 미검증 | ✅ 유지 | `~/.claude/skills/repo-eval` | [success/2026-11-01_repo-eval_저장소검증-체크리스트](success/2026-11-01_repo-eval_저장소검증-체크리스트/) |
