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
| 2026-11-02 | [browser-use/video-use](https://github.com/browser-use/video-use) (@43cfc56) | Claude Code 대화형 영상 편집 스킬 | 분석 완료, 외부 전송은 ElevenLabs STT 한 곳(유료 키), npx 자동 설치 주의. 휴대폰엔 부적합(librosa/ffmpeg) | ✅ 유지 (설치 보류: PC/노트북 연결 후) | 미설치 | [success/2026-11-02_video-use_AI-영상편집](success/2026-11-02_video-use_AI-영상편집/) |
| 2026-11-05 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) (@7716ee8) | 미국·한국 핵심 종목 아침 브리핑 가능성 검토 | 분석만 함, 저장소 코드 실행 안 함. Qt6 PC 프로그램(휴대폰 부적합), 클라우드 텔레메트리 포함, AI 기능은 api.fincept.in 유료 서버로 전송, 한국 전용 연동 없음(야후·구글뉴스 의존), pandas 필요 | ❌ 삭제 (사용자 결정: 브리핑 안 함) | 없음 | 없음 |
