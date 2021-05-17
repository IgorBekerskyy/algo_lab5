import os


def read(file):
    with open(file, 'r') as input_file:
        data = input_file.readlines()
    return data


def write(result, file_name):
    try:
        os.remove(file_name + ".out")
    except FileNotFoundError:
        pass
    with open(file_name + '.out', "a", ) as f:
        f.write("Indexes of pattern : ")
        for i in range(len(result)):
            f.write(str(result[i]))
            f.write(str(','))
        f.close()