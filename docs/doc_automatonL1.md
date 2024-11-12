# AutomatonL1

## Description

**AutomatonL1** is a deterministic finite automaton (DFA) that recognizes words containing at least four occurrences of the symbol **"a"**. This automaton is part of a collection implemented in Python, illustrating the recognition of specific patterns within character strings.

---

## Structure and Functioning

**AutomatonL1** consists of five states, representing the count of occurrences of the symbol "a":

- **q0**: Initial state, no occurrence of "a".
- **q1**: One occurrence of "a".
- **q2**: Two occurrences of "a".
- **q3**: Three occurrences of "a".
- **q4**: Four or more occurrences of "a" (acceptance state).

Transitions between states are governed by the transition function described in the table below, where the automaton remains in an acceptance state (q4) whenever four or more occurrences of "a" are recorded.

### Transition Function (δ)

| Current State | Input Symbol | Next State |
|---------------|--------------|------------|
| q0            | a            | q1         |
| q0            | b            | q0         |
| q1            | a            | q2         |
| q1            | b            | q1         |
| q2            | a            | q3         |
| q2            | b            | q2         |
| q3            | a            | q4         |
| q3            | b            | q3         |
| q4            | a            | q4         |
| q4            | b            | q4         |

### Formal Definitions

- **Set of States (Q)**: {q0, q1, q2, q3, q4}
- **Alphabet (Σ)**: {a, b}
- **Initial State**: q0
- **Acceptance State (F)**: {q4}

---

## Accepted Language

The language **L** recognized by **AutomatonL1** is defined as:

- **L = { w ∈ {a, b}* | w contains "aaaa" as a subsequence }**

In other words, **L** is the set of words over the alphabet {a, b} that contain at least four occurrences of the symbol "a" at some point in the sequence.

---

## Example of Operation

- **Input**: `"aaaa"`
  - **States Visited**: q0 → q1 → q2 → q3 → q4
  - **Result**: Accepted

- **Input**: `"bbaaabaaa"`
  - **States Visited**: q0 → q0 → q1 → q2 → q3 → q4
  - **Result**: Accepted

- **Input**: `"abbba"`
  - **States Visited**: q0 → q1 → q1 → q1 → q1
  - **Result**: Rejected (does not reach acceptance state `q4`)

---

## Code

The code for this automaton is located in `src/automatonL1.py` and implements the transition function and acceptance logic for the specified language.

---

## Usage Example

To test the automaton with an input word, run:

```python
from src.automatonL1 import AutomatonL1

dfa = AutomatonL1()
print(dfa.accepts("aaaa"))  # True
print(dfa.accepts("abbba"))  # False
