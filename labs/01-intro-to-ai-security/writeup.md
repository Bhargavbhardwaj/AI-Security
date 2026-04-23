# Lab 01 — Introduction to AI Security

**Platform:** TryHackMe  
**Difficulty:** Easy  
**Status:** ✅ Complete

---

## Room Overview

This introductory room walks through the fundamental concepts of AI Security, exploring what makes AI/ML systems uniquely vulnerable and how those vulnerabilities differ from traditional software security.

---

## Setup

No special tooling required for this room.  
All tasks are theory-based or interactive in-browser.

---

## Tasks

### Task 1 — What is AI Security?

#### Approach
Read through the introductory material covering:
- Differences between AI and traditional software
- Why AI systems introduce novel attack vectors
- The CIA triad applied to AI systems

#### Key Takeaways
- AI models are statistical — small, crafted input changes can cause large behavioural changes.
- Data integrity is critical: the model is only as trustworthy as its training data.
- Confidentiality concerns include model inversion and membership inference.

---

### Task 2 — The AI Attack Surface

#### Approach
Identify and categorise the stages of the ML pipeline where attacks can occur.

#### Stages
| Stage | Attack |
|-------|--------|
| Data collection | Poisoning |
| Training | Backdoor injection |
| Deployment | Supply chain compromise |
| Inference | Adversarial examples, prompt injection |

---

### Task 3 — Quiz / Challenge

**Flag:** `FLAG{REDACTED}`

---

## Key Takeaways

1. AI security is a superset of traditional security — classic vulnerabilities still apply.
2. The non-deterministic nature of ML models makes testing harder.
3. MITRE ATLAS is the go-to threat matrix for adversarial ML.
