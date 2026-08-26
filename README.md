# 🔢 KHOKHAR Square Digital Root Transformation – GUI

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An interactive graphical tool to explore the **KHOKHAR Square Digital Root Transformation** – a beautiful iterative process on 4‑digit numbers that eventually reaches a fixed point.

![GUI Demo](https://via.placeholder.com/800x500?text=Screenshot+Placeholder)  
*(Replace with an actual screenshot)*

---

## ✨ What is the KHOKHAR Transformation?

Given a 4‑digit number **n = d₁d₂d₃d₄**, the transformation **T(n)** is defined in four steps:

1. **Place the digits** on the four vertices of a square in cyclic order.
2. **For each edge**, compute the **digital root** of the sum of its two endpoint digits:  
   `sᵢ = dr(dᵢ + dᵢ₊₁)` (indices modulo 4).  
   *(Digital root: dr(x) = 1 + (x‑1) mod 9 for x>0, dr(0)=0)*
3. **Form two 4‑digit strings** from the multiset {s₁, s₂, s₃, s₄}:  
   - `D = desc(s₁, s₂, s₃, s₄)` – digits in non‑increasing order.  
   - `A = asc(s₁, s₂, s₃, s₄)` – digits in non‑decreasing order.
4. **The transformation** is:  
   `T(n) = D − A`  (written as a 4‑digit string with leading zeros).

Repeated application of **T** eventually reaches a **fixed point** (e.g., `7443` is a fixed point). This process was introduced by **Muhammad S. Khokhar** in his exploration of digital root dynamics.

---

## 🖥️ GUI Features

- **Step‑by‑step execution** – Click “Next Step” to advance one iteration at a time.
- **Auto‑run mode** – Watch the entire orbit unfold automatically (600 ms per step).
- **Visual square diagram** – Digits, edge sums, and digital roots are displayed on an interactive canvas.
- **Edge analysis panel** – Shows every edge sum and its digital root for the current number.
- **Transformation details** – Displays `D`, `A`, and the computed `T(n)`.
- **Orbit history** – Keeps a scrollable log of all steps, showing the full path to the fixed point.
- **Fixed‑point detection** – Highlights when a fixed point is reached and disables further steps.
- **Integrated help** – The “Help” button opens a pop‑up with the complete formula and a worked example (`1234 → 3996 → ... → 7443`).

---

## 🚀 Installation & Usage

### Prerequisites
- **Python 3.8** or higher.
- **Tkinter** – included with standard Python installations on Windows, macOS, and most Linux distributions.  
  (If missing, install via your package manager, e.g., `sudo apt-get install python3-tk` on Debian/Ubuntu.)


Equivalently, it is the single‑digit value obtained by repeatedly summing the digits until only one digit remains.

---

## ✨ Example: Orbit of 1234 (with table)

Starting from `1234`, the transformation iterates as follows:

| Step | Number | Edge sums (raw) | Digital roots (s₁,s₂,s₃,s₄) | D (desc) | A (asc) | T(n) = D‑A |
|------|--------|----------------|-----------------------------|----------|---------|------------|
| 0    | 1234   | 3,5,7,5        | 3,5,7,5                     | 7553     | 3557    | 3996       |
| 1    | 3996   | 12,18,15,9     | 3,9,6,9                     | 9963     | 3699    | 6264       |
| 2    | 6264   | 8,8,10,10      | 8,8,1,1                     | 8811     | 1188    | 7623       |
| 3    | 7623   | 13,8,5,10      | 4,8,5,1                     | 8541     | 1458    | 7083       |
| 4    | 7083   | 7,8,11,10      | 7,8,2,1                     | 8721     | 1278    | 7443       |
| 5    | 7443   | 11,8,7,10      | 2,8,7,1                     | 8721     | 1278    | 7443       |

After step 5, we obtain `7443`. Applying the transformation again gives the same number, so `7443` is a **fixed point**.  
This fixed point is sometimes called the **“black hole”** of the transformation, because every starting number eventually falls into it (for the standard 4‑digit case).

> **The black‑hole number is `7443`.**  
> It is the unique attractor for all 4‑digit numbers under this transformation (excluding trivial cases that lead to 0000).

---

## 🖥️ GUI Features

- **Step‑by‑step execution** – Click “Next Step” to advance one iteration at a time.
- **Auto‑run mode** – Watch the entire orbit unfold automatically (600 ms per step).
- **Visual square diagram** – Digits, edge sums, and digital roots are displayed on an interactive canvas.
- **Edge analysis panel** – Shows every edge sum and its digital root for the current number.
- **Transformation details** – Displays `D`, `A`, and the computed `T(n)`.
- **Orbit history** – Keeps a scrollable log of all steps, showing the full path to the fixed point.
- **Fixed‑point detection** – Highlights when a fixed point is reached and disables further steps.
- **Integrated help** – The “Help” button opens a pop‑up with the complete formula and a worked example (the table above).

---

## 🚀 Installation & Usage

### Prerequisites
- **Python 3.8** or higher.
- **Tkinter** – included with standard Python installations on Windows, macOS, and most Linux distributions.  
  (If missing, install via your package manager, e.g., `sudo apt-get install python3-tk` on Debian/Ubuntu.)

### Clone the repository
```bash
