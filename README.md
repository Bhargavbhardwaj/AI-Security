# 🛡️ AI Security — TryHackMe Learning Path

![TryHackMe](https://img.shields.io/badge/Platform-TryHackMe-red?style=flat-square&logo=tryhackme)
![Topic](https://img.shields.io/badge/Topic-AI%20Security-blueviolet?style=flat-square)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

> A structured repository documenting progress through the **TryHackMe AI Security** learning path — covering the theory, hands-on labs, and tooling involved in securing AI/ML systems.

---

## 📚 Table of Contents

- [About](#-about)
- [Learning Path Overview](#-learning-path-overview)
- [Repository Structure](#-repository-structure)
- [Progress Tracker](#-progress-tracker)
- [Getting Started](#-getting-started)
- [Key Concepts](#-key-concepts)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📖 About

This repository is a personal knowledge base built while completing the [TryHackMe AI Security](https://tryhackme.com) learning path.  
Each module includes:

- 📝 **Notes** — theory summaries and concept explanations
- 🧪 **Labs** — step-by-step writeups with flags and observations
- 🔧 **Scripts** — reusable tools and proof-of-concept code

---

## 🗺️ Learning Path Overview

| # | Module | Topic | Status |
|---|--------|-------|--------|
| 01 | Introduction to AI Security | Fundamentals of AI/ML and attack surface | ✅ Complete |
| 02 | Adversarial Machine Learning | Evasion, poisoning, and model robustness | 🔄 In Progress |
| 03 | Prompt Injection | LLM attack vectors and mitigations | 🔄 In Progress |
| 04 | Data Poisoning | Corrupting training data and defences | ⬜ Pending |
| 05 | Model Theft & Extraction | Stealing model functionality via APIs | ⬜ Pending |
| 06 | Secure AI Development | SDLC best practices for AI systems | ⬜ Pending |

---

## 📁 Repository Structure

```
AI-Security/
├── README.md                  # This file
├── .gitignore
│
├── notes/                     # Theory notes per module
│   ├── README.md
│   ├── 01-intro-to-ai-security/
│   ├── 02-adversarial-ml/
│   ├── 03-prompt-injection/
│   ├── 04-data-poisoning/
│   ├── 05-model-theft/
│   └── 06-secure-ai-development/
│
├── labs/                      # Lab writeups per room
│   ├── README.md
│   ├── 01-intro-to-ai-security/
│   ├── 02-adversarial-ml/
│   └── 03-prompt-injection/
│
├── scripts/                   # Utility and PoC scripts
│   ├── README.md
│   ├── adversarial_example_generator.py
│   └── prompt_injection_tester.py
│
└── resources/                 # Curated external references
    └── README.md
```

---

## ✅ Progress Tracker

```
Overall Progress: ██░░░░░░░░  20%

01 - Intro to AI Security       [██████████] 100%
02 - Adversarial ML             [█████░░░░░]  50%
03 - Prompt Injection           [███░░░░░░░]  30%
04 - Data Poisoning             [░░░░░░░░░░]   0%
05 - Model Theft & Extraction   [░░░░░░░░░░]   0%
06 - Secure AI Development      [░░░░░░░░░░]   0%
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- A free [TryHackMe](https://tryhackme.com) account
- Basic understanding of machine learning concepts

### Clone the repository

```bash
git clone https://github.com/Bhargavbhardwaj/AI-Security.git
cd AI-Security
```

### Install script dependencies

```bash
pip install -r scripts/requirements.txt
```

---

## 🔑 Key Concepts

| Concept | Brief Description |
|---------|------------------|
| **Adversarial Examples** | Inputs crafted to fool ML models into mis-classification |
| **Prompt Injection** | Manipulating LLM prompts to bypass safety controls |
| **Data Poisoning** | Injecting malicious data into the training pipeline |
| **Model Extraction** | Reconstructing a model via repeated API queries |
| **Evasion Attacks** | Bypassing deployed classifiers at inference time |
| **Backdoor Attacks** | Embedding hidden triggers into a model during training |

---

## 🤝 Contributing

This is a personal learning repository, but suggestions and corrections are welcome!  
Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

*Happy Hacking! 🔒*

