import tkinter as tk
from tkinter import ttk, messagebox

# ----------------------------------------------------------------------
# Core transformation logic (unchanged)
# ----------------------------------------------------------------------

def digital_root(n: int) -> int:
    if n == 0:
        return 0
    return 1 + (n - 1) % 9

def desc_digits(digits):
    return ''.join(sorted(map(str, digits), reverse=True))

def asc_digits(digits):
    return ''.join(sorted(map(str, digits)))

def khokhar_transform(n_str: str):
    d = tuple(int(ch) for ch in n_str.zfill(4))
    raw_sums = (
        d[0] + d[1],
        d[1] + d[2],
        d[2] + d[3],
        d[3] + d[0],
    )
    s = tuple(digital_root(x) for x in raw_sums)
    desc_val = desc_digits(s)
    asc_val = asc_digits(s)
    result_num = int(desc_val) - int(asc_val)
    result = f"{result_num:04d}"
    return result, d, s, raw_sums, desc_val, asc_val

# ----------------------------------------------------------------------
# GUI Application (refined for responsiveness)
# ----------------------------------------------------------------------

class KHOKHARApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KHOKHAR Square Digital Root Transformation")
        self.root.geometry("950x750")
        self.root.minsize(850, 700)

        # State
        self.current_number = ""
        self.history = []
        self.current_step = 0
        self.is_running = False
        self.auto_run_id = None
        self.fixed_point = None

        # Build UI
        self._build_ui()
        self.reset_state()

    def _build_ui(self):
        # Main container
        main = ttk.Frame(self.root, padding="15")
        main.pack(fill=tk.BOTH, expand=True)

        # Header
        ttk.Label(main, text="🔢 KHOKHAR Square Digital Root Transformation",
                  font=('Segoe UI', 16, 'bold')).pack(anchor='w')

        # Controls
        ctrl = ttk.Frame(main)
        ctrl.pack(fill=tk.X, pady=10)

        ttk.Label(ctrl, text="Start number:").pack(side=tk.LEFT, padx=(0,5))
        self.input_var = tk.StringVar()
        self.input_var.trace('w', self._on_input_change)
        ttk.Entry(ctrl, textvariable=self.input_var, width=8,
                  font=('Segoe UI', 12, 'bold'), justify='center').pack(side=tk.LEFT, padx=(0,15))

        self.next_btn = ttk.Button(ctrl, text="▶ Next Step", command=self.next_step, width=12)
        self.next_btn.pack(side=tk.LEFT, padx=(0,8))

        self.reset_btn = ttk.Button(ctrl, text="↺ Reset", command=self.reset_state, width=10)
        self.reset_btn.pack(side=tk.LEFT, padx=(0,8))

        self.auto_btn = ttk.Button(ctrl, text="▶▶ Auto-run", command=self.toggle_auto_run, width=12)
        self.auto_btn.pack(side=tk.LEFT, padx=(0,8))

        self.help_btn = ttk.Button(ctrl, text="❓ Help", command=self.show_help, width=10)
        self.help_btn.pack(side=tk.LEFT)

        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(ctrl, textvariable=self.status_var, font=('Segoe UI', 9, 'italic'),
                  foreground='#7f8c8d').pack(side=tk.RIGHT)

        # Two‑column display
        display = ttk.Frame(main)
        display.pack(fill=tk.BOTH, expand=True, pady=10)

        # Left: Canvas
        left = ttk.Frame(display)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0,10))

        self.canvas = tk.Canvas(left, bg='#ffffff', width=450, height=320, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True, pady=10)

        info_frame = ttk.Frame(left)
        info_frame.pack(fill=tk.X)
        self.current_label = ttk.Label(info_frame, text="Current: —", font=('Segoe UI', 13, 'bold'))
        self.current_label.pack(side=tk.LEFT)
        self.step_label = ttk.Label(info_frame, text="Step 0", font=('Segoe UI', 10), foreground='#7f8c8d')
        self.step_label.pack(side=tk.RIGHT)

        # Right: Edge, Result, History
        right = ttk.Frame(display)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Edge Analysis
        edge_frame = ttk.LabelFrame(right, text="📊 Edge Analysis", padding=10)
        edge_frame.pack(fill=tk.X, pady=(0,10))
        self.edge_info_var = tk.StringVar(value="Enter a number and click 'Next Step'")
        ttk.Label(edge_frame, textvariable=self.edge_info_var, wraplength=350,
                  justify='left').pack(anchor='w')

        # Transformation Result
        res_frame = ttk.LabelFrame(right, text="📐 Transformation", padding=10)
        res_frame.pack(fill=tk.X, pady=(0,10))
        self.result_info_var = tk.StringVar(value="D = —, A = —")
        ttk.Label(res_frame, textvariable=self.result_info_var, wraplength=350,
                  justify='left').pack(anchor='w')
        self.result_value_var = tk.StringVar(value="T(n) = —")
        ttk.Label(res_frame, textvariable=self.result_value_var,
                  font=('Segoe UI', 14, 'bold'), foreground='#3498db').pack(anchor='w', pady=(5,0))

        # History
        hist_frame = ttk.LabelFrame(right, text="📜 Orbit History", padding=10)
        hist_frame.pack(fill=tk.BOTH, expand=True)
        self.history_text = tk.Text(hist_frame, height=6, font=('Segoe UI', 10),
                                    bg='#f8f9fa', wrap=tk.WORD, state='disabled')
        scroll = ttk.Scrollbar(hist_frame, orient=tk.VERTICAL, command=self.history_text.yview)
        self.history_text.configure(yscrollcommand=scroll.set)
        self.history_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Fixed point indicator
        self.fixed_indicator = ttk.Label(main, text="", font=('Segoe UI', 11, 'bold'),
                                         foreground='#27ae60')
        self.fixed_indicator.pack(fill=tk.X)

    # ------------------------------------------------------------------
    # Drawing methods
    # ------------------------------------------------------------------

    def _draw_square(self, d, s, current_num):
        """Draw the square with current digits and edge sums."""
        self.canvas.delete("all")
        w = self.canvas.winfo_width() if self.canvas.winfo_width() > 50 else 450
        h = self.canvas.winfo_height() if self.canvas.winfo_height() > 50 else 320
        size = min(w - 100, h - 80, 240)
        margin_x = (w - size) // 2
        margin_y = (h - size) // 2
        x1, y1 = margin_x, margin_y
        x2, y2 = margin_x + size, margin_y
        x3, y3 = margin_x + size, margin_y + size
        x4, y4 = margin_x, margin_y + size

        d_str = [str(x) for x in d]
        s_str = [str(x) for x in s]

        # Edges
        self.canvas.create_line(x1, y1, x2, y2, fill='#dce1e8', width=2)
        self.canvas.create_text((x1+x2)//2, (y1+y2)//2 - 22, text=f"s₁ = {s_str[0]}",
                                font=('Segoe UI', 10, 'bold'), fill='#3498db')
        self.canvas.create_line(x2, y2, x3, y3, fill='#dce1e8', width=2)
        self.canvas.create_text((x2+x3)//2 + 22, (y2+y3)//2, text=f"s₂ = {s_str[1]}",
                                font=('Segoe UI', 10, 'bold'), fill='#3498db')
        self.canvas.create_line(x3, y3, x4, y4, fill='#dce1e8', width=2)
        self.canvas.create_text((x3+x4)//2, (y3+y4)//2 + 22, text=f"s₃ = {s_str[2]}",
                                font=('Segoe UI', 10, 'bold'), fill='#3498db')
        self.canvas.create_line(x4, y4, x1, y1, fill='#dce1e8', width=2)
        self.canvas.create_text((x4+x1)//2 - 22, (y4+y1)//2, text=f"s₄ = {s_str[3]}",
                                font=('Segoe UI', 10, 'bold'), fill='#3498db')

        # Vertices
        radius = 22
        for (x, y, label, value) in [(x1,y1,"d₁",d_str[0]), (x2,y2,"d₂",d_str[1]),
                                     (x3,y3,"d₃",d_str[2]), (x4,y4,"d₄",d_str[3])]:
            self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius,
                                    fill='#ebf5fb', outline='#3498db', width=2)
            self.canvas.create_text(x, y-6, text=label, font=('Segoe UI', 9, 'bold'),
                                    fill='#7f8c8d')
            self.canvas.create_text(x, y+12, text=value, font=('Segoe UI', 16, 'bold'),
                                    fill='#2c3e50')

        # Title & edge sums detail
        self.canvas.create_text(w//2, 18, text=f"Current: {current_num}",
                                font=('Segoe UI', 12, 'bold'), fill='#2c3e50')
        if all(str(x).isdigit() for x in d):
            detail = "Edge sums: "
            parts = [f"{d[i]}+{d[(i+1)%4]}={d[i]+d[(i+1)%4]} → {s[i]}" for i in range(4)]
            detail += "  |  ".join(parts)
            self.canvas.create_text(w//2, h-12, text=detail, font=('Segoe UI', 9),
                                    fill='#7f8c8d', anchor='s')

    # ------------------------------------------------------------------
    # Event Handlers
    # ------------------------------------------------------------------

    def _on_input_change(self, *args):
        val = self.input_var.get().strip()
        if val and (not val.isdigit() or len(val) > 4):
            if len(val) > 4:
                self.input_var.set(val[:4])

    def reset_state(self):
        self._stop_auto_run()
        val = self.input_var.get().strip()
        if not val.isdigit() or len(val) != 4:
            val = "1234"
            self.input_var.set(val)
        self.current_number = val.zfill(4)
        self.history = []
        self.current_step = 0
        self.fixed_point = None

        # Compute initial edge sums
        _, d, s, raw, _, _ = khokhar_transform(self.current_number)
        self._draw_square(d, s, self.current_number)

        edge_lines = [f"{['Top','Right','Bottom','Left'][i]}: {d[i]}+{d[(i+1)%4]}={raw[i]} → {s[i]}"
                      for i in range(4)]
        self.edge_info_var.set("\n".join(edge_lines))
        self.result_info_var.set("D = —, A = —")
        self.result_value_var.set("T(n) = ?")
        self.fixed_indicator.config(text="")
        self.status_var.set("Ready")

        self.history_text.config(state='normal')
        self.history_text.delete('1.0', tk.END)
        self.history_text.config(state='disabled')

        self.current_label.config(text=f"Current: {self.current_number}")
        self.step_label.config(text="Step 0")
        self.next_btn.config(state='normal')
        self.auto_btn.config(text="▶▶ Auto-run", state='normal')
        self.root.update_idletasks()

    def next_step(self):
        if self.is_running and self.auto_run_id is not None:
            # Prevent overlapping calls
            return
        if self.fixed_point is not None:
            messagebox.showinfo("Fixed Point", f"Already at {self.fixed_point}. Reset to try again.")
            return

        n_str = self.current_number
        result, d, s, raw, desc_val, asc_val = khokhar_transform(n_str)
        self.current_step += 1
        self.history.append((self.current_step, n_str, result, d, s, raw, desc_val, asc_val))

        # Update UI
        self._draw_square(d, s, n_str)
        edge_lines = [f"{['Top','Right','Bottom','Left'][i]}: {d[i]}+{d[(i+1)%4]}={raw[i]} → {s[i]}"
                      for i in range(4)]
        self.edge_info_var.set("\n".join(edge_lines))
        self.result_info_var.set(f"D = desc({', '.join(map(str, s))}) = {desc_val}  |  A = asc({', '.join(map(str, s))}) = {asc_val}")
        self.result_value_var.set(f"T({n_str}) = {desc_val} - {asc_val} = {result}")

        self.current_number = result
        self.current_label.config(text=f"Current: {result}")
        self.step_label.config(text=f"Step {self.current_step}")

        # Update history
        self.history_text.config(state='normal')
        self.history_text.delete('1.0', tk.END)
        orbit = " → ".join([h[1] for h in self.history] + [result])
        lines = ["Orbit: " + orbit, ""]
        for step, n, res, d, s, raw, desc, asc in self.history:
            lines.append(f"  Step {step}: {n} → {res}  (D={desc}, A={asc}, roots={', '.join(map(str, s))})")
        self.history_text.insert('1.0', "\n".join(lines))
        self.history_text.config(state='disabled')
        self.history_text.see(tk.END)

        # Fixed point check
        if result == n_str:
            self.fixed_point = result
            self.fixed_indicator.config(text=f"✓ Fixed point reached: {result} after {self.current_step} steps!")
            self.status_var.set(f"✓ Fixed point {result}")
            self.next_btn.config(state='disabled')
            self.auto_btn.config(state='disabled')
            self.is_running = False  # stop auto if running
            if self.auto_run_id:
                self.root.after_cancel(self.auto_run_id)
                self.auto_run_id = None
            self.auto_btn.config(text="▶▶ Auto-run")
        else:
            self.status_var.set(f"Step {self.current_step} → {result}")

        self.root.update_idletasks()

        # If auto-run is on, schedule next step with shorter delay (600ms)
        if self.is_running and self.fixed_point is None:
            self.auto_run_id = self.root.after(600, self.next_step)

    # ------------------------------------------------------------------
    # Auto-run control
    # ------------------------------------------------------------------

    def toggle_auto_run(self):
        if self.is_running:
            self._stop_auto_run()
        else:
            self._start_auto_run()

    def _start_auto_run(self):
        if self.fixed_point is not None:
            messagebox.showinfo("Fixed Point", f"Already at {self.fixed_point}. Reset first.")
            return
        self.is_running = True
        self.auto_btn.config(text="⏹ Stop")
        self.next_btn.config(state='disabled')
        self.status_var.set("Auto-running...")
        # Start immediately
        self.next_step()

    def _stop_auto_run(self):
        self.is_running = False
        if self.auto_run_id:
            self.root.after_cancel(self.auto_run_id)
            self.auto_run_id = None
        self.auto_btn.config(text="▶▶ Auto-run")
        if self.fixed_point is None:
            self.next_btn.config(state='normal')
        self.status_var.set("Stopped")

    # ------------------------------------------------------------------
    # Help dialog
    # ------------------------------------------------------------------

    def show_help(self):
        help_text = r"""
KHOKHAR Square Digital Root Transformation
===========================================

Given a 4-digit number n = d₁d₂d₃d₄, the transformation T(n) is:

1. Place d₁, d₂, d₃, d₄ on the four vertices of a square in cyclic order.

2. For each edge, compute the digital root of the sum of its two endpoint digits:
   s₁ = dr(d₁ + d₂)
   s₂ = dr(d₂ + d₃)
   s₃ = dr(d₃ + d₄)
   s₄ = dr(d₄ + d₁)

3. Form two 4-digit strings from the multiset {s₁, s₂, s₃, s₄}:
   D = desc(s₁, s₂, s₃, s₄)   (non-increasing order)
   A = asc(s₁, s₂, s₃, s₄)    (non-decreasing order)

4. The transformation is:
   T(n) = D - A

Digital Root:
dr(n) = 1 + (n-1) mod 9 for n > 0, and dr(0) = 0.

Example: n = 1234
─────────────────
Edge sums: 1+2=3, 2+3=5, 3+4=7, 4+1=5
Digital roots: 3, 5, 7, 5
D = 7553, A = 3557
T(1234) = 7553 - 3557 = 3996

Orbit: 1234 → 3996 → 6264 → 7623 → 7083 → 7443 (fixed point)
"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Help")
        dialog.geometry("600x500")
        dialog.transient(self.root)
        dialog.grab_set()
        frame = ttk.Frame(dialog, padding=15)
        frame.pack(fill=tk.BOTH, expand=True)
        text = tk.Text(frame, font=('Consolas', 10), bg='#f8f9fa', wrap=tk.WORD)
        scroll = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=text.yview)
        text.configure(yscrollcommand=scroll.set)
        text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        text.insert('1.0', help_text)
        text.config(state='disabled')
        ttk.Button(dialog, text="Close", command=dialog.destroy).pack(pady=10)

# ----------------------------------------------------------------------
# Run
# ----------------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = KHOKHARApp(root)
    root.mainloop()