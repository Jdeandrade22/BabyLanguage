# Baby Language

A simple mathematical expression tokenizer written in Python. This project demonstrates basic lexical analysis by breaking down mathematical expressions into their component tokens.

## Features

- Tokenizes mathematical expressions
- Supports basic operators: +, -, *, /
- Handles parentheses
- Processes multi-digit numbers

## Usage

```python
from func import tokenize

expression = "((12+3*5)+5/4)"
tokens = tokenize(expression)
print(tokens)
```

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
```bash
https://github.com/Jdeandrade22/BabyLanguage.git
cd BabyLanguage
```

2. Run the example:
```bash
python main.py
``` 
