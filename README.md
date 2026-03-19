# 🔧 wrench

> Point it at your code. Get back what's slow and how to fix it.

Wrench is a multi-language performance analyser that combines static analysis with AI-powered explanations. It finds real performance issues in your code — nested loops, inefficient patterns, bad practices — then explains exactly why they're a problem and shows you the fix.

No cloud, no setup hell, no enterprise pricing. Just run it on a file.

---

## What it catches

**High priority**
- Nested loops (O(n²) and worse)
- Expensive function calls inside loops
- Repeated attribute access that should be cached
- String concatenation with `+` in loops

**Medium priority**
- List appends inside nested loops
- Unnecessary `list(range(n))` creation
- Bare `except:` and overly broad `except Exception`
- Global variable access inside loops
- Mutable default arguments

---

## Supported languages

| Language | Extension |
|----------|-----------|
| Python | `.py` |
| JavaScript | `.js` |
| TypeScript | `.ts` |
| Go | `.go` |
| C | `.c` |
| C++ | `.cpp`, `.cc` |

---

## Installation

```bash
git clone https://github.com/yourusername/wrench.git
cd wrench
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_key_here
```

Get a free Groq API key at [console.groq.com](https://console.groq.com) 

---

## Usage

```bash
python main.py yourfile.py
python main.py app.js
python main.py main.go
python main.py server.cpp
```

That's it. Wrench detects the language from the file extension automatically.

### Example output

```
Nested loop at line 19 — potential O(n²)
String concatenation at line 22 — use ''.join() instead
Function call 'expensive_function' inside loop at line 25 — consider moving it out
Bare except at line 40 — catches everything including system exceptions, be specific

--- AI Analysis ---

1. Nested loop at line 19
   Problem: Two nested loops over the same data gives you O(n²) time complexity.
   For 1000 items that's 1,000,000 iterations instead of 1,000.

   Fix:
   # before
   for i in items:
       for j in items:
           process(i, j)

   # after — use itertools or restructure with a dict lookup
   lookup = {item: process(item) for item in items}
```

---

## How it works

```
your file
    ↓
Tree-sitter parses it into a syntax tree
    ↓
IR translator converts to language-agnostic representation
    ↓
Detectors run static analysis on the IR
    ↓
Findings sent to Groq (Llama 3.3 70B)
    ↓
Plain English explanation + fix
```

The static analysis layer is deterministic — it either finds a nested loop or it doesn't. No hallucination. The AI layer explains what the detectors already confirmed exists.

---

## Roadmap

- [x] Static analysis (Python, JS, TS, Go, C, C++)
- [x] AI-powered explanations and fixes
- [x] Multi-language IR architecture
- [ ] Runtime profiling (Layer 3)
- [ ] More detectors
- [ ] `pip install wrench` support
- [ ] Web UI

---

## Project structure

```
wrench/
├── detectors/
│   ├── base.py         ← depth tracking, core visitor
│   ├── high.py         ← high priority detectors
│   └── medium.py       ← medium priority detectors
├── languages/
│   ├── python_rules.py ← Tree-sitter node mappings per language
│   ├── js_rules.py
│   └── ...
├── ir.py               ← language-agnostic IR node
├── ir_translator.py    ← Tree-sitter → IR translation
├── parser_engine.py    ← language detection + parser setup
├── ai_engine.py        ← Groq integration
└── main.py             ← entry point
```

---

## Contributing

Pull requests welcome. If you want to add a new language, add a rules file in `languages/` mapping Tree-sitter node types to the generic IR types. That's it — the detectors work on all languages automatically.

Open an issue first for anything major.

---

Built by [@vishaddjain]