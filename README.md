# **IITB Racing Autonomous: Path Planning & Controls Trainee Module**
---

## 🏎️ Who We Are

We are the Path Planning and Controls Subsystem (PPC) of **IITB Racing Driverless**, a student-led team that builds autonomous electric race cars.

Our goal is to enable our car to **race autonomously between blue and yellow cones**, **complete a lap in the shortest possible time**, and **avoid collisions with any cones**. To achieve this, we focus on designing algorithms that generate **optimal paths** and provide **precise controls** to follow them.

### 🧠 What We’ve Achieved So Far
- 🧩 **Delaunay Triangulation** for fast and smooth raceline generation  
- 🌀 **Optimized racelines** to reduce lap time  
- 🚗 **Pure Pursuit** and **Stanley Controllers** for tracking paths  
- 🔄 **Velocity profiling** based on curvature  

### 🔬 What We’re Currently Working On
- 🌳 **RRT (Rapidly-exploring Random Trees)** for real-time path planning in unknown maps  
- 🧠 **MPC (Model Predictive Control)** for generating optimal control actions considering dynamics  

<table>
  <tr>
    <td align="center"><b>Delaunay Triangulation</b></td>
    <td align="center"><b>RRT Path Planning</b></td>
    <td align="center"><b>MPC Optimal Control</b></td>
  </tr>
  <tr>
    <td><img src="assets/delaunay_example.png" width="300"/></td>
    <td><img src="assets/rrt_example.gif" width="300"/></td>
    <td><img src="assets/mpc_example.gif" width="300"/></td>
  </tr>
</table>

---

## 💡 Introduction to Path Planning and Control

**Path Planning and Control** is a critical subsystem that connects high-level perception with low-level actuation. It ensures that the autonomous race car not only knows **where to go** but also **how to get there** effectively and safely.

### 📌 Path Planning:
Generates a feasible and smooth trajectory based on the car’s position and the SLAM-generated map. We explore:
- Linear & spline interpolation  
- Delaunay triangulation  
- Curvature-based optimization  
- Algorithms like A*, RRT, and optimization-based planners  

### 📌 Controls:
Makes sure the car follows the planned trajectory by computing steering, throttle, and brake commands. We cover:
- PID controllers for speed tracking  
- Pure Pursuit and Stanley for steering  
- Advanced controllers like MPC that take vehicle dynamics into account  

Together, they allow our autonomous race car to drive dynamically and intelligently!

---

## 📝 Instructions

- Trainees are required to update the shared task sheet: **Module Progress**
- **Documentation is mandatory** for each checkpoint:
  - Create a Google Doc titled `PPC_Module_YourName`
  - Document your learnings, errors faced, and any doubts
  - Set sharing to **“anyone with the link”** and update the link in the task sheet
- Don’t hesitate to reach out to **JDEs/DEs** if you're stuck or curious
- Performance in this module will be used to judge your abilities and **assign subsystems** in the team
- Most importantly, **have fun while learning 🚀**

---

## 🧭 Module Overview

This module is designed to give you a foundational understanding of the key concepts in Path Planning and Control. It is divided into **two main parts**:

### 1. Path Planning
- 📍 Interpolation  
- 📈 Basic Optimization  
- ⚡ Velocity Profiling using Curvature
  
### 2. Controls
- 🔧 PID Control  
- 🚲 Bicycle Model  
- 🧭 Stanley Controller  

---

## ✅ Learning Outcomes

By the end of this module, you will be able to:
- Interpolate smooth trajectories from cone maps  
- Understand curvature and apply basic optimization principles to path smoothing  
- Build a velocity profile that respects physical constraints  
- Implement and tune a PID controller for velocity tracking  
- Understand the kinematic bicycle model  
- Implement a Stanley controller for path tracking  
- Simulate and animate your car following the trajectory using Matplotlib  

---

## 📅 Checkpoints

| Checkpoint | Topic                        | Deliverable                                |
|------------|------------------------------|--------------------------------------------|
| 📍 Checkpoint 1 | Interpolation     | Midline interpolation from cone map         |
| 📍 Checkpoint 2 | Optimization + Velocity Profile | Optimized path + velocity profile            |
| 📍 Checkpoint 3 | PID Control                  | Tuning + response using velocity profile    |
| 📍 Checkpoint 4 | Stanley Control              | Car tracking trajectory using Stanley       |

Each checkpoint includes a corresponding `.ipynb` file with:  
- Notes 📝  
- Assignments 🧪  
- Plots 📊  
- Animations 🎞️  

---
