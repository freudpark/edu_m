# Curated sources: access methods and limits

Verified access from this environment on 2026-11-01 is marked ✅.

| # | Site | Best for | How to access | Limits |
|---|---|---|---|---|
| 1 | Brookings — https://www.brookings.edu | Economics, technology, policy research, data | ✅ WebSearch with `allowed_domains: ["brookings.edu"]`, then WebFetch the article or PDF | US-centric viewpoint |
| 2 | Wikipedia — https://ko.wikipedia.org, https://en.wikipedia.org, https://zh.wikipedia.org | Fast overview of any field, definitions, history | ✅ WebFetch `https://ko.wikipedia.org/wiki/<제목>` (exact title; URL-encode). If 404, search with `allowed_domains: ["wikipedia.org"]` to find the exact title | Anyone can edit; verify important facts via its references. Korean articles are often shorter, so check English for depth |
| 3 | Foreign Affairs — https://www.foreignaffairs.com | International relations, global economy, long-term trends | ✅ WebSearch with `allowed_domains: ["foreignaffairs.com"]` | Many articles paywalled; body may not be readable |
| 4 | Snopes — https://www.snopes.com | Fact-checking rumors, viral claims | WebSearch with `allowed_domains: ["snopes.com"]` | Mostly US/English rumors; for Korean rumors also search Korean fact-check outlets |
| 5 | Open Yale Courses — https://oyc.yale.edu | University lectures: history, philosophy, literature, economics, science | WebSearch with `allowed_domains: ["oyc.yale.edu"]`; course pages list lectures, transcripts | Lectures are mostly 2006–2015 recordings; English only |
| 6 | Khan Academy — https://www.khanacademy.org | Systematic learning: math, science, economics | WebSearch with `allowed_domains: ["khanacademy.org"]` | Some pages render with JavaScript; link the page if content cannot be read |
| 7 | Project Gutenberg — https://www.gutenberg.org | Free public-domain classic books | ✅ Gutendex API: WebFetch `https://gutendex.com/books/?search=<title or author>` → plain text at `https://www.gutenberg.org/ebooks/<id>.txt.utf-8` | Mostly pre-1930 works, mostly English |
| 8 | Internet Archive — https://archive.org | Old web pages (Wayback Machine), books, video, software | Wayback: WebFetch `https://archive.org/wayback/available?url=<url>`; search: `https://archive.org/advancedsearch.php?q=<query>&fl[]=identifier,title&rows=10&output=json` | Copyright status varies by item; check before recommending downloads |
| 9 | Pixabay — https://pixabay.com | Free images and video | WebSearch with `allowed_domains: ["pixabay.com"]`; give page links | Pixabay Content License: free use, no attribution needed; no selling unmodified copies; no implying endorsement |
| 10 | Pexels — https://www.pexels.com | High-quality free images and video | WebSearch with `allowed_domains: ["pexels.com"]`; give page links | Pexels License: free use, no attribution needed; no selling unmodified copies; no implying endorsement |

## Notes

- WebSearch is US-region search. For Korea-specific topics, add Korean keywords or follow up with general search.
- Use several `allowed_domains` in one search when a mode needs more than one site (e.g. policy: `["brookings.edu", "foreignaffairs.com"]`).
