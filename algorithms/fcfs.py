def fcfs(processes):
    processes.sort(key=lambda x: x['arrival'])
    time = 0
    gantt = []
    waiting_times = []
    turnaround_times = []

    for p in processes:
        start = max(time, p['arrival'])
        end = start + p['burst']
        gantt.append((p['id'], start, end))

        
        waiting = start - p['arrival']
        turnaround = end - p['arrival']
        waiting_times.append(waiting)
        turnaround_times.append(turnaround)
        time = end

    avg_waiting = sum(waiting_times) / len(processes)
    avg_turnaround = sum(turnaround_times) / len(processes)

    return gantt, avg_waiting, avg_turnaround
