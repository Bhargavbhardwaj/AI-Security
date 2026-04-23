# 🔧 Scripts

Reusable utility scripts and proof-of-concept tools developed during the AI Security learning path.

## Contents

| Script | Description |
|--------|-------------|
| [`adversarial_example_generator.py`](./adversarial_example_generator.py) | Generates adversarial examples using the FGSM attack |
| [`prompt_injection_tester.py`](./prompt_injection_tester.py) | Tests LLM endpoints for common prompt injection payloads |

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Each script includes a `--help` flag:

```bash
python adversarial_example_generator.py --help
python prompt_injection_tester.py --help
```

## ⚠️ Disclaimer

These scripts are provided **for educational purposes only**.  
Only use them on systems you own or have explicit permission to test.
