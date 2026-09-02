import tkinter as tk
from tkinter import ttk, messagebox


# -----------------------------
# Conversion Functions
# -----------------------------

def convert():
    try:
        value = float(value_entry.get())
        category = category_var.get()
        from_unit = from_var.get()
        to_unit = to_var.get()

        if category == "Length":
            units = {
                "Meter": 1,
                "Kilometer": 1000,
                "Centimeter": 0.01,
                "Millimeter": 0.001,
                "Mile": 1609.34,
                "Yard": 0.9144,
                "Foot": 0.3048,
                "Inch": 0.0254
            }

            result = value * units[from_unit] / units[to_unit]

        elif category == "Weight":
            units = {
                "Kilogram": 1,
                "Gram": 0.001,
                "Milligram": 0.000001,
                "Pound": 0.453592,
                "Ounce": 0.0283495
            }

            result = value * units[from_unit] / units[to_unit]

        elif category == "Volume":
            units = {
                "Liter": 1,
                "Milliliter": 0.001,
                "Gallon": 3.78541,
                "Quart": 0.946353,
                "Pint": 0.473176,
                "Cup": 0.236588
            }

            result = value * units[from_unit] / units[to_unit]

        elif category == "Time":
            units = {
                "Second": 1,
                "Minute": 60,
                "Hour": 3600,
                "Day": 86400,
                "Week": 604800
            }

            result = value * units[from_unit] / units[to_unit]

        elif category == "Temperature":
            if from_unit == to_unit:
                result = value

            elif from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = (value * 9 / 5) + 32

            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = (value - 32) * 5 / 9

            elif from_unit == "Celsius" and to_unit == "Kelvin":
                result = value + 273.15

            elif from_unit == "Kelvin" and to_unit == "Celsius":
                result = value - 273.15

            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                result = (value - 32) * 5 / 9 + 273.15

            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                result = (value - 273.15) * 9 / 5 + 32

        result_label.config(
            text=f"{value:g} {from_unit} = {result:.4f} {to_unit}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

    except KeyError:
        messagebox.showerror("Error", "Please select valid units.")


# -----------------------------
# Update Units
# -----------------------------

def update_units(event=None):
    category = category_var.get()

    unit_lists = {
        "Length": [
            "Meter", "Kilometer", "Centimeter", "Millimeter",
            "Mile", "Yard", "Foot", "Inch"
        ],

        "Weight": [
            "Kilogram", "Gram", "Milligram", "Pound", "Ounce"
        ],

        "Volume": [
            "Liter", "Milliliter", "Gallon",
            "Quart", "Pint", "Cup"
        ],

        "Time": [
            "Second", "Minute", "Hour", "Day", "Week"
        ],

        "Temperature": [
            "Celsius", "Fahrenheit", "Kelvin"
        ]
    }

    units = unit_lists[category]

    from_combo["values"] = units
    to_combo["values"] = units

    from_var.set(units[0])
    to_var.set(units[1])


# -----------------------------
# Clear Function
# -----------------------------

def clear():
    value_entry.delete(0, tk.END)
    result_label.config(text="Result will appear here")


# -----------------------------
# Main Window
# -----------------------------

root = tk.Tk()
root.title("Unit Converter")
root.geometry("500x500")
root.resizable(False, False)

# Background
root.configure(bg="#f2f2f2")


# -----------------------------
# Title
# -----------------------------

title = tk.Label(
    root,
    text="UNIT CONVERTER",
    font=("Arial", 24, "bold"),
    bg="#f2f2f2"
)

title.pack(pady=25)


# -----------------------------
# Category
# -----------------------------

tk.Label(
    root,
    text="Select Category",
    font=("Arial", 12),
    bg="#f2f2f2"
).pack()

category_var = tk.StringVar()
category_var.set("Length")

category_combo = ttk.Combobox(
    root,
    textvariable=category_var,
    values=[
        "Length",
        "Weight",
        "Temperature",
        "Volume",
        "Time"
    ],
    state="readonly",
    width=25
)

category_combo.pack(pady=8)
category_combo.bind("<<ComboboxSelected>>", update_units)


# -----------------------------
# Value
# -----------------------------

tk.Label(
    root,
    text="Enter Value",
    font=("Arial", 12),
    bg="#f2f2f2"
).pack(pady=(15, 5))

value_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center",
    width=27
)

value_entry.pack()


# -----------------------------
# From Unit
# -----------------------------

tk.Label(
    root,
    text="From",
    font=("Arial", 12),
    bg="#f2f2f2"
).pack(pady=(15, 5))

from_var = tk.StringVar()

from_combo = ttk.Combobox(
    root,
    textvariable=from_var,
    state="readonly",
    width=25
)

from_combo.pack()


# -----------------------------
# To Unit
# -----------------------------

tk.Label(
    root,
    text="To",
    font=("Arial", 12),
    bg="#f2f2f2"
).pack(pady=(15, 5))

to_var = tk.StringVar()

to_combo = ttk.Combobox(
    root,
    textvariable=to_var,
    state="readonly",
    width=25
)

to_combo.pack()


# -----------------------------
# Buttons
# -----------------------------

button_frame = tk.Frame(root, bg="#f2f2f2")
button_frame.pack(pady=25)

convert_button = tk.Button(
    button_frame,
    text="CONVERT",
    command=convert,
    font=("Arial", 12, "bold"),
    width=12,
    padx=10
)

convert_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    command=clear,
    font=("Arial", 12, "bold"),
    width=12,
    padx=10
)

clear_button.grid(row=0, column=1, padx=5)


# -----------------------------
# Result
# -----------------------------

result_label = tk.Label(
    root,
    text="Result will appear here",
    font=("Arial", 14, "bold"),
    bg="#f2f2f2",
    wraplength=450
)

result_label.pack(pady=10)


# Initialize units
update_units()


# Start application
root.mainloop()