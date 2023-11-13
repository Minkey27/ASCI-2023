def main():
    with open("2/input.txt", "r") as f:
        # read input from file
        input_data = f.readlines()

    valids = 0
    for line in input_data:
        # 3-6 e: leurrtgbeeur
        min_max, char, string = line.split()
        min, max = min_max.split("-")
        char = char[0]

        if string.count(char) < int(min) or string.count(char) > int(max):
            continue

        valids += 1

    print(valids)


if __name__ == "__main__":
    main()
