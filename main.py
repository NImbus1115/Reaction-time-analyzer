import tkinter as tk
import time
import random
import statistics
import matplotlib.pyplot as plt   

# ---- SETUP WINDOW ----
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="grey")

# ---- VARIABLES ----
reaction_times = []
memory_numbers = []
trial = 0
max_trials = 5
start_time = 0

# ---- LABEL ----
label = tk.Label(root, text="", font=("Arial", 50), fg="white", bg="grey")
label.pack(expand=True)

# ---- FUNCTIONS ----

def start_experiment(event=None):
    global trial
    trial = 0
    reaction_times.clear()
    memory_numbers.clear()
    next_trial()

def next_trial():
    global trial
    if trial < max_trials:
        delay = random.uniform(2000, 5000)
        root.after(int(delay), show_stimulus)
    else:
        show_results()

def show_stimulus():
    global start_time

    number = random.randint(10, 99)
    memory_numbers.append(number)

    label.config(text=f"REMEMBER: {number}\n\nWAIT...")
    root.after(1500, show_click)

def show_click():
    global start_time
    label.config(text="CLICK NOW!\n(Press SPACE)")
    start_time = time.time()

def record_reaction(event):
    global trial

    if label.cget("text").startswith("CLICK NOW"):
        end_time = time.time()
        reaction_time = end_time - start_time
        reaction_times.append(reaction_time)

        trial += 1
        label.config(text=f"Trial {trial}: {reaction_time:.3f} sec")

        root.after(1500, next_trial)

# ---- RESULTS ----
def show_results():
    avg = sum(reaction_times) / len(reaction_times)
    std_dev = statistics.stdev(reaction_times)

    # Fatigue / Adaptation
    if reaction_times[-1] > reaction_times[0]:
        trend = "Fatigue detected"
    elif reaction_times[-1] < reaction_times[0]:
        trend = "Adaptation detected"
    else:
        trend = "No clear trend"

    label.config(
        text=f"Average: {avg:.3f} sec\n"
             f"Variability: {std_dev:.3f}\n"
             f"{trend}\n\n"
             f"Showing graph..."
    )

    root.after(2000, show_graph)   

def show_graph():
    root.destroy() 

    plt.plot(reaction_times, marker='o')
    plt.title("Reaction Time Over Trials")
    plt.xlabel("Trial Number")
    plt.ylabel("Reaction Time (seconds)")
    plt.grid()
    plt.show()

    memory_test()  

# ---- MEMORY TEST ----
def memory_test():
    print("\nRecall the numbers:")
    correct = 0

    for i, num in enumerate(memory_numbers):
        answer = input(f"Trial {i+1}: ")
        if answer == str(num):
            correct += 1

    print(f"Memory Score: {correct}/{max_trials}")

# ---- CONTROLS ----
root.bind("<space>", record_reaction)
root.bind("<Return>", start_experiment)
root.bind("<Escape>", lambda e: root.destroy())

# ---- START SCREEN ----
label.config(text="Press ENTER to Start\nPress ESC to Exit")

root.mainloop() 