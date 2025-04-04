import matplotlib.pyplot as plt
import streamlit as st

def plot_gantt(gantt):
    fig, ax = plt.subplots()
    for task in gantt:
        ax.broken_barh([(task[1], task[2] - task[1])], (10, 9),
                       facecolors=('tab:blue'))
        ax.text(task[1] + (task[2] - task[1]) / 2, 14, f"P{task[0]}", ha='center')
    ax.set_ylim(5, 25)
    ax.set_xlim(0, gantt[-1][2] + 2)
    ax.set_xlabel("Time")
    ax.set_yticks([])
    ax.set_title("Gantt Chart")
    st.pyplot(fig)
