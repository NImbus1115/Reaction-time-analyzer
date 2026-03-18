import time
import random
import matplotlib.pyplot as plt

print("Reaction Time Test")
print("When you see 'CLICK NOW!', press Enter as fast as possible.")
input("Press Enter to start...")

reaction_times = []

for i in range(5):
    wait_time = random.uniform(2, 5)
    time.sleep(wait_time)

    print("CLICK NOW!")

    start_time = time.time()
    input()
    end_time = time.time()

    reaction_time = end_time - start_time
    reaction_times.append(reaction_time)

    print(f"Your reaction time: {reaction_time:.3f} seconds\n")

average_time = sum(reaction_times) / len(reaction_times)
print(f"Average Reaction Time: {average_time:.3f} seconds")

plt.plot(reaction_times, marker='o')
plt.title("Reaction Time Over Trials")
plt.xlabel("Trial Number")
plt.ylabel("Reaction Time (seconds)") 
plt.show()