Msequence = []

def collatz_algorithm(x):
    sequence = [x]
    Msequence.append(x)

    while x > 1:

        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1

        if x in Msequence:
            print("This ain't beating the Collatz Conjecture, I'm sorry.")
            break

        sequence.append(x)
        Msequence.append(x)

    return sequence


def stoof():
    x = int(input("Pick a number: "))
    result = collatz_algorithm(x)

    print(f"Sequence for {x}: {result}")
    print(f"Total steps to reach 1: {len(result)}")
    stoof()


stoof()
