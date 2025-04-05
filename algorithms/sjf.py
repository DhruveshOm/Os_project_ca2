def sjf(processes):
    processes = sorted(processes, key=lambda x: (x['arrival'], x['burst']))
    n = len(processes)
    time = 0
    completed = 0
    gantt = []
    waiting_times = []
    turnaround_times = []
    visited = [False] * n

    while completed < n:
        idx = -1
        min_burst = float('inf')

        for i in range(n):
            if processes[i]['arrival'] <= time and not visited[i] and processes[i]['burst'] < min_burst:
                min_burst = processes[i]['burst']
                idx = i

        if idx == -1:
            time += 1
            continue

        p = processes[idx]
        start = time
        end = start + p['burst']
        gantt.append((p['id'], start, end))

        waiting = start - p['arrival']
        turnaround = end - p['arrival']
        waiting_times.append(waiting)
        turnaround_times.append(turnaround)

        visited[idx] = True
        completed += 1
        time = end

    
    avg_waiting = sum(waiting_times) / n
    avg_turnaround = sum(turnaround_times) / n

    return gantt, avg_waiting, avg_turnaround
