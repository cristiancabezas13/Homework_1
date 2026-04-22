# Assignment 2 – KMP Algorithm (Dragon Book Fig. 3.20)
**Course:** Formal Languages and Compilers (SI2002 / STO270)  
**Students:** Cristian David Cabezas Jimenez, Isabela Valencia Pino  
**Deadline:** April 24, 2026

This program implements the KMP algorithm described in *Compilers: Principles, Techniques, and Tools (2nd Edition)* (Dragon Book), **Section 3.4.5**, using the pseudocode from **Figure 3.20 (page 138)**. The algorithm is used for token recognition during the lexical analysis phase of a compiler.

---

## What the KMP algorithm does (short)

KMP checks whether a keyword (pattern) appears as a substring in a text. When a mismatch occurs, it uses the **failure function** `f(s)` to fall back to the best valid prefix instead of restarting from the beginning.

---

## Implementation summary (short)

- We compute the **failure function** using Dragon Book **Figure 3.19** (same approach as Assignment 1).
- We implement KMP exactly as **Figure 3.20**:
  - Scan the text left to right.
  - `s` stores how many characters of the keyword have been matched.
  - On mismatch: update `s` using the failure function until continuing is possible.
  - If `s == n` (keyword length) → return **"yes"**, else after finishing the text → **"no"**.

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

- `kmp_fig320.py` → KMP implementation (Fig. 3.20) + failure function (Fig. 3.19)
- `README.md` → Explanation + how to run + Exercise 3.4.6 results

---

## How to run

### 1) Open a terminal in the folder containing the script

Example (Windows PowerShell):

```powershell
cd C:\Users\crist\Downloads
```

### 2) Run the program

Usage:

```powershell
python .\kmp_fig320.py <text> <keyword>
```

Example:

```powershell
python .\kmp_fig320.py abababaab ababaa
```

---

## Exercise 3.4.6 (Page 138)

**Keyword (pattern):** `ababaa`

### (a) Text = `abababaab`

Run:

```powershell
python .\kmp_fig320.py abababaab ababaa
```

Expected output:
- `yes`

### (b) Text = `abababbaa`

Run:

```powershell
python .\kmp_fig320.py abababbaa ababaa
```

Expected output:
- `no`

---

## Optional: Save outputs as evidence

```powershell
python .\kmp_fig320.py abababaab ababaa > ex346_a.txt
python .\kmp_fig320.py abababbaa ababaa > ex346_b.txt
```
