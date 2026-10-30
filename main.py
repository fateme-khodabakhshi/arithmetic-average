# https://github.com/fateme-khodabakhshi/arithmetic-average

def average(numbers):
    return sum(numbers) / len(numbers)


while True:
    try:
        numbers = list(map(float, input().split()))

        if not numbers:
            raise ValueError

        print(f"{average(numbers):.2f}")
        break

    except ValueError:
        print("Invalid Input! Enter a valid input.")
