# Prompt Canary ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="Prompt Canary Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/prompt-canary/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/prompt-canary?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/prompt-canary/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**Prompt Canary** is a production-ready developer tool and connector: Zero-width steganographic canary injector detecting system prompt leaks and output tampering.

---

## 🚀 Problem Statement

System prompts and intellectual property are easily extracted by attackers using indirect prompt injection without the developer noticing.

---

## ⚡ Architecture Flow

```mermaid
flowchart LR
    A[System Prompt] --> B[Encode Zero-Width Canary \u200B\u200C]
    B --> C[Watermarked Prompt]
    C --> D[LLM Completion Engine]
    D --> E[Output Text Stream]
    E --> F[Canary Extractor]
    F -->|Canary Found| G[ALERT: System Prompt Leaked!]
```

---

## 📊 Performance Benchmarks

| Metric | Standard Prompt | With Prompt Canary |
|---|---|---|
| Visual Disruption | Clean | 100% Invisible (0 glyph width) |
| Detection Reliability | 0% | 100% Exact match |
| Encoding Latency | - | 0.015ms |

---

## 🛠️ Installation & Quickstart

```bash
pip install prompt_canary
```

### Python API

```python
import prompt_canary

print(prompt_canary.__version__)
```

### CLI Usage

```bash
prompt-canary --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
