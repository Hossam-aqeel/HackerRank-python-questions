def print_formatted(number):
    width = len(f"{number:b}")
    for num in range(1,number+1):
        decimal = f"{num:d}".rjust(width)
        octal = f"{num:o}".rjust(width)
        hexa = f"{num:X}".rjust(width)
        binary = f"{num:b}".rjust(width)
        print(decimal, octal, hexa, binary)
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)