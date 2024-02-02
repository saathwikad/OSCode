def round_robin(processes, time_quantum):
    queue = processes.copy()
    completion_time = [0] * len(processes)
    waiting_time = [0] * len(processes)

    time = 0
    while queue:
        process = queue.pop(0)
        if process[1] <= time_quantum:
            time += process[1]
            completion_time[process[2]] = time
        else:
            time += time_quantum
            queue.append((process[0], process[1] - time_quantum, process[2]))

    for i in range(len(processes)):
        waiting_time[i] = completion_time[i] - processes[i][1]

    average_waiting_time = sum(waiting_time) / len(processes)
    return completion_time, waiting_time, average_waiting_time

# Example usage
processes = [(0, 5), (2, 3), (4, 1), (5, 4)]
time_quantum = 2
completion, waiting, avg_waiting = round_robin(processes, time_quantum)
print("Completion Time:", completion)
print("Waiting Time:", waiting)
print("Average Waiting Time:", avg_waiting)
