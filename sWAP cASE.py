def swap_case(s):
    new_list = []
    for i in s:
        if i.isupper():
            new_list.append(i.lower())
        elif i.islower():
            new_list.append(i.upper())
        else:
            new_list.append(i)

    return "".join(new_list)

if name == 'main':
    s = input()
    result = swap_case(s)
    print(result)