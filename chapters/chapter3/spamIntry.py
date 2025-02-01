def spam(divideBy):
    return 42 / divideBy
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))     # never executed because once the execution jumps to teh code in the except clause it does not return to the try clause
except ZeroDivisionError:
    print('Error: Invalid argument.')