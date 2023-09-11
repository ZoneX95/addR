import itertools
import tkinter as tk
from tkinter import messagebox, scrolledtext

def best_sum(numbers, target):
    combinations = []
    for length in range(1, len(numbers) + 1):
        for combination in itertools.combinations(numbers, length):
            combination_sum = sum(combination)
            if combination_sum <= target:
                difference = abs(combination_sum - target)
                combinations.append((combination, combination_sum, difference))
    combinations.sort(key=lambda x: x[2])
    best_combinations = []
    smallest_difference = combinations[0][2]
    for combination in combinations:
        if combination[2] == smallest_difference:
            best_combinations.append(combination)
        else:
            break
    return best_combinations

def calculate():
    numbers_input = numbers_entry.get()
    numbers_strings = numbers_input.split(",")
    try:
        numbers = [float(number) for number in numbers_strings]
    except ValueError:
        messagebox.showerror("Nevažeći unos", "Molimo unesite valjane brojeve.")
        return

    target_input = target_entry.get()
    try:
        target = float(target_input)
    except ValueError:
        messagebox.showerror("Nevažeći unos", "Molimo unesite valjani ciljni broj.")
        return

    result = best_sum(numbers, target)
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    for solution in result:
        rounded_combination = [round(num) for num in solution[0]]
        rounded_sum = round(solution[1])
        rounded_difference = round(solution[2])
        result_text.insert(tk.END, f"Kombinacija: {rounded_combination}, Zbir: {rounded_sum}, Razlika: {rounded_difference}\n")
    result_text.config(state=tk.DISABLED)

# Create the main application window
app = tk.Tk()
app.title("addR")

# Create and place GUI elements
numbers_label = tk.Label(app, text="Unesite brojeve razdvojene zarezima:")
numbers_entry = tk.Entry(app)
target_label = tk.Label(app, text="Unesite ciljni broj:")
target_entry = tk.Entry(app)
calculate_button = tk.Button(app, text="Izračunaj", command=calculate)
result_label = tk.Label(app, text="Rezultati:")
result_text = scrolledtext.ScrolledText(app, height=10, width=50, state=tk.DISABLED)  # Adjusted width

numbers_label.pack()
numbers_entry.pack()
target_label.pack()
target_entry.pack()
calculate_button.pack()
result_label.pack()
result_text.pack()

# Start the GUI event loop
app.mainloop()
