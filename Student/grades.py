def Avg(grades):
    return sum(grades)/len(grades)

def Max(grades):
    biggest=grades[0]

    for grade in grades:
        if grade>biggest:
            biggest=grade

    return biggest

def Min(grades):
    smallest=grades[0]

    for grade in grades:
        if grade<smallest:
            smallest=grade

    return smallest