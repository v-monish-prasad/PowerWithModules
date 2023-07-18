def powerWithModules(A, B, C):
    A %= C  # to make sure that the value is between the range 0 and C - 1 to handle larger values
    result = 1
    for i in range(B):
        result = (result * A) % C

    return result


if __name__ == "__main__":
    A = int(input())
    B = int(input())
    C = int(input())

    print(powerWithModules(A, B, C))
