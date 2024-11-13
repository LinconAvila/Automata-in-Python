# AutomatonL2

## Description

**AutomatonL2** is a deterministic finite automaton (DFA) that recognizes words ending with the symbol "a". This automaton is part of a collection implemented in Python, showcasing how DFAs can be used to identify patterns at specific positions in strings.

---

## Structure and Functioning

**AutomatonL2**  has two states:

- **q0**: Initial state and non-accepting state, representing words that either have not ended with "a" or have ended with "b".
- **q1**: Accepting state, representing words that end with "a".

The automaton processes each symbol in the input string, following the transition function defined below, and determines whether the string ends in an acceptance state.

### Transition Function (δ)

| Current State | Input Symbol | Next State |
|---------------|--------------|------------|
| q0            | a            | q1         |
| q0            | b            | q0         |
| q1            | a            | q1         |
| q1            | b            | q0         |

### Formal Definitions

- **Set of States (Q)**: {q0, q1}
- **Alphabet (Σ)**: {a, b}
- **Initial State**: q0
- **Acceptance State (F)**: {q1}

---

## Accepted Language

The language **L** recognized by **AutomatonL1** is defined as:

- **L = { w ∈ {a, b} | w ends with "a" }**

This means that L consists of all strings over the alphabet {a, b} that conclude with the symbol "a".

---

## Example of Operation

- **Input**: `"aba"`
  - **States Visited**: q0 → q0 → q1 → q1
  - **Result**: Accepted

- **Input**: `"bbaa"`
  - **States Visited**: q0 → q0 → q0 → q1
  - **Result**: Accepted

- **Input**: `"abb""`
  - **States Visited**: q0 → q0 → q1 → q0
  - **Result**: Rejected (does not end in acceptance state q1)

---

## Code

The code for this automaton is located in `src/automatonL2.py` and implements the transition function and acceptance logic for the specified language.

---

## Usage Example

To test the automaton with an input word, run:

```python
from src.automatonL2 import AutomatonL2

dfa = AutomatonL2()
print(dfa.accepts("aba"))  # True
print(dfa.accepts("abb"))  # False
