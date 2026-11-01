---
name: knowledge-sources
description: Answer knowledge, fact-check, learning and policy questions from a curated set of trusted sources (Brookings, Wikipedia, Foreign Affairs, Snopes, Open Yale Courses, Khan Academy, Project Gutenberg, Internet Archive, Pixabay, Pexels). Use automatically for factual or background-knowledge questions, rumor checks, history/philosophy/science learning, "심심해/아무거나" knowledge requests, daily knowledge cards, and whenever drafting public policy analysis, personal work rules/strategies, or company policy/planning documents. Do not use for coding, stock research, or system administration tasks.
metadata:
  author: freudpark
  version: "1.1.0"
---

# Knowledge Sources

Goal: give the user a trustworthy, easy answer built from the curated sources first, with links they can follow. Answer in Korean, polite, conclusion first.

How to reach each site and its limits: [sources](references/sources.md).

## Which sources fit which request
| Request | Start with |
|---|---|
| Fact, concept, person, event | Wikipedia (ko → en; zh for China topics), then Khan / Open Yale for explanation |
| Rumor or viral claim | Snopes, Wikipedia, Internet Archive (original or deleted pages). Verdict: 사실 / 거짓 / 일부 사실 / 확인 불가 |
| Public policy, economy, technology, geopolitics | Brookings + Foreign Affairs. Show where they disagree; add 찬성 근거 / 반대 근거 / 한국에 주는 시사점 |
| Rules, plans or strategy Claude drafts for the user | Brookings research on the field, as background principles. Keep the result practical |
| Company policy or planning document | Brookings + Foreign Affairs for evidence, Wikipedia for definitions. Never put company-confidential details into search queries |
| A topic to learn | Wikipedia → Open Yale / Khan lectures → Gutenberg originals → Internet Archive |
| "심심해", "아무거나", daily card | Pick a surprising topic from history, science, philosophy or literature; avoid recent repeats |
| Images or video | Pixabay / Pexels, with the license summary |

Fall back to general search when the curated sources have nothing; say so in one line.

## Output
Short by default: one-line conclusion, 3–7 plain lines, 1–3 "더 보기" links, then sources with dates. Go deep only when the user asks ("자세히").

Daily card (for Telegram, plain text):
```
🃏 오늘의 지식: <제목>
<3~5줄>
💡 왜 흥미로운가: <한 줄>
📚 더 보기: <URL 1~2개>
```

## Standards
- Read a page before citing it; mark anything unverified "미확인". Label expert pieces as analysis ("~의 분석"), not settled fact.
- Note "요약만 확인" when Foreign Affairs is paywalled.
- Keep quotes short; never send the user's personal or company data to any site.

## Improve this skill
After a use where something went wrong (a source unreachable, wrong routing, the user corrected the answer), fix the cause here or in `references/sources.md`, bump `metadata.version`, and note it in one line in the user's lessons file. Remove instructions that turn out unnecessary.
