# video-use: Claude Code용 대화형 영상 편집 스킬

- 원본: https://github.com/browser-use/video-use (Browser Use, MIT, 커밋 43cfc56, 2026-10-08)
- 분석일: 2026-11-02
- 판정: ✅ 유지. **설치는 보류**합니다 (윈도우 PC 또는 노트북을 연결한 뒤).
- 보관 방식: 분석 문서와 원본 주소만 보관합니다 (나중에 같은 커밋을 다시 받으면 됩니다).

## 목적
원본 영상을 폴더에 넣고 "편집해 줘"라고 하면 `edit/final.mp4`를 만들어 줍니다.
- 군더더기 말과 빈 구간 삭제, 색 보정, 컷마다 30ms 오디오 페이드
- 자막, 애니메이션 오버레이 (Manim, Remotion, HyperFrames)
- 렌더링 결과를 스스로 검수 (최대 3회)
- 순서: 원본 확인 → 계획 제안 → **사용자 승인** → 편집 → 검수

## 작동 원리
ElevenLabs Scribe로 단어 단위 타임스탬프 받아쓰기를 만들고, LLM은 그 텍스트(약 12KB)와 필요한 시점의 타임라인 이미지만 보고 편집 지점을 정합니다.

## 보안 점검
- 외부 전송은 helpers/transcribe.py의 한 곳뿐입니다: `https://api.elevenlabs.io/v1/speech-to-text`. **음성이 업로드되며 유료 API 키가 필요합니다.**
- `shell=True`, eval/exec 없음. 숨은 문자 없음.
- 주의: 애니메이션을 만들 때 SKILL.md가 `npx --yes hyperframes`, `npx create-video@latest`로 외부 npm 패키지를 그때그때 설치합니다.

## 이 환경에서
- 휴대폰: ffmpeg와 numpy가 없고, librosa는 Termux에서 빌드가 어렵습니다(pandas와 같은 문제). 렌더링 성능도 부족해 부적합합니다.
- 윈도우 PC나 노트북에 맞습니다 → plans/orchestra.md 3단계.

## 나중에 설치하는 방법 (PC/노트북)
1. ffmpeg 설치. 저장소를 clone하고 `pip install -e .` (또는 `uv sync`)
2. `~/.claude/skills/video-use`에 저장소 폴더를 심볼릭 링크로 연결 (helpers/와 SKILL.md가 같은 폴더에 있어야 함)
3. `.env`에 ELEVENLABS_API_KEY를 넣음 (대화창에 붙여 넣지 말 것)
4. 짧은 시험 영상 하나로 검증
5. 회사 영상이나 사적인 영상은 외부 업로드 여부를 먼저 판단
