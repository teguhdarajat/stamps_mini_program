from mini_program import MiniProgram

if __name__ == "__main__":
    mini_program = MiniProgram(100)
    numbers = mini_program.get_numbers()
    print(numbers)
    for i in range(len(numbers)):
        print(numbers[i], end = " ")