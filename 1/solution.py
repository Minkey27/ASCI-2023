def main():
    with open("1/input.txt", "r") as f:
        # read input from file
        input_data = f.readlines()

    highest_amount_workload = current_worker_load = 0
    for line in input_data:
        if line == "\n":
            if current_worker_load > highest_amount_workload:
                highest_amount_workload = current_worker_load
            current_worker_load = 0
        else:
            current_worker_load += int(line)

    print(highest_amount_workload)


if __name__ == "__main__":
    main()
