import tkinter as tk

# --- Theme definitions ---
themes = {
    "dark": {
        "bg": "#2e2e2e",
        "entry_bg": "#1e1e1e",
        "entry_fg": "#00FFAA",
        "btn_bg": "#3b3b3b",
        "btn_fg": "white",
        "btn_active_bg": "#505050",
        "btn_active_fg": "#00FFAA",
        "icon": "☀️"
    },
    "light": {
        "bg": "#f2f2f2",
        "entry_bg": "#ffffff",
        "entry_fg": "#222222",
        "btn_bg": "#e0e0e0",
        "btn_fg": "#000000",
        "btn_active_bg": "#cccccc",
        "btn_active_fg": "#000000",
        "icon": "🌙"
    }
}

current_theme = "dark"

# --- Main window ---
root = tk.Tk()
root.title("PyVisual Calculator")
root.resizable(False, False)

# --- Frame to hold toggle icon ---
top_frame = tk.Frame(root)
top_frame.grid(row=0, column=0, columnspan=4, sticky='e', padx=5, pady=5)
top_frame.configure(bg=themes[current_theme]['bg'])

# --- Entry display ---
entry = tk.Entry(root, width=16, font=('Arial', 30), bd=0, relief=tk.FLAT, justify='right')
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=(0, 20), ipady=10)

# --- Button click logic ---
def click(button_text):
    if button_text == '=':
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# --- Toggle button logic ---
def toggle_theme():
    global current_theme
    current_theme = "light" if current_theme == "dark" else "dark"
    apply_theme()

# --- Toggle icon button ---
toggle_btn = tk.Button(top_frame, text=themes["dark"]["icon"], command=toggle_theme,
                       font=('Arial', 14), bd=0, relief=tk.FLAT, bg=themes["dark"]["bg"], fg=themes["dark"]["entry_fg"],
                       activebackground=themes["dark"]["bg"], activeforeground=themes["dark"]["entry_fg"])
toggle_btn.pack(anchor='ne')

# --- Button layout ---
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

# --- Button creation ---
button_refs = []

for r, row in enumerate(buttons, start=2):
    for c, char in enumerate(row):
        b = tk.Button(root, text=char, command=lambda ch=char: click(ch), font=('Arial', 20), bd=0, relief=tk.FLAT)
        b.grid(row=r, column=c, padx=8, pady=8, ipadx=10, ipady=10)
        button_refs.append(b)

# --- Apply theme function ---
def apply_theme():
    theme = themes[current_theme]
    root.configure(bg=theme["bg"])
    top_frame.configure(bg=theme["bg"])
    entry.configure(bg=theme["entry_bg"], fg=theme["entry_fg"], insertbackground=theme["entry_fg"])
    toggle_btn.configure(
        text=theme["icon"],
        bg=theme["bg"],
        fg=theme["entry_fg"],
        activebackground=theme["bg"],
        activeforeground=theme["entry_fg"]
    )
    for btn in button_refs:
        btn.configure(
            bg=theme["btn_bg"],
            fg=theme["btn_fg"],
            activebackground=theme["btn_active_bg"],
            activeforeground=theme["btn_active_fg"]
        )

# --- Initial theme setup ---
apply_theme()

# --- Run the application ---
root.mainloop()
