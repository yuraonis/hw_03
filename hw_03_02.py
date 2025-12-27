import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt

# Дані
x = np.array([0, 1, 1.5, 2.5, 3, 4.5, 5, 6])
y = np.array([0, 67, 101, 168, 202, 310, 334, 404])


def calculate():
    # Очистка таблиці
    for row in table.get_children():
        table.delete(row)

    # МНК для y = a*x^2 + b
    X = np.column_stack((x**2, np.ones(len(x))))
    a, b = np.linalg.lstsq(X, y, rcond=None)[0]

    # Оновлення тексту рівняння
    label_result.config(
        text=f"Рівняння регресії: y = {a:.4f}·x² + {b:.4f}"
    )

    # Заповнення таблиці
    for i in range(len(x)):
        y_reg = a * x[i]**2 + b
        table.insert(
            "",
            "end",
            values=(i + 1, x[i], y[i], round(y_reg, 2))
        )

    # Побудова графіка
    x_plot = np.linspace(min(x), max(x), 300)
    y_plot = a * x_plot**2 + b

    plt.figure()
    plt.scatter(x, y, label="Експериментальні точки")
    plt.plot(x_plot, y_plot, label="Крива регресії")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Лінійна регресія методом МНК (y = a·x² + b)")
    plt.grid()
    plt.legend()
    plt.show()


# --- Інтерфейс ---
root = tk.Tk()
root.title("Лінійна регресія")
root.geometry("750x500")

tk.Label(
    root,
    text="Лінійна регресія методом найменших квадратів",
    font=("Arial", 14)
).pack(pady=10)

tk.Button(
    root,
    text="Обчислити",
    command=calculate,
    width=20
).pack(pady=10)

label_result = tk.Label(
    root,
    text="Рівняння регресії:"
)
label_result.pack(pady=5)

columns = ("№", "x", "y", "y (регресія)")
table = ttk.Treeview(
    root,
    columns=columns,
    show="headings"
)

for col in columns:
    table.heading(col, text=col)
    table.column(col, anchor="center")

table.pack(expand=True, fill="both", padx=10, pady=10)

root.mainloop()
