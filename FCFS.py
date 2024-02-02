def fcfs(processes):
    arrival_time = [process[0] for process in processes]
    burst_time = [process[1] for process in processes]

    completion_time = [0] * len(processes)
    waiting_time = [0] * len(processes)

    completion_time[0] = burst_time[0]
    for i in range(1, len(processes)):
        completion_time[i] = completion_time[i - 1] + burst_time[i]

    waiting_time[0] = 0
    for i in range(1, len(processes)):
        waiting_time[i] = completion_time[i - 1] - arrival_time[i]

    average_waiting_time = sum(waiting_time) / len(processes)
    return completion_time, waiting_time, average_waiting_time

# Example usage
processes = [(0, 5), (2, 3), (4, 1), (5, 4)]
completion, waiting, avg_waiting = fcfs(processes)
print("Completion Time:", completion)
print("Waiting Time:", waiting)
print("Average Waiting Time:", avg_waiting)
