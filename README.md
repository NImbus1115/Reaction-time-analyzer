# 🧠 Cognitive Reaction Time Experiment (GUI-Based)

A Python-based interactive cognitive experiment that measures human reaction time under dual-task conditions, while analyzing performance trends such as fatigue, adaptation, and response variability.

---

## 🚀 Features

* 🖥️ Full-screen GUI-based experimental interface (Tkinter)
* ⏱️ Real-time reaction time measurement using keyboard input
* 🧠 Dual-task paradigm:

  * React to stimulus (SPACE key)
  * Memorize numbers simultaneously
* 📊 Performance analysis:

  * Average reaction time
  * Variability (standard deviation)
  * Fatigue vs adaptation detection
* 📈 Graph visualization of reaction time across trials

---

## 🧠 Concept

Reaction time is a key behavioral measure used to study how quickly the brain processes stimuli and generates responses.

This project implements a **simplified experimental paradigm** that demonstrates:

* Stimulus-response timing
* Dual-task interference (reaction + memory load)
* Performance trends across trials (fatigue or learning effects)

While not a laboratory-grade system, this project provides a **conceptual and computational model** of how cognitive experiments can be structured, executed, and analyzed.

---

## 💻 Technologies Used

* Python
* Tkinter (GUI interface)
* Matplotlib (data visualization)
* Time, Random, Statistics modules

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/NImbus1115/Reaction-time-analyzer.git
```

2. Navigate to the project folder:

```bash
cd Reaction-time-analyzer
```

3. (Optional but recommended) Activate virtual environment:

```bash
source venv/bin/activate
```

4. Install required libraries:

```bash
pip install matplotlib
```

5. Run the program:

```bash
python3 main.py
```

---

## 🧪 Experimental Flow

1. Press **ENTER** to start the experiment
2. A number appears (to be memorized)
3. After a delay, stimulus appears ("CLICK NOW")
4. Press **SPACE** as quickly as possible
5. Repeat for multiple trials
6. View performance analysis and graph
7. Recall memory task in terminal

---

## 📊 Output

* Reaction time for each trial
* Average response time
* Variability (consistency of responses)
* Fatigue or adaptation trend
* Graph showing performance over trials
* Memory recall score

---

## 🎯 Applications

* Educational demonstration of cognitive experiments
* Understanding attention and cognitive load
* Introduction to behavioral data analysis
* Basic simulation of experimental design in cognitive science

---

## 🔮 Future Improvements

* Fully GUI-based memory test (remove terminal input)
* Multi-user comparison
* Data export (CSV for analysis)
* Enhanced experimental conditions (visual vs auditory stimuli)
* Real-time plotting

---

## 👨‍💻 Author

**Mehal Badgujar**

---

## ⭐ Note

This project is intended as a learning and demonstration tool for understanding how cognitive experiments can be implemented computationally using Python.










