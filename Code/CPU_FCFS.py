def fcfs(processes):
    processes.sort(key=lambda x: x[1])

    completion_time = [0] * len(processes)
    completion_time[0] = processes[0][1] + processes[0][2]

    for i in range(1, len(processes)):
        completion_time[i] = max(completion_time[i - 1], processes[i][1]) + processes[i][2]

    turn_around_time = [completion_time[i] - processes[i][1] for i in range(len(processes))]
    waiting_time = [completion_time[i] - processes[i][1] - processes[i][2] for i in range(len(processes))]
    return completion_time, waiting_time, turn_around_time


if __name__ == "__main__":
    processes_list = [
        # [Process ID, Arrival Time, Burst Time]
        [1, 0, 2],
        [2, 1, 2],
        [3, 5, 3],
        [4, 6, 4]
    ]

    fcfs_completion_time, fcfs_waiting_time, fcfs_turn_around_time = fcfs(processes_list)

    print("FCFS Schedule:")
    print("| Process ID | Arrival Time | Burst Time | Completion Time | Turn Round Time| Waiting Time |")
    for i in range(len(processes_list)):
        print(
            f"| {processes_list[i][0]}           | {processes_list[i][1]}             | {processes_list[i][2]}          | {fcfs_completion_time[i]}                 |{fcfs_turn_around_time[i]}                 | {fcfs_waiting_time[i]}             |")
