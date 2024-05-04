def sjf(processes):
    # processes = [process, arrival, buzze]

    processes.sort(key=lambda x: (x[1], x[2]))

    completion_time = [0] * len(processes)
    completion_time[0] = processes[0][1] + processes[0][2]

    for i in range(1, len(processes)):
        completion_time[i] = completion_time[i - 1] + processes[i][2]

    turn_around_time = [completion_time[i] - processes[i][1] for i in range(len(processes))]
    waiting_time = [turn_around_time[i] - processes[i][2] for i in range(len(processes))]
    return completion_time, waiting_time, turn_around_time


if __name__ == "__main__":
    processes_list = [
        [1, 1, 3],
        [2, 2, 4],
        [3, 1, 2],
        [4, 4, 4]
    ]

    sjf_completion_time, sjf_waiting_time, sjf_turn_time = sjf(processes_list)

    print("SJF Schedule:")
    print("| Process ID | Arrival Time | Burst Time | Completion Time|Turn Around Time | Waiting Time |")
    for i in range(len(processes_list)):
        print(
            f"| {processes_list[i][0]}           | {processes_list[i][1]}             | {processes_list[i][2]}          | {sjf_completion_time[i]}          |{sjf_turn_time[i]}                | {sjf_waiting_time[i]}             |")
