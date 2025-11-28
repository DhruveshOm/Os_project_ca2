# 🧠 Intelligent CPU Scheduler Simulator

This project is an interactive web-based simulator that visualizes how classic CPU scheduling algorithms work in real time.  
It allows users to input process details, generate dynamic Gantt charts, and compare key performance metrics across algorithms.

## ✨ Features
- Real-time simulation of **FCFS**, **SJF**, **Round Robin**, and **Priority Scheduling**
- Auto-generated **Gantt charts**, tables, and performance insights
- Dynamic recommendation of the most efficient algorithm based on waiting time
- Side-by-side comparison of all algorithms using visual graphs
- Clean interface powered by Streamlit for easy interaction

## 🔍 How It Works
Users provide arrival time, burst time, priorities (if needed), and time quantum (for RR).  
The simulator then:
1. Runs the scheduling algorithm  
2. Generates Gantt chart + metrics  
3. Re-runs all algorithms in the background  
4. Suggests which algorithm is optimal for the given workload  

## 📊 Algorithms Implemented
- **FCFS (First Come First Serve)**
- **SJF (Shortest Job First)**
- **Round Robin**
- **Priority Scheduling**

## 🖼️ Outputs Generated
- Interactive Gantt Chart  
- Average Waiting & Turnaround Times  
- Algorithm Comparison Bar Graph  
- Recommended Algorithm Indicator  

## 🚀 Running the Project
