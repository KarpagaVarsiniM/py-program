N = int(input("Enter a number: "))

if N == 0:
    print("***The number is neutral***")

elif N % 2 == 0:
    print("***The number is even***")

    V = N
    rev = 0

    while V > 0:
        rem = V % 10
        rev = rev * 10 + rem
        V = V // 10

    if rev == N:
        print("***The given number is a palindrome***")
    else:
        print("***The given number is not a palindrome***")

elif N % 2 != 0:
    print("***The number is odd***")

    fact = 1

    for i in range(N, 0, -1):
        fact *= i

    print("The factorial is:", fact)

    if N % 2 != 0:
        count = 0
        temp = abs(fact)

        if temp == 0:
            count = 1
        else:
            while temp != 0:
                temp = temp // 10
                count += 1

        print("The count is:", count)

