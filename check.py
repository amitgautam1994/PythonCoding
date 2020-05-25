def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        print(str(i).rjust(w," "), str(oct(i).lstrip("0o")).rjust(w," "), str(hex(i).lstrip("0x").capitalize()).rjust(w," "),  str(bin(i).lstrip("0b")).rjust(w," "))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)