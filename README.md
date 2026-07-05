# Elm Offer Agent
A practical AI tool for validating PC offers with structured analysis.
Elm is a modular AI prompt system designed to validate and review desktop PC offers.

It analyzes a customer request and an offer, checks for compatibility issues, and provides structured feedback, suggestions, and (optionally) a customer-ready email.
👉 Live tool: https://https://minigiovanni.github.io/elm-offer-agent/

---

## 🚀 What it does

Elm helps you:

- Detect hardware compatibility issues  
- Identify missing or incorrect components  
- Match configurations with customer needs  
- Provide a structured analysis  
- Generate a customer-friendly email (Full version)  

---

## 🧩 Versions

Elm is available in three variants:

| Version | Use case | Description |
|--------|--------|-------------|
| **Light (default)** | Daily use | Fast analysis, errors and scores |
| **Full** | Advanced | Deep analysis + suggestions + email |
| **Quick** | Fast check | Minimal output, compatibility + score only |

---

## ⚙️ How to use

### Recommended (agent-based)

1. Open your LLM (ChatGPT, Copilot, Gemini, etc.)
2. Create a new custom agent / GPT
3. Copy a build from the `builds` folder
4. Paste it as system prompt
5. Use the agent for all your requests

### Quick usage

1. Copy a build
2. Paste it in a new chat
3. Send your input in a second message

Example format:

KLANTVRAAG:
...

OFFERTE:
...

---

## 🏗️ Project structure

- `modules/` → prompt logic split into components  
- `builds/` → compiled prompts (output)  
- `scripts/` → build pipeline  
- `docs/` → website (GitHub Pages)  
- `tests/` → test cases and validation  

---

## 🔨 Build system

Elm is modular and compiled into final prompt files.

Run:

python scripts/build.py

Output:

- builds/elm-full.txt  
- builds/elm-simple.txt  
- builds/elm-score.txt  

Each build:
- combines modules  
- injects version automatically  
- enforces output structure  

---

## 📦 Versioning

Versioning is managed in:

scripts/build.py

Format:

vX.Y.Z + suffix

Examples:

- v0.4.1f → Full  
- v0.4.1l → Light  
- v0.4.1q → Quick  

Versions are automatically included in:
- build output  
- prompt content  
- website display  

---

## 🧪 Testing

Test cases are stored in:

tests/

They validate:
- detection of errors  
- compatibility checks  
- debug codes  

---

## ⚠️ Disclaimer

Elm is a support tool.

You remain fully responsible for:
- correctness of the offer  
- final configuration decisions  

Do not input sensitive or personal data into LLMs.

---

## 🧠 Design principles

- Modular prompt architecture  
- Strict output structure  
- Cross-LLM compatibility  
- Testable behavior  
- Maintainable and extendable  

---

## 💬 Feedback

Feedback is highly appreciated — this project is actively evolving.