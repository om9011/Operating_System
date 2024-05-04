def increase_avaliable(available_resources, new_free_resources):
    return [available_resources[i] + new_free_resources[i] for i in range(len(available_resources))]


def bankers(allocated_resources, max_demand_resources, available_resources):
    remaining_need = []
    process = 0
    remember_squence = {}
    safe_sequence = []
    while (process < len(allocated_resources)):
        need = [max_demand_resources[process][i] - allocated_resources[process][i] for i in
                range(len(allocated_resources[process]))]
        remaining_need.append(need)
        remember_squence[process] = need
        process += 1

    remaining_need_new = sorted(remaining_need)

    for process in remaining_need_new:
        if process <= available_resources:
            for key, val in remember_squence.items():
                if val == process:
                    process_id = key
                    available_resources = increase_avaliable(available_resources, allocated_resources[process_id])
                    safe_sequence.append(process_id + 1)

        else:
            print("Deadlock")

    print(allocated_resources,
          max_demand_resources,
          safe_sequence, sep="\n")


if __name__ == "__main__":
    # Example allocation matrix
    allocated_resources = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    # Example maximum demand matrix
    max_demand_resources = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]

    # Example available resources
    available_resources = [3, 3, 2]

    bankers(allocated_resources, max_demand_resources, available_resources)