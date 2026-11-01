---
name: knowledge-sources
description: Answer knowledge, fact-check, learning and policy questions from a curated set of trusted sources (Brookings, Wikipedia, Foreign Affairs, Snopes, Open Yale Courses, Khan Academy, Project Gutenberg, Internet Archive, Pixabay, Pexels). Use automatically for factual or background-knowledge questions, rumor checks, history/philosophy/science learning, "심심해/아무거나" knowledge requests, daily knowledge cards, and whenever drafting public policy analysis, personal work rules/strategies, or company policy/planning documents. Do not use for coding, stock research, or system administration tasks.
metadata:
  author: freudpark
  version: "1.0.0"
---

# Knowledge Sources

Answer in Korean, polite tone, conclusion first in plain words. Use the curated sources below before general web search. See [sources](references/sources.md) for access methods and per-site limits.

## Pick the mode

| User intent | Mode |
|---|---|
| Question about a fact, concept, event, person | **A. 질문 답변** |
| "이거 사실이야?", rumor, viral claim | **B. 팩트체크** |
| Public policy, economics, technology, geopolitics | **C. 정책 분석** |
| Claude is drafting rules, plans, strategy for the user (e.g. orchestra plan, security rules, investment principles) | **D. 내 작업 규칙·전략** |
| Company policy document, proposal, planning report | **E. 회사 정책·기획** |
| A topic to learn about ("~에 대해 알려줘") | **F. 주제 종합 정리** |
| "심심해", "아무거나", no topic | **G. 랜덤 지식** |
| Scheduled daily run | **H. 지식 카드** |
| Needs images or video for content | **I. 소스 찾기** |

## Source routing (check in this order)

- **A 질문:** Wikipedia (ko → en; zh only when the topic is China-related) → Khan Academy / Open Yale for explanations → general search to fill gaps.
- **B 팩트체크:** Snopes → Wikipedia → Internet Archive Wayback (original or deleted pages) → general search for the primary source. Give a verdict: 사실 / 거짓 / 일부 사실 / 확인 불가.
- **C 정책:** Brookings (reports, data) + Foreign Affairs (international view) → Wikipedia for background terms. Show where the two disagree.
- **D 내 작업 규칙·전략:** Brookings research on the relevant field (technology governance, cybersecurity, AI, economics) as background principles. Keep the result practical; cite the principle each rule rests on only when it adds real value.
- **E 회사 정책·기획:** Brookings + Foreign Affairs for evidence and trends, Wikipedia for definitions. **Never put company-confidential details into search queries**; search with generic terms only.
- **F 주제 정리:** Wikipedia summary → Open Yale / Khan lecture to go deeper → Gutenberg original texts (classics) → Internet Archive for older books or media → Brookings / Foreign Affairs if the topic has a current policy angle.
- **G 랜덤:** Pick one surprising topic from history, science, philosophy or literature (vary across calls; avoid repeating recent topics in this conversation). Build it like F, short.
- **H 지식 카드:** Same as G, in the card format below.
- **I 소스:** Pixabay / Pexels. State the license (free to use, no attribution required, but no resale as-is and no implying endorsement by people shown). Give links, never download into project folders unasked.

If a curated source has nothing relevant, say so in one line and use general search. Never invent a source.

## Answer format

Default: **short first, deeper on request.**

```
**한 줄 결론**

핵심 3~7줄 (쉬운 말)

📚 더 보기: 강의 / 원전 / 보고서 링크 1~3개 (있을 때만)

출처: [사이트명: 제목](URL) (날짜가 있으면 날짜)
```

- When the user says "자세히", expand: background, key points per source, disagreements between sources, and limits.
- Policy answers (C, E): add **찬성 근거 / 반대 근거 / 한국에 주는 시사점** as short bullets.
- Fact-checks (B): verdict first, then the evidence, then where the claim came from.

**지식 카드 (H) 형식:**
```
🃏 오늘의 지식: <제목>
<3~5줄 이야기처럼>
💡 왜 흥미로운가: 한 줄
📚 더 보기: 링크 1~2개
```

## Rules

- Read the page before citing it; a search snippet alone is not verification. Mark anything unverified as "미확인".
- Wikipedia is a starting point: for contested or important facts, follow its cited primary source.
- Foreign Affairs is often paywalled. If only the abstract is readable, say "요약만 확인" next to it.
- Keep quotes short and give the link; summarize instead of copying long passages.
- Separate facts from interpretation. Brookings and Foreign Affairs pieces are expert opinion, not settled fact; label them as "~의 분석".
- Do not send the user's personal or company data to any site.
