def priority_scheduling_preemptive(processes):
    processes.sort(key=lambda x: (x[1], x[3]))

    time = 0
    completion_time = [0] * len(processes)
    remaining_time = [process[2] for process in processes]

    while True:
        highest_priority_index = -1
        for i in range(len(processes)):
            if processes[i][1] <= time and remaining_time[i] > 0:
                if highest_priority_index == -1 or processes[i][3] < processes[highest_priority_index][3]:
                    highest_priority_index = i

        if highest_priority_index == -1:
            break

        remaining_time[highest_priority_index] -= 1
        time += 1

        if remaining_time[highest_priority_index] == 0:
            completion_time[highest_priority_index] = time

    waiting_time = [completion_time[i] - processes[i][1] - processes[i][2] for i in range(len(processes))]
    return completion_time, waiting_time


if __name__ == "__main__":
    processes_list = [
        [1, 0, 1, 2],
        [2, 1, 7, 6],
        [3, 2, 3, 3],
        [4, 3, 6, 5],
        [5, 4, 5, 4],
        [6, 5, 15, 10],
        [7, 15, 8, 9]
    ]

    completion_time_p, waiting_time_p = priority_scheduling_preemptive(processes_list)

    print("Priority Scheduling (Preemptive) Schedule:")
    print("| Process ID | Arrival Time | Burst Time | Priority | Completion Time | Waiting Time |")
    for i in range(len(processes_list)):
        print(
            f"| {processes_list[i][0]}           | {processes_list[i][1]}             | {processes_list[i][2]}          | {processes_list[i][3]}       | {completion_time_p[i]}                 | {waiting_time_p[i]}             |")
