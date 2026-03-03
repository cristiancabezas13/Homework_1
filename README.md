# Homework 1 – Failure Function (Dragon Book Fig. 3.19)

**Course:** Formal Languages and Compilers  
**Students:** Cristian David Cabezas Jimenez, Isabela Valencia Pino

This program implements the algorithm from *Compilers: Principles, Techniques, and Tools (2nd Edition)* (Dragon Book), **Figure 3.19**, to compute the **failure function** for a given keyword (pattern).

---

## What the failure function does
Given a keyword `b1 b2 ... bn`, the failure function `f(s)` (for `s = 1..n`) stores the length of the **longest proper prefix** of `b1..bs` that is also a **suffix** of `b1..bs`.  
Intuitively, it tells us how far we can “fall back” after a mismatch without restarting the comparison from scratch.

---

## What it is used for
The failure function is used in efficient pattern matching (e.g., KMP-like behavior). When a mismatch happens, instead of restarting from the beginning of the pattern, we jump to a smaller valid prefix indicated by `f(s)`. This avoids repeated work and makes the matching process efficient.

---

## Requirements
- Python 3.13

---

## Versions used
- **Operating System:** Windows 11 
- **Programming language:** Python 3.13 
- **Tools:** Visual Studio Code, PowerShell 

---

## How to run

### 1) Open a terminal in the folder that contains the file
Example (Windows PowerShell):
```powershell
cd D:\Descargas
python .\failure_function_fig319.py --test
