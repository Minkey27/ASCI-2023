def get_number_repr_of_character(char):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96


def main():
    with open("3/input.txt", "r") as f:
        # read input from file
        input_data = f.readlines()

    counter = 0
    for line in input_data:
        # minus one to strip new line.
        line = line.strip()

        half_index = int(len(line) / 2)

        first_half = line[:half_index]
        last_half = line[half_index:]

        for letter in first_half:
            if letter in last_half:
                counter += get_number_repr_of_character(letter)
                # print(letter, first_half, last_half)
                break  # Stop at first match.

    print(counter)


if __name__ == "__main__":
    main()
