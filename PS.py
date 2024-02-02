def priority_scheduling(processes):
    processes.sort(key=lambda x: x[2], reverse=True)  # Sort processes based on priority in descending order

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
processes = [(0, 5, 3), (2, 3, 1), (4, 1, 4), (5, 4, 2)]
completion, waiting, avg_waiting = priority_scheduling(processes)
print("Completion Time:", completion)
print("Waiting Time:", waiting)
print("Average Waiting Time:", avg_waiting)
