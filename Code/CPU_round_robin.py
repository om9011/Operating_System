def round_robin(processes, time_quantum):
    ready_queue = []
    time = 0
    completion_time = [0] * len(processes)
    burst_time = [processes[i][2] for i in range(len(processes))]
    prev_process = None

    while True:
        # All processes have arrived but not completed then put it in ready_queue
        for process in processes:
            if process[1] <= time and process not in ready_queue and process[2] > 0 and process is not prev_process:  # [p1, p2, p3, p1, p4, p2, p1,]
                ready_queue.append(process)

        if prev_process is not None and prev_process[2] > 0 and prev_process not in ready_queue:
            ready_queue.append(prev_process)

        if not ready_queue:
            break

        current_process = ready_queue.pop(0)  # expected p2, but getiing p1

        if current_process[2] > time_quantum:
            time += time_quantum
            current_process[2] -= time_quantum
            prev_process = current_process
        else:
            time += current_process[2]
            current_process[2] = 0
            completion_time[current_process[0] - 1] = time
        print(ready_queue)

    turn_time = [completion_time[i] - processes[i][1] for i in range(len(processes))]
    waiting_time = [turn_time[i] - burst_time[i] for i in range(len(processes))]
    return completion_time, waiting_time, turn_time


if __name__ == "__main__":
    processes_list = [
        # [Process ID, Arrival Time, Burst Time]
        [1, 0, 5],
        [2, 1, 4],
        [3, 2, 2],
        [4, 4, 1]
    ]

    time_quantum = 2
    rr_completion_time, rr_waiting_time, turn = round_robin(processes_list, time_quantum)

    print(f"Round Robin ({time_quantum} time quantum) Schedule:")
    print("| Process ID | Arrival Time | Burst Time | Completion Time| Turn Aruond  | Waiting Time |")
    for i in range(len(processes_list)):
        print(
            f"| {processes_list[i][0]}           | {processes_list[i][1]}             | {processes_list[i][2]}          | {rr_completion_time[i]}                 | {turn[i]}                 | {rr_waiting_time[i]}             |")
