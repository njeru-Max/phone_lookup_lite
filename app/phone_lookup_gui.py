import tkinter as tk
from tkinter import messagebox
from backend.phone_lookup import lookup_number   # import function from your file

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
        result_label.config(text=result_text)

# --------------------------
# GUI Setup
# --------------------------
root = tk.Tk()
root.title("Phone Number Lookup (Truecaller Lite)")
root.geometry("400x250")
root.resizable(False, False)

# Input field
tk.Label(root, text="Enter Phone Number (+countrycode):").pack(pady=5)
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=5)

# Search button
lookup_btn = tk.Button(root, text="Lookup", command=run_lookup,
                       bg="blue", fg="white", font=("Arial", 12))
lookup_btn.pack(pady=10)

# Results label
result_label = tk.Label(root, text="", font=("Arial", 11), justify="left")
result_label.pack(pady=10)

# Run app
root.mainloop()
