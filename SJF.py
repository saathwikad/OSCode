def sjf(processes):
    processes.sort(key=lambda x: x[1])  # Sort processes based on burst time

    completion_time = [0] * len(processes)
    waiting_time = [0] * len(processes)

    completion_time[0] = processes[0][1]
    for i in range(1, len(processes)):
        completion_time[i] = completion_time[i - 1] + processes[i][1]

    waiting_time[0] = 0
    for i in range(1, len(processes)):
        waiting_time[i] = completion_time[i - 1]

    average_waiting_time = sum(waiting_time) / len(processes)
    return completion_time, waiting_time, average_waiting_time

# Example usage
processes = [(0, 5), (2, 3), (4, 1), (5, 4)]
completion, waiting, avg_waiting = sjf(processes)
print("Completion Time:", completion)
print("Waiting Time:", waiting)
print("Average Waiting Time:", avg_waiting)
