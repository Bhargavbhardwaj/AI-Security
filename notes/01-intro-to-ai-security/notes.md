# Module 01 — Introduction to AI Security

## Summary

This module introduces the fundamental concepts of Artificial Intelligence and Machine Learning from a security perspective. It covers what makes AI systems different from traditional software and why they present unique attack surfaces.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Machine Learning (ML)** | Systems that learn patterns from data instead of following explicit rules |
| **Neural Networks** | Layered mathematical models loosely inspired by the human brain |
| **Training Data** | The dataset used to teach a model its task |
| **Inference** | Running a trained model on new, unseen data |
| **Attack Surface** | The sum of entry points an attacker can exploit |

---

## Why AI Systems Are Different

1. **Non-determinism** — small input changes can cause unpredictable outputs.
2. **Data dependency** — model behaviour is directly shaped by its training data.
3. **Black-box nature** — internal decision logic is often opaque.
4. **Continuous deployment** — models are frequently retrained, widening the CI/CD attack surface.

---

## Common AI Security Threats

| Threat | Description |
|--------|-------------|
| **Adversarial Examples** | Inputs crafted to fool the model at inference time |
| **Data Poisoning** | Corrupting training data to manipulate model behaviour |
| **Model Theft** | Reconstructing a model via query access |
| **Prompt Injection** | Hijacking LLM instruction context through user input |
| **Backdoor Attacks** | Embedding hidden triggers during training |

---

## AI Security Lifecycle

```
[Data Collection] → [Model Training] → [Model Deployment] → [Inference / API]
       ↑                   ↑                   ↑                    ↑
  Data Poisoning    Backdoor Attack      Supply Chain           Adversarial
                                         Compromise              Examples
```

---

## Defences / Mitigations

- Validate and sanitise training data sources.
- Perform threat modelling specific to ML pipelines.
- Apply input validation at inference endpoints.
- Monitor model outputs for distribution drift.
- Follow MITRE ATLAS and NIST AI RMF guidelines.

---

## References

- [MITRE ATLAS](https://atlas.mitre.org/)
- [NIST AI Risk Management Framework](https://www.nist.gov/system/files/documents/2023/01/26/NIST.AI.100-1.pdf)
- [Google SAIF](https://saif.google/)
