def priority_scheduling_non_preemptive(processes):
    processes.sort(key=lambda x: (x[3], x[1]))

    completion_time = [0] * len(processes)
    completion_time[0] = processes[0][1] + processes[0][2]

    for i in range(1, len(processes)):
        completion_time[i] = completion_time[i - 1] + processes[i][2]

    waiting_time = [completion_time[i] - processes[i][1] - processes[i][2] for i in range(len(processes))]
    return completion_time, waiting_time


if __name__ == "__main__":
    processes_list = [
        # [
        # [Process ID, Arrival Time, Burst Time, Priority]
        [1, 0, 3, 3],
        [2, 1, 6, 4],
        [3, 3, 1, 9],
        [4, 2, 2, 7],
        [5, 4, 4, 8]
    ]

    completion_time_np, waiting_time_np = priority_scheduling_non_preemptive(processes_list)

    print("Priority Scheduling (Non-Preemptive) Schedule:")
    print("| Process ID | Arrival Time | Burst Time | Priority | Completion Time | Waiting Time |")
    for i in range(len(processes_list)):
        print(
            f"| {processes_list[i][0]}           | {processes_list[i][1]}             | {processes_list[i][2]}          | {processes_list[i][3]}       | {completion_time_np[i]}                 | {waiting_time_np[i]}             |")
