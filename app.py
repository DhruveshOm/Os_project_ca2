import streamlit as st
from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from algorithms.round_robin import round_robin
from algorithms.priority import priority_scheduling
from utils.gantt_chart import plot_gantt
from copy import deepcopy
import plotly.graph_objects as go

st.set_page_config(
    page_title="🧠 Intelligent CPU Scheduler Simulator",
    layout="centered",
    page_icon="🧠"
)

st.markdown("""
    <h1 style='text-align: center; color: #4A90E2;'>🧠 Intelligent CPU Scheduler Simulator</h1>
    <p style='text-align: center;'>Simulate classic CPU scheduling algorithms with real-time Gantt charts and performance metrics</p>
""", unsafe_allow_html=True)
st.divider()
tq = 2

with st.sidebar:
    st.title("⚙️ Settings")
    algo = st.selectbox("📊 Select Algorithm", ["FCFS", "SJF", "Round Robin", "Priority Scheduling"])
    num = st.slider("🕧 Number of Processes", min_value=1, max_value=10, value=3)
    if algo == "Round Robin":
        tq = st.number_input("⏱️ Time Quantum", min_value=1, max_value=10, value=2)

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

st.divider()

if 'show_comparison' not in st.session_state:
    st.session_state.show_comparison = False

if st.button("🚀 Run Scheduling Simulation", use_container_width=True):
    if algo == "FCFS":
        gantt, avg_wt, avg_tt = fcfs(processes)
    elif algo == "SJF":
        gantt, avg_wt, avg_tt = sjf(processes)
    elif algo == "Round Robin":
        gantt, avg_wt, avg_tt = round_robin(processes, tq)
    elif algo == "Priority Scheduling":
        gantt, avg_wt, avg_tt = priority_scheduling(processes)

    st.subheader("📅 Gantt Chart")
    plot_gantt(gantt)

    st.subheader("📈 Performance Metrics")
    col1, col2 = st.columns(2)
    col1.metric("⏳ Avg Waiting Time", f"{avg_wt:.2f} units")
    col2.metric("🔁 Avg Turnaround Time", f"{avg_tt:.2f} units")

    st.markdown("### 📜 Gantt Chart Breakdown")
    st.table([{"Process": f"P{pid}", "Start": start, "End": end} for pid, start, end in gantt])

    st.success("✅ Simulation completed successfully!")

    st.divider()
    st.subheader("🧐 Recommended Algorithm")

    proc_fcfs = deepcopy(processes)
    proc_sjf = deepcopy(processes)
    proc_rr = deepcopy(processes)
    proc_prio = deepcopy(processes)

    _, w_fcfs, _ = fcfs(proc_fcfs)
    _, w_sjf, _ = sjf(proc_sjf)
    _, w_rr, _ = round_robin(proc_rr, tq)
    _, w_prio, _ = priority_scheduling(proc_prio)

    best_algo_map = {
        "FCFS": w_fcfs,
        "SJF": w_sjf,
        "Round Robin": w_rr,
        "Priority Scheduling": w_prio
    }

    best_algorithm = min(best_algo_map, key=best_algo_map.get)
    best_value = best_algo_map[best_algorithm]

    st.success(f"✅ Based on your current process data, the recommended algorithm is **{best_algorithm}** with the lowest average waiting time of **{best_value:.2f} units**.")

    st.session_state.show_comparison = True

if st.session_state.show_comparison:
    st.subheader("📊 Compare All Scheduling Algorithms")

    _, w_fcfs, t_fcfs = fcfs(deepcopy(processes))
    _, w_sjf, t_sjf = sjf(deepcopy(processes))
    _, w_rr, t_rr = round_robin(deepcopy(processes), tq)
    _, w_prio, t_prio = priority_scheduling(deepcopy(processes))

    algorithms = ["FCFS", "SJF", "Round Robin", "Priority Scheduling"]
    avg_waiting_times = [w_fcfs, w_sjf, w_rr, w_prio]
    avg_turnaround_times = [t_fcfs, t_sjf, t_rr, t_prio]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=algorithms,
        y=avg_waiting_times,
        name='Avg Waiting Time',
        marker_color='indigo'
    ))
    fig.add_trace(go.Bar(
        x=algorithms,
        y=avg_turnaround_times,
        name='Avg Turnaround Time',
        marker_color='orange'
    ))

    fig.update_layout(
        barmode='group',
        title='📊 Algorithm Comparison',
        xaxis_title='Scheduling Algorithm',
        yaxis_title='Time (units)',
        legend_title='Metric',
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    st.session_state.show_comparison = False
