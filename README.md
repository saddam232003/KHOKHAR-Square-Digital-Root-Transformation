# KHOKHAR-Square-Digital-Root-Transformation
The KHOKHAR Square Digital Root Transformation: 7443 A Fixed-Point Analysis of a 4-Digit Graph-Based Iterative Map
# 🔢 KHOKHAR Square Digital Root Transformation – GUI

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An interactive graphical tool to explore the **KHOKHAR Square Digital Root Transformation** – a beautiful iterative process on 4‑digit numbers that eventually reaches a fixed point.

 
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

### Clone the repository
```bash
git clone (https://github.com/saddam232003/KHOKHAR-Square-Digital-Root-Transformation/blob/main/README.md)
cd KHOKHAR-Square-DRT-GUI
