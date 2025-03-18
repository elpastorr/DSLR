import sys


def compare_data(our_file, correct_file):
    try:
        our_data = open(our_file, "r")
        correct_data = open(correct_file, "r")
    except Exception as e:
        print(e)
    nb_false = 0
    nb_lines = -1
    for our_line, correct_line in zip(our_data, correct_data):
        if our_line != correct_line:
            nb_false += 1
        nb_lines += 1
    print("Number of incorect guess: ", nb_false)
    print("Percentage of correct guess: ", (1 - nb_false / nb_lines) * 100)
    our_data.close()
    correct_data.close()


def main(sys_argv):
    if len(sys_argv) != 3:
        print("Error: wrong arg number\nUsage: python3 main.py our_data correct_data ")
        return
    try:
        compare_data(sys_argv[1], sys_argv[2])
    except Exception as e:
        print(e)
        return


if __name__ == "__main__":
    sys_argv = sys.argv
    main(sys_argv)
