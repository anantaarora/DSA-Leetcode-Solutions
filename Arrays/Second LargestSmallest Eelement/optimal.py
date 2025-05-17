def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    small = float("inf")
    second_small = float("inf")
    large = float("-inf")
    second_large = float("-inf")

    for i in range(0, len(a)):
        if a[i] < small:
            second_small = small
            small = a[i]
        elif a[i] < second_small and a[i] != small:
            second_small = a[i]
        if a[i] > large:
            second_large = large
            large = a[i]
        elif a[i] > second_large and a[i] != large:
            second_large = a[i]

    return [second_large, second_small]