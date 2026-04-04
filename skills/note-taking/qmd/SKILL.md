---
name: qmd
description: Query Markdown Database - Fast full-text, vector similarity, and hybrid search for documentation. Use when searching the doc-hub, finding notes, or querying indexed markdown content.
homepage: https://github.com/tobi/qmd
prerequisites:
  commands: [qmd]
metadata:
  hermes:
    tags: [search, markdown, documentation, vector, note-taking]
---

# QMD - Query Markdown Database

Mini CLI search engine for docs, knowledge bases, and meeting notes with local AI capabilities.

## Setup

- **Installation**: `bun install -g qmd`
- **Initialize**: `qmd collection add /path/to/docs --name doc-hub`
- **Embed**: `qmd embed` (Downloads models automatically)

## Common Commands

- **Hybrid Search (Best)**: `qmd query "search term" -c doc-hub`
- **Full Text Search**: `qmd search "keyword" -c doc-hub`
- **Vector Search**: `qmd vsearch "semantic concept" -c doc-hub`
- **Get Document**: `qmd get "doc-hub/file.md"`
- **List Files**: `qmd ls doc-hub`

## Advanced Usage

- **Context Integration**: `qmd context add qmd://doc-hub "Technical documentation"`
- **JSON Output**: `qmd query "term" --json`
- **Markdown Output**: `qmd search "term" --md --full`
- **File List**: `qmd search "term" --files` (for file list with scores)

## Management

- **Status**: `qmd status`
- **Update Index**: `qmd update` (Re-index)
- **Git Pull & Update**: `qmd update --pull`
- **Collections**: `qmd collection list` / `add <path> --name <name>` / `remove <name>`

## MCP Server

- **Start**: `qmd mcp`
- Configure in agent as MCP server.

## Notes

- **Models**: Auto-downloads EmbeddingGemma (embeddings) and Qwen (reranking/generation).
- **Index path**: `~/.cache/qmd/index.sqlite`
- **Performance**: Use `--min-score` to filter relevance.
