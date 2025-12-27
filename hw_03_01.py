import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt


# Вихідні експериментальні дані
x_data = [0, 1, 1.5, 2.5, 3, 4.5, 5, 6]
y_data = [0, 67, 101, 168, 202, 310, 334, 404]


# Функція для обчислення коефіцієнтів лінійної регресії
def linear_regression(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum(xi ** 2 for xi in x)
    sum_xy = sum(x[i] * y[i] for i in range(n))

    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    b = (sum_y - a * sum_x) / n
    return a, b


# Основна функція обчислення та оновлення інтерфейсу
def calculate():
    try:
        table.delete(*table.get_children())

        a, b = linear_regression(x_data, y_data)

        for i in range(len(x_data)):
            table.insert(
                "",
                "end",
                values=(
                    i + 1,
                    x_data[i],
                    y_data[i],
                    f"{a * x_data[i] + b:.3f}"
                )
            )

        label_result.config(
            text=f"Рівняння регресії: y = {a:.3f}x + {b:.3f}"
        )

        plot_graph(x_data, y_data, a, b)

    except Exception as e:
        messagebox.showerror("Помилка", str(e))


# Функція побудови графіка експериментальних точок і лінії регресії
def plot_graph(x, y, a, b):
    plt.figure()

    plt.scatter(x, y, label="Експериментальні точки")

    x_line = [min(x), max(x)]
    y_line = [a * xi + b for xi in x_line]
    plt.plot(x_line, y_line, label="Лінія регресії")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Лінійна регресія методом МНК")
    plt.grid(True)
    plt.legend()
    plt.show()


# Інтерфейс програми
root = tk.Tk()
root.title("Лінійна регресія")
root.geometry("750x500")

tk.Label(
    root,
    text="Лінійна регресія методом найменших квадратів"
).pack(pady=10)

tk.Button(
    root,
    text="Обчислити",
    command=calculate
).pack(pady=10)

label_result = tk.Label(
    root,
    text="Рівняння регресії:"
)
label_result.pack(pady=5)


# Таблиця для відображення результатів
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
