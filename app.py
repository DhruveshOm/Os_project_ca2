# import streamlit as st
# from algorithms.fcfs import fcfs
# from algorithms.sjf import sjf
# from algorithms.round_robin import round_robin
# from algorithms.priority import priority_scheduling
# from utils.gantt_chart import plot_gantt

# st.set_page_config(page_title="CPU Scheduler Simulator", layout="centered")
# st.title("🧠 Intelligent CPU Scheduler Simulator")

# algo = st.selectbox("📊 Select Scheduling Algorithm", ["FCFS", "SJF", "Round Robin", "Priority Scheduling"])
# num = st.number_input("🔢 Number of Processes", min_value=1, max_value=10, value=3)

# st.markdown("---")

# processes = []

# for i in range(num):
#     st.subheader(f"Process {i+1}")
#     arrival = st.number_input(f"Arrival Time (P{i+1})", min_value=0, key=f"a{i}")
#     burst = st.number_input(f"Burst Time (P{i+1})", min_value=1, key=f"b{i}")
#     priority = 0
#     if algo == "Priority Scheduling":
#         priority = st.number_input(f"Priority (Lower = Higher) (P{i+1})", min_value=0, key=f"p{i}")
#     processes.append({'id': i+1, 'arrival': arrival, 'burst': burst, 'priority': priority})

# st.markdown("---")

# if algo == "Round Robin":
#     time_quantum = st.number_input("⏱️ Time Quantum", min_value=1, max_value=10, value=2)

# if st.button("🚀 Run Scheduler"):
#     if algo == "FCFS":
#         gantt, avg_wt, avg_tt = fcfs(processes)
#     elif algo == "SJF":
#         gantt, avg_wt, avg_tt = sjf(processes)
#     elif algo == "Round Robin":
#         gantt, avg_wt, avg_tt = round_robin(processes, time_quantum)
#     elif algo == "Priority Scheduling":
#         gantt, avg_wt, avg_tt = priority_scheduling(processes)

#     st.subheader("📅 Gantt Chart")
#     plot_gantt(gantt)

#     st.subheader("📈 Performance Metrics")
#     st.write(f"**Average Waiting Time:** `{avg_wt:.2f}`")
#     st.write(f"**Average Turnaround Time:** `{avg_tt:.2f}`")

#     st.markdown("### 🧾 Gantt Chart Data")
#     st.table([{"Process": f"P{pid}", "Start": start, "End": end} for pid, start, end in gantt])



import streamlit as st
from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from algorithms.round_robin import round_robin
from algorithms.priority import priority_scheduling
from utils.gantt_chart import plot_gantt

st.set_page_config(
    page_title="🧠 Intelligent CPU Scheduler Simulator",
    layout="centered",
    page_icon="🧠"
)

# -------------------------------
# Title & Intro
# -------------------------------
st.markdown("""
    <h1 style='text-align: center; color: #4A90E2;'>🧠 Intelligent CPU Scheduler Simulator</h1>
    <p style='text-align: center;'>Simulate classic CPU scheduling algorithms with real-time Gantt charts and performance metrics</p>
""", unsafe_allow_html=True)

st.divider()

# -------------------------------
# Sidebar: Algorithm Selector
# -------------------------------
with st.sidebar:
    st.title("⚙️ Settings")
    algo = st.selectbox("📊 Select Algorithm", ["FCFS", "SJF", "Round Robin", "Priority Scheduling"])
    num = st.slider("🔢 Number of Processes", min_value=1, max_value=10, value=3)

    if algo == "Round Robin":
        tq = st.number_input("⏱️ Time Quantum", min_value=1, max_value=10, value=2)

# -------------------------------
# Process Input Table
# -------------------------------
st.subheader("📝 Enter Process Details")

processes = []
cols = st.columns([1, 1, 1, 1]) if algo == "Priority Scheduling" else st.columns([1, 1, 1])

for i in range(num):
    with cols[0]:
        arrival = st.number_input(f"Arrival (P{i+1})", min_value=0, key=f"arr{i}")
    with cols[1]:
        burst = st.number_input(f"Burst (P{i+1})", min_value=1, key=f"burst{i}")
    with cols[2]:
        if algo == "Priority Scheduling":
            priority = st.number_input(f"Priority (P{i+1})", min_value=0, key=f"prio{i}")
        else:
            priority = 0
    processes.append({'id': i+1, 'arrival': arrival, 'burst': burst, 'priority': priority})

# -------------------------------
# Run Scheduler
# -------------------------------
st.divider()

if st.button("🚀 Run Scheduling Simulation", use_container_width=True):
    if algo == "FCFS":
        gantt, avg_wt, avg_tt = fcfs(processes)
    elif algo == "SJF":
        gantt, avg_wt, avg_tt = sjf(processes)
    elif algo == "Round Robin":
        gantt, avg_wt, avg_tt = round_robin(processes, tq)
    elif algo == "Priority Scheduling":
        gantt, avg_wt, avg_tt = priority_scheduling(processes)

    # -------------------------------
    # Display Results
    # -------------------------------
    st.subheader("📅 Gantt Chart")
    plot_gantt(gantt)

    st.subheader("📈 Performance Metrics")
    col1, col2 = st.columns(2)
    col1.metric("⏳ Avg Waiting Time", f"{avg_wt:.2f} units")
    col2.metric("🔁 Avg Turnaround Time", f"{avg_tt:.2f} units")

    st.markdown("### 📋 Gantt Chart Breakdown")
    st.table([{"Process": f"P{pid}", "Start": start, "End": end} for pid, start, end in gantt])

    st.success("✅ Simulation completed successfully!")

