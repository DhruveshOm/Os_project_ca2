def round_robin(processes, quantum):
    from collections import deque

    processes = sorted(processes, key=lambda x: x['arrival'])
    queue = deque()
    n = len(processes)
    time = 0
    idx = 0
    gantt = []
    remaining = {p['id']: p['burst'] for p in processes}
    waiting_times = {}
    start_times = {}
    end_times = {}
    arrived = set()

    while True:
        while idx < n and processes[idx]['arrival'] <= time:
            queue.append(processes[idx])
            arrived.add(processes[idx]['id'])
            idx += 1

        
        if queue:
            p = queue.popleft()
            pid = p['id']
            if pid not in start_times:
                start_times[pid] = time

            execute_time = min(quantum, remaining[pid])
            gantt.append((pid, time, time + execute_time))
            time += execute_time
            remaining[pid] -= execute_time

            # Enqueue newly arrived during execution
            while idx < n and processes[idx]['arrival'] <= time:
                queue.append(processes[idx])
                arrived.add(processes[idx]['id'])
                idx += 1

            if remaining[pid] > 0:
                queue.append(p)
            else:
                end_times[pid] = time
                waiting_times[pid] = end_times[pid] - p['arrival'] - p['burst']
        else:
            if idx < n:
                time = processes[idx]['arrival']
            else:
                break

    turnaround_times = [end_times[p['id']] - p['arrival'] for p in processes]
    avg_waiting = sum(waiting_times.values()) / n
    avg_turnaround = sum(turnaround_times) / n

    return gantt, avg_waiting, avg_turnaround
