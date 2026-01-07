# University Scheduling System 📅

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Django](https://img.shields.io/badge/Django-Framework-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Overview

The **University Scheduling System** is an automated tool designed to solve the complex "Time Table Scheduling Problem" faced by universities. It utilizes **Genetic Algorithms (AI)** to generate conflict-free academic schedules that optimize resource utilization (classrooms, professors, and time slots).

This project was developed as an **Honors Thesis** to demonstrate how evolutionary algorithms can solve NP-hard constraint satisfaction problems better than traditional heuristic methods.

## 🚀 Key Features

* **🧬 Genetic Algorithm Engine:** Implements selection, crossover, and mutation to evolve schedule populations toward an optimal solution.
* **⚡ Conflict Detection:** Automatically detects and resolves "hard constraints" (e.g., a professor double-booked, room capacity exceeded).
* **💻 Dual Interface:** * **Web Application:** A full-stack Django app for managing data and viewing schedules online.
    * **Desktop GUI:** A lightweight Tkinter interface for local testing.
* **📊 Optimization Metrics:** Scores schedules based on "soft constraints" (e.g., preferred time slots, minimizing gaps for students).

## 🛠️ Tech Stack

* **Language:** Python
* **Web Framework:** Django (Backend)
* **Desktop GUI:** Tkinter
* **Frontend:** HTML5, CSS3, Bootstrap
* **Algorithm:** Genetic Algorithm (Evolutionary Computation)

---

## 💻 Installation & Setup

This project can be run in two modes: as a **Web Application** or as a **Desktop Script**.

### Option 1: Run the Web Interface (Django)
*Recommended for the full experience.*

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/srav-athina/University-Scheduling-System.git](https://github.com/srav-athina/University-Scheduling-System.git)
    cd University-Scheduling-System
    ```

2.  **Navigate to the web application folder**
    ```bash
    cd "Honors Thesis/scheduler/LocalThesis"
    ```

3.  **Install Dependencies**
    ```bash
    pip install django
    ```

4.  **Run the Server**
    ```bash
    python manage.py runserver
    ```

5.  **Open in Browser**
    Go to: `http://127.0.0.1:8000`

---

### Option 2: Run the Desktop / Terminal App
*For testing the core algorithm logic locally.*

1.  **Navigate to the script folder**
    ```bash
    cd "Honors Thesis/scheduler"
    ```

2.  **Run the Desktop GUI**
    ```bash
    python tkinter_driver.py
    ```

3.  **OR Run the Terminal Script**
    ```bash
    python driver.py
    ```

---

## ⚙️ How It Works (The Algorithm)

The core of this system uses a **Genetic Algorithm** to find the best schedule:

1.  **Population Initialization:** Randomly generates a set of schedules.
2.  **Fitness Calculation:** Each schedule is "graded" based on the number of conflicts (fewer conflicts = higher score).
3.  **Crossover:** Swaps parts of two high-scoring schedules to create a new "offspring" schedule.
4.  **Mutation:** Randomly changes a class time or room to prevent getting stuck in local optima.
5.  **Evolution:** Repeats this process over hundreds of generations until a conflict-free schedule is found.

## 👤 Author

**Sravanthi** *Completed as an Undergraduate Honors Thesis.*
