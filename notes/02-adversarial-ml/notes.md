# Module 02 — Adversarial Machine Learning

## Summary

Adversarial Machine Learning studies how attackers deliberately manipulate inputs to deceive ML models, and how defenders can build more robust systems.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Adversarial Example** | A carefully perturbed input that causes a model to misclassify |
| **Perturbation Budget (ε)** | Maximum allowed change to the input |
| **White-box Attack** | Attacker has full access to model architecture and weights |
| **Black-box Attack** | Attacker can only query the model via an API |
| **Transferability** | Adversarial examples crafted for one model often fool another |

---

## Attack Taxonomy

### By Attacker Goal
- **Evasion** — cause mis-classification at inference time
- **Poisoning** — corrupt model behaviour via training data
- **Extraction** — steal model functionality

### By Attacker Knowledge
- White-box (full access)
- Grey-box (partial access)
- Black-box (query-only)

---

## Common Attacks

### Fast Gradient Sign Method (FGSM)
```
x_adv = x + ε · sign(∇_x J(θ, x, y))
```
- Single-step gradient attack.
- Very fast; baseline for more powerful methods.

### Projected Gradient Descent (PGD)
- Multi-step variant of FGSM.
- Considers the strongest first-order adversary.

### Carlini & Wagner (C&W)
- Optimisation-based attack.
- Produces smaller perturbations than FGSM.

### DeepFool
- Finds the minimum perturbation to cross a decision boundary.

---

## Defences / Mitigations

| Defence | Description |
|---------|-------------|
| **Adversarial Training** | Include adversarial examples in the training set |
| **Input Preprocessing** | Denoising, feature squeezing, JPEG compression |
| **Certified Defences** | Provide provable robustness guarantees (e.g., randomised smoothing) |
| **Ensemble Methods** | Use multiple diverse models to reduce transferability |
| **Detection** | Identify adversarial inputs before they reach the model |

---

## References

- [Goodfellow et al. — FGSM (2015)](https://arxiv.org/abs/1412.6572)
- [Madry et al. — PGD (2018)](https://arxiv.org/abs/1706.06083)
- [Carlini & Wagner (2017)](https://arxiv.org/abs/1608.04644)
- [IBM ART Library](https://github.com/Trusted-AI/adversarial-robustness-toolbox)
