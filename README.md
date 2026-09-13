# 🔢 KHOKHAR Digital Root Transformations

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Preprint](https://img.shields.io/badge/Preprint-202608.1972-orange.svg)](https://www.preprints.org/manuscript/202608.1972)

An interactive graphical tool to explore two beautiful iterative processes on digital roots:

1. **KHOKHAR Square Digital Root Transformation** (4‑digit numbers) — reaches the fixed point **7443**.
2. **KHOKHAR Hexagon Digital Root Transformation** (6‑digit numbers) — reaches the fixed point **761733** (the Khokhar Constant) and exhibits a period‑2 cycle.

Both transformations were introduced by **Muhammad Saddam Khokhar**. Each is implemented in its **own Python file with its own GUI** — you can run either one independently.

---

## 📂 Two Separate Code Files — Two Different GUIs

| File | Transformation | Digits | Fixed Points | Cycle | GUI Style |
|------|----------------|--------|--------------|-------|-----------|
| `khokhar_square_gui.py` | Square (4 vertices) | 4 | 0000, 7443 | none | Square diagram |
| `khokhar_hexagon_gui.py` | Hexagon (6 vertices) | 6 | 000000, 761733 | 759933 ↔ 831762 | Hexagon diagram |

Each file is **fully self‑contained**. The GUI layouts differ: the square version draws a four‑vertex square; the hexagon version draws a six‑vertex hexagon with corresponding edge‑analysis panels and step panels.

---

## 📖 KHOKHAR Square Transformation (4‑digit)

Given a 4‑digit number **n = d₁d₂d₃d₄**:

1. Place the digits on the four vertices of a **square** in cyclic order.
2. For each edge, compute the **digital root** of the sum of its two endpoint digits:
   `sᵢ = dr(dᵢ + dᵢ₊₁)`, indices modulo 4.
3. Form two 4‑digit strings:
   - `D = desc(s₁, s₂, s₃, s₄)` — non‑increasing order.
   - `A = asc(s₁, s₂, s₃, s₄)` — non‑decreasing order.
4. **T(n) = D − A**, written as a 4‑digit string with leading zeros.

Repeated application reaches the fixed point **7443**.

### 🔹 Step-by-Step Example (Square): starting from `1234`

**Step 0 — n = 1234**
- Vertices: 1, 2, 3, 4
- Edge sums (raw): 1+2=3, 2+3=5, 3+4=7, 4+1=5
- Digital roots: **3, 5, 7, 5**
- Descending D = **7553**, Ascending A = **3557**
- T(1234) = 7553 − 3557 = **3996**

**Step 1 — n = 3996**
- Vertices: 3, 9, 9, 6
- Edge sums: 12, 18, 15, 9
- Digital roots: **3, 9, 6, 9**
- D = **9963**, A = **3699**
- T(3996) = 9963 − 3699 = **6264**

**Step 2 — n = 6264**
- Vertices: 6, 2, 6, 4
- Edge sums: 8, 8, 10, 10
- Digital roots: **8, 8, 1, 1**
- D = **8811**, A = **1188**
- T(6264) = 8811 − 1188 = **7623**

**Step 3 — n = 7623**
- Vertices: 7, 6, 2, 3
- Edge sums: 13, 8, 5, 10
- Digital roots: **4, 8, 5, 1**
- D = **8541**, A = **1458**
- T(7623) = 8541 − 1458 = **7083**

**Step 4 — n = 7083**
- Vertices: 7, 0, 8, 3
- Edge sums: 7, 8, 11, 10
- Digital roots: **7, 8, 2, 1**
- D = **8721**, A = **1278**
- T(7083) = 8721 − 1278 = **7443**

**Step 5 — n = 7443 (FIXED POINT)**
- Vertices: 7, 4, 4, 3
- Edge sums: 11, 8, 7, 10
- Digital roots: **2, 8, 7, 1**
- D = **8721**, A = **1278**
- T(7443) = 8721 − 1278 = **7443** ✅

**Orbit:** `1234 → 3996 → 6264 → 7623 → 7083 → 7443`

| Step | n | Edge roots | D (desc) | A (asc) | T(n) |
|------|---|------------|----------|---------|------|
| 0 | 1234 | 3,5,7,5 | 7553 | 3557 | 3996 |
| 1 | 3996 | 3,9,6,9 | 9963 | 3699 | 6264 |
| 2 | 6264 | 8,8,1,1 | 8811 | 1188 | 7623 |
| 3 | 7623 | 4,8,5,1 | 8541 | 1458 | 7083 |
| 4 | 7083 | 7,8,2,1 | 8721 | 1278 | 7443 |
| 5 | 7443 | 2,8,7,1 | 8721 | 1278 | **7443** |

---

## 📖 KHOKHAR Hexagon Transformation (6‑digit)

Given a 6‑digit number **n = d₁d₂d₃d₄d₅d₆**:

1. Place the digits on the six vertices of a **hexagon** in cyclic order.
2. For each edge, compute the digital root of the sum of its two endpoint digits:
   `sᵢ = dr(dᵢ + dᵢ₊₁)`, indices modulo 6.
3. Form two 6‑digit strings:
   - `D = desc(s₁, …, s₆)` — non‑increasing order.
   - `A = asc(s₁, …, s₆)` — non‑decreasing order.
4. **T₆(n) = D − A**, written as a 6‑digit string with leading zeros.

### Fixed points and cycle

- **Fixed points:** `000000` (trivial) and **`761733`** (Khokhar Constant).
- **Period‑2 cycle:** `759933 ↔ 831762`.
- **Basin sizes:** `761733` captures **89.64 %**, the 2‑cycle captures **10.34 %**, and `000000` captures **0.02 %** (211 inputs).

### 🔹 Step-by-Step Example (Hexagon): starting from `123456`

**Step 0 — n = 123456**
- Vertices: 1, 2, 3, 4, 5, 6
- Edge sums: 3, 5, 7, 9, 11, 7
- Digital roots: **3, 5, 7, 9, 2, 7**
- D = **977532**, A = **235779**
- T₆(123456) = 977532 − 235779 = **741753**

**Step 1 — n = 741753**
- Vertices: 7, 4, 1, 7, 5, 3
- Edge sums: 11, 5, 8, 12, 8, 10
- Digital roots: **2, 5, 8, 3, 8, 1**
- D = **885321**, A = **123588**
- T₆(741753) = 885321 − 123588 = **761733**

**Step 2 — n = 761733 (FIXED POINT)**
- Vertices: 7, 6, 1, 7, 3, 3
- Edge sums: 13, 7, 8, 10, 6, 10
- Digital roots: **4, 7, 8, 1, 6, 1**
- D = **876411**, A = **114678**
- T₆(761733) = 876411 − 114678 = **761733** ✅

**Orbit:** `123456 → 741753 → 761733`

### 🔹 Second Example (Hexagon): starting from `987654`

- Step 0: 987654 → edge roots 8,6,4,2,9,4 → D=986442, A=244689 → **741753**
- Step 1: 741753 → **761733** (fixed)
- Orbit: `987654 → 741753 → 761733`

### 🔹 Third Example (Hexagon): starting from `111111`

- Step 0: 111111 → all edge roots = 2 → D = A = 222222 → **000000**
- Orbit: `111111 → 000000` (fixed)

### 🔹 Period‑2 Cycle Example: starting from `759933`

- Step 0: 759933 → edge roots 3,5,9,3,6,1 → D=965331, A=133569 → **831762**
- Step 1: 831762 → edge roots 2,4,8,4,8,1 → D=884421, A=124488 → **759933**
- The two numbers repeat forever: `759933 ↔ 831762`

### 📊 Hexagon Orbit Table (for `123456`)

| Step | n | Edge roots | D (desc) | A (asc) | T₆(n) |
|------|---|------------|----------|---------|-------|
| 0 | 123456 | 3,5,7,9,2,7 | 977532 | 235779 | 741753 |
| 1 | 741753 | 2,5,8,3,8,1 | 885321 | 123588 | 761733 |
| 2 | 761733 | 4,7,8,1,6,1 | 876411 | 114678 | **761733** |

---

## 🖥️ GUI Features (common to both files)

- **Step‑by‑step execution** — advance one iteration at a time.
- **Auto‑run mode** — watch the orbit unfold automatically (600 ms per step).
- **Visual diagram** — square (4‑digit) or hexagon (6‑digit) with digits, edge sums, and digital roots.
- **Edge analysis panel** — shows every edge sum and its digital root.
- **Transformation details** — displays `D`, `A`, and the computed `T(n)`.
- **Orbit history** — scrollable log of all steps.
- **Fixed‑point detection** — highlights when a fixed point (or cycle) is reached.
- **Integrated help** — pop‑up with formulas and worked examples.

---

## 🚀 Installation & Usage

### Prerequisites

- **Python 3.8** or higher
- **Tkinter** — included with standard Python on Windows and macOS; on Linux, install via your package manager (e.g. `sudo apt-get install python3-tk`)
- **Matplotlib** and **NumPy** — install via `pip install matplotlib numpy`

### Clone the repository

```bash
git clone https://github.com/yourusername/khokhar-digital-root-transformations.git
cd khokhar-digital-root-transformations
```

### Run the 4‑digit Square GUI

```bash
python khokhar_square_gui.py
```

### Run the 6‑digit Hexagon GUI

```bash
python khokhar_hexagon_gui.py
```

---

## 📁 Repository Structure

```
khokhar-digital-root-transformations/
│
├── khokhar_square_gui.py          # 4-digit square transformation GUI
├── khokhar_hexagon_gui.py         # 6-digit hexagon transformation GUI
├── README.md                      # this file
└── figures/                       # optional screenshots
```

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- **Muhammad Saddam Khokhar** — conceptualization, mathematics, and original implementation.
- **Misbah Ayoub** — contributions to the 6‑digit analysis.
- **Zakria** — contributions to the 6‑digit analysis.
- Open‑source tools: Python, Tkinter, Matplotlib, NumPy.

---

## 📚 References

1. Khokhar, M. S., Ayoub, M., & Jamali, Z. (2026). *The KHOKHAR Square Digital Root Transformation: 7443 A Fixed-Point Analysis of a 4-Digit Graph-Based Iterative Map*. SSRN. https://ssrn.com/abstract=7438803
2. Khokhar, M. S., Ayoub, M., & Zakria. (2026). *The KHOKHAR Square Digital Root Transformation: 7443 a Fixed-Point Analysis of a 4-Digit Graph-Based Iterative Map*. Preprints. https://doi.org/10.20944/preprints202608.1972.v1
3. Bhattacharjee, P. K. (2020). Kaprekar's Constant 6174 for Four Digits Number Reality to Other Digits Number. *International Journal of Chemistry, Mathematics and Physics*, 4(5), 92–94.

---

## 📬 Contact

**Dr. Muhammad Saddam Khokhar**

📧 saddam_khokhar@hotmail.com
🔗 ORCID: 0000-0001-7489-0542

---

⭐ If you find this work useful, please consider starring the repository and citing the associated preprint.
