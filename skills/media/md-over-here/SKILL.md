---
name: md-over-here
description: Web to markdown converter CLI that fetches web pages and converts them to clean markdown optimized for AI/LLM input. Use for extracting article text, scraping web content, and converting pages to markdown for analysis.
homepage: https://github.com/EstebanForge/md-over-here
prerequisites:
  commands: [md-over-here]
metadata:
  hermes:
    tags: [web, scraping, markdown, fetch, html]
---

# md-over-here (Web to Markdown)

Fetches web pages and converts them to clean markdown using Mozilla's Readability algorithm. Optimized for feeding into AI agents.

## Common Commands

- **Fetch URL**: `md-over-here https://example.com/article`
- **Shorthand**: `mdoh https://example.com/article`
- **Save to File**: `mdoh --save article.md https://example.com`
- **Multiple URLs**: `mdoh https://site.com/a https://site.com/b`
- **Combine**: `mdoh --save research.md https://site.com/a https://site.com/b`

## Advanced Usage

- **Bypass Cache**: `mdoh --no-cache https://example.com`
- **Custom Timeout**: `mdoh --timeout 60s https://slow.com`
- **User Agent**: `mdoh --user-agent "MyBot/1.0" https://example.com`
- **Verbose**: `mdoh -v https://example.com`

## Cache Management

Cache is stored at `~/.config/md-over-here/cache` with 24h TTL.

- **Stats**: `mdoh cache stats`
- **Clear**: `mdoh cache clear`
- **Custom Dir**: `mdoh --cache-dir /tmp/cache https://example.com`

## Output Format

The tool provides structured output with metadata:

```markdown
# Article Title

**URL:** ... **Author:** ... **Published:** ...
**Description:** ...

---

## [Content]

<!-- Fetched: TIMESTAMP -->
```
