# serenity-skill: 공급망 병목 투자 리서치 스킬

- **원본**: https://github.com/muxuuu/serenity-skill (MIT, v1.1.0, 커밋 193e409)
- **검증일**: 2026-11-01
- **판정**: ✅ 유지 (휴대폰 서버에 설치됨)

## 목적
AI 에이전트(Claude Code, Codex)용 투자 리서치 방법론 스킬입니다. 기술 붐이 일어날 때 공급망에서 늘리기 어려운 병목을 찾고, 그 병목으로 실제 이익을 내는 회사를 증거 중심으로 추립니다.
- 6단계 분석: 시스템 변화 → 공급망 위치 → 회사 노출도 → 이익 전환 → 밸류에이션 → 반론
- 사용 방식: 테마 스캔, 회사 주장 검증, 후보 비교, 학습 대화

## 보안 점검
- 실행 코드는 `scripts/validate_skill.py`(형식 검사) 하나뿐이며, 네트워크·시스템에 접근하지 않음
- 외부 전송, 키 탈취, 숨은 지시, 보이지 않는 문자 없음
- 매매나 계좌 조작 기능 없음

## 설치 위치 (휴대폰 서버)
`/root/.claude/skills/serenity-skill/` (SKILL.md, LICENSE, references, assets, examples, agents만 복사)

## 검증 결과
1. `validate_skill.py` → `OK: serenity-skill (380 description chars)`
2. Claude Code에서 스킬이 자동 인식되고 `/serenity-skill`로 호출됨을 확인
3. 시험 과제: 한국 시장, "한미반도체는 HBM 공급망의 핵심 병목 공급사다"를 오프라인으로 분해
   - 제품 역할(TC 본더), 상업 단계, 고객 집중도, 경쟁사, 반론(하이브리드 본딩 전환, 고객사 장비 다변화)으로 나누고, 확인할 항목을 표시함
   - 스킬 지침대로 "확인 안 됨"과 "없음"을 구분하고, 매매 권유 없이 연구 우선순위만 제시함

## 사용법
```
/serenity-skill 한국 시장으로, [테마 또는 회사] 를 조사해줘
```
주의: 기본 대상이 중국 A주이므로 **"한국 시장"이라고 꼭 지정**해야 합니다.

## stock_bot과의 관계
자동 연동 기능은 없습니다. stock_bot이 고른 후보(stage1/stage2)를 사람이 검토할 때 정성 분석 도구로 활용합니다.

## 삭제 방법
`rm -rf /root/.claude/skills/serenity-skill`
