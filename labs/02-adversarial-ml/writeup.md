# Lab 02 — Adversarial Machine Learning

**Platform:** TryHackMe  
**Difficulty:** Medium  
**Status:** 🔄 In Progress

---

## Room Overview

Hands-on exploration of adversarial attacks against image classifiers. This room involves crafting adversarial examples and observing their effect on a deployed neural network.

---

## Setup

```bash
# Start the AttackBox or connect via OpenVPN
# Clone the provided starter code
git clone <room-repo-url>
cd adversarial-ml-lab
pip install -r requirements.txt
```

---

## Tasks

### Task 1 — Understanding the Target Model

#### Approach
- Inspect the model architecture (ResNet-18).
- Confirm baseline accuracy on the clean test set.

#### Observations
- Model achieves ~94% accuracy on clean CIFAR-10 images.
- Output layer uses softmax; top-1 prediction is the class with the highest logit.

---

### Task 2 — Fast Gradient Sign Method (FGSM)

#### Approach
1. Forward pass: compute the loss for the true label.
2. Backward pass: compute `∇_x J(θ, x, y)`.
3. Apply perturbation: `x_adv = x + ε · sign(∇_x J)`.
4. Evaluate the adversarial example against the model.

```python
# Pseudocode
x.requires_grad = True
output = model(x)
loss = criterion(output, true_label)
loss.backward()
x_adv = x + epsilon * x.grad.sign()
x_adv = torch.clamp(x_adv, 0, 1)
```

#### Observations
- With ε = 0.03, accuracy drops from 94% → ~18%.
- Perturbations are imperceptible to the human eye.

---

### Task 3 — Challenge Flag

> 🔄 In progress — complete after lab submission.

**Flag:** `FLAG{REDACTED}`

---

## Key Takeaways

1. FGSM is computationally cheap but highly effective.
2. Small ε keeps perturbations visually imperceptible.
3. Adversarial robustness and standard accuracy often trade off against each other.
