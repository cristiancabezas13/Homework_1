# Assignment 2 – KMP Algorithm (Dragon Book Fig. 3.20)

**Course:** Formal Languages and Compilers (SI2002 / STO270)  
**Students:** Cristian David Cabezas Jimenez, Isabela Valencia Pino  
**Deadline:** April 24, 2026

This program implements the KMP algorithm described in *Compilers: Principles, Techniques, and Tools (2nd Edition)* (Dragon Book), **Section 3.4.5**, using the pseudocode from **Figure 3.20 (page 138)**. The algorithm is used for token recognition during the lexical analysis phase of a compiler.

---

## What the KMP algorithm does
KMP checks whether a pattern (keyword) appears as a substring inside a text.  
Instead of restarting the comparison from the beginning after a mismatch, it uses the **failure function** `f(s)` to decide how far to “fall back” while keeping already matched information. This makes the search efficient.

---

## Short explanation of our implementation
- We compute the **failure function** using the same method from Assignment 1 (Dragon Book **Figure 3.19**).
- Then, we implement KMP as in **Figure 3.20**:
  - We scan the text from left to right.
  - `s` stores how many characters of the keyword have been matched so far.
  - On mismatch, we update `s` using the failure function until we can continue or `s` becomes 0.
  - If `s == n` (pattern length), we return **"yes"**; otherwise, after finishing the text we return **"no"**.

---

## Requirements
- Python 3.14

---

## Versions used
- **Operating System:** Windows 11
- **Programming language:** Python 3.14
- **Tools:** Visual Studio Code, PowerShell

---

## Files
- `kmp_fig320.py` → Implementation of KMP (Fig. 3.20) and failure function (Fig. 3.19)
- `exercise_3_4_6.md` → Written solution for Exercise 3.4.6 (page 138)

---

## How to run (step-by-step)

### 1) Open a terminal in the folder containing the script
Example (Windows PowerShell):
```powershell
cd C:\Users\crist\Downloads
- Run the program
python .\kmp_fig320.py abababaab ababaa
you have to see "yes" and after put
python .\kmp_fig320.py abababbaa ababaa
you have to see "no"
- Optional: Save outputs as evidence
python .\kmp_fig320.py abababaab ababaa > ex346_a.txt
python .\kmp_fig320.py abababbaa ababaa > ex346_b.txt
