print('Enter a number for its collatz sequence: ')
num = int(input())

# Collatz sequence: if number is even, return number // 2
# if number is odd, return 3 * number + 1

while num != 1:
    if num % 2 == 0:
        num = num // 2
    else:
        num = 3 * num + 1

    print(num)
