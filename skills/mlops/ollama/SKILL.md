---
name: ollama
description: Local AI backend for free, private, offline inference. Use for running LLMs locally, chat, single-shot prompts, and model management.
homepage: https://ollama.com
prerequisites:
  commands: [ollama]
metadata:
  hermes:
    tags: [llm, local, inference, ollama, private]
---

# Ollama (Local AI Backend)

Free, private, offline inference running as a systemd service.

## Service Management

- **Check Status**: `systemctl status ollama`
- **Start**: `sudo systemctl start ollama`
- **Stop**: `sudo systemctl stop ollama`
- **Restart**: `sudo systemctl restart ollama`
- **Enable on Boot**: `sudo systemctl enable ollama`
- **Version**: `ollama -v`

## Common Commands

- **Interactive Chat**: `ollama run qwen2.5:7b`
- **Single Shot**: `ollama run deepseek-r1:8b "Explain quantum computing"`
- **Multiline/File**: `cat file.txt | ollama run qwen2.5:7b "Summarize this"`

## Model Management

- **List Models**: `ollama list`
- **Pull Model**: `ollama pull model_name`
- **Remove Model**: `ollama rm model_name`
- **Running Models**: `ollama ps`
- **Stop Model**: `ollama stop model_name`

## Integrations

- **Launch Integration**: `ollama launch`
- **Supported**: OpenCode, Claude Code, Codex, Droid.
- **Example**: `ollama launch opencode`

## API Usage

Endpoint: `http://localhost:11434/v1` (OpenAI Compatible)

- **List Models**: `curl http://localhost:11434/v1/models`
- **Chat**: `curl http://localhost:11434/v1/chat/completions`

## Configuration

- **Models Path**: `/mnt/data/ollama/models` (set via `OLLAMA_MODELS` env)
- **Data Path**: `/mnt/data/ollama` (blobs, manifests)
- **GPU**: RTX 3070 Laptop (8GB VRAM)
- **Logs**: `journalctl -u ollama -f`

## Notes

- **Modelfile**: Custom models with `ollama create -f Modelfile`.
- **Environment**: Check with `systemctl show ollama --property=Environment`.
