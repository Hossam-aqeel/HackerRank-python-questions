def split_and_join(line):
    list = line.split(" ")
    line = "-".join(list)
    return line

if name == 'main':
    line = input()
    result = split_and_join(line)
    print(result)