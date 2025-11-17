1
import tkinter as tk
from tkinter import messagebox
from backend.phone_lookup import lookup_number  # import backend function

def run_lookup():
    number = entry.get().strip()
    result = lookup_number(number)

    if "error" in result:
        messagebox.showerror("Error", result["error"])
    else:
        result_text = (
            f"Country: {result['country']}\n"
            f"City/Region: {result['city']}\n"
            f"Carrier: {result['carrier']}\n"
            f"Line Type: {result['line_type']}"
        )
        result_box.config(state="normal")
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, result_text)
        result_box.config(state="disabled")

def clear_fields():
    entry.delete(0, tk.END)
    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)
    result_box.config(state="disabled")

def copy_results():
    root.clipboard_clear()
    text = result_box.get("1.0", tk.END).strip()
    root.clipboard_append(text)
    root.update()
    messagebox.showinfo("Copied", "Results copied to clipboard!")

# --------------------------
# GUI Setup (Enhanced)
# --------------------------
root = tk.Tk()
root.title("📱 Phone Number Lookup (Truecaller Lite)")
root.geometry("500x350")
root.resizable(False, False)
root.config(bg="#f4f4f4")

# Input section
frame_top = tk.Frame(root, bg="#f4f4f4")
frame_top.pack(pady=10)

tk.Label(frame_top, text="Enter Phone Number (+countrycode):", bg="#f4f4f4", font=("Arial", 11)).pack(anchor="w")
entry = tk.Entry(frame_top, width=35, font=("Arial", 13))
entry.pack(pady=5)

# Buttons
frame_btns = tk.Frame(root, bg="#f4f4f4")
frame_btns.pack(pady=5)

tk.Button(frame_btns, text="Lookup", command=run_lookup, bg="#007BFF", fg="white", font=("Arial", 11), width=12).grid(row=0, column=0, padx=5)
tk.Button(frame_btns, text="Clear", command=clear_fields, bg="#6c757d", fg="white", font=("Arial", 11), width=12).grid(row=0, column=1, padx=5)
tk.Button(frame_btns, text="Copy", command=copy_results, bg="#28a745", fg="white", font=("Arial", 11), width=12).grid(row=0, column=2, padx=5)

# Results box
frame_results = tk.Frame(root, bg="#FEFBFB")
frame_results.pack(pady=10, fill="both", expand=True)
tk.Label(frame_results, text="Results:", bg="#f4f4f4", font=("Arial", 11, "bold")).pack(anchor="w")
result_box = tk.Text(frame_results, height=8, width=55, font=("Consolas", 11), state="disabled", wrap="word")
result_box.pack(pady=5)

# Run app
root.mainloop()


