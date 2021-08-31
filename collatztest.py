# Collatz sequence

def collatz(number):
    #even
    if number % 2 == 0:
        number = number // 2
        print(number)
        return number
    #odd
    elif number % 2 == 1:
        number = 3*number+1
        print(number)
        return number

print("Enter an integer:")
number = int(input())

while number > 1:
    number = collatz(number)
    if number != 1:
        continue
    if number == 1:
        break
