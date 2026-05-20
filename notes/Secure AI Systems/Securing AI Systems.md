# Securing AI Systems - TryHackMe Notes

## Overview

This room focuses on the security challenges introduced by modern AI-powered applications.  
Using the fictional AI assistant **TryAssist**, the room explains how integrating Large Language Models (LLMs) into production systems creates entirely new attack surfaces beyond traditional web security.

The key idea is that AI systems are not just models — they are complete ecosystems involving prompts, APIs, plugins, storage systems, logs, and external integrations.

---

# Why AI Systems Create New Risks

Traditional applications usually expose:

- Web applications
- APIs
- Databases
- Authentication systems

AI systems add additional components such as:

- Natural language interfaces
- Prompt handling
- Context retrieval systems
- External tool integrations
- Vector databases
- Conversation logging
- Autonomous actions

Even if the AI behaves exactly as intended, sensitive information can still leak due to poor architectural security decisions.

Example:
Samsung engineers accidentally leaked proprietary source code by pasting it into ChatGPT.

---

# Anatomy of an AI System

A production AI system typically contains:

## 1. User Interface
The frontend where users interact with the AI.

## 2. Application Layer
Handles authentication, business logic, and communication with the model.

## 3. LLM (Large Language Model)
Processes prompts and generates responses.

## 4. Retrieval Systems
Fetches contextual information from documents, databases, or vector stores.

## 5. External Tools & APIs
Allows the AI to interact with repositories, CI/CD pipelines, or other services.

## 6. Logging & Monitoring
Stores conversations, prompts, outputs, and system activity.

---

# AI Attack Surface

AI systems introduce several new attack vectors:

| Attack Surface | Risk |
|---|---|
| Prompts | Prompt injection attacks |
| Training/Context Data | Sensitive data exposure |
| Plugins & APIs | Excessive permissions |
| Logs & Conversations | Credential leakage |
| Model Outputs | Unsafe or malicious responses |
| Autonomous Actions | Abuse of system privileges |

---

# Important Security Frameworks

## OWASP LLM Top 10 (2025)

The primary framework for identifying LLM-related risks.

Examples include:

- Prompt Injection
- Sensitive Information Disclosure
- Excessive Agency
- Insecure Output Handling
- Supply Chain Vulnerabilities

## MITRE ATLAS

A knowledge base for adversarial threats targeting AI systems.

Focuses on:

- AI attack techniques
- Adversarial behaviors
- Real-world AI threat modeling

---

# System-Level Threats

## 1. Improper Output Handling

LLM outputs are trusted without validation.

### Risk:
- Command injection
- Unsafe code execution
- XSS or malicious content delivery

### Defence:
- Output sanitisation
- Validation layers
- Sandboxing

---

## 2. Excessive Agency

The AI has too many permissions or autonomous capabilities.

### Risk:
- Deleting data
- Triggering pipelines
- Accessing sensitive systems

### Defence:
- Least privilege
- Human approval workflows
- Scoped permissions

---

## 3. System Prompt Leakage

Attackers extract hidden prompts or internal instructions.

### Risk:
- Exposure of internal logic
- Security bypasses
- Information disclosure

### Defence:
- Prompt hardening
- Segregation of secrets
- Monitoring prompt manipulation attempts

---

## 4. Unbounded Consumption

Attackers abuse the AI system to exhaust resources.

### Risk:
- High operational costs
- Denial of service
- API abuse

### Defence:
- Rate limiting
- Token quotas
- Usage monitoring

---

## 5. Sensitive Information Disclosure

Confidential data is exposed through prompts, logs, or responses.

### Risk:
- Credential leaks
- Internal documentation exposure
- Source code disclosure

### Defence:
- Data classification
- Redaction
- Secure logging practices

---

# Secure Design Patterns

## Defence in Depth
Use multiple security layers instead of relying on one control.

## Least Privilege
Grant only the minimum permissions necessary.

## Monitoring & Logging
Continuously monitor prompts, outputs, and API usage.

## Human-in-the-Loop
Require manual approval for sensitive actions.

## Input & Output Validation
Treat both prompts and model responses as untrusted data.

---

# Key Takeaways

- AI systems dramatically expand the attack surface.
- Security must cover the entire AI ecosystem, not just the model.
- Prompt injection is the AI equivalent of traditional injection attacks.
- Sensitive data leakage can happen without vulnerabilities.
- Proper architecture and defensive design are critical before deployment.

---

# Conclusion

Securing AI systems requires combining traditional cybersecurity principles with new AI-specific threat models.  
Frameworks like **OWASP LLM Top 10** and **MITRE ATLAS** help security teams understand and defend modern AI infrastructures against evolving threats.
