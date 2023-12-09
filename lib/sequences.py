#!/usr/bin/env python3

def print_fibonacci(length):
    
    if length == 0:
        print('[]')
        return 0

    if length == 1:
        print('[0]')
        return 0
    
    if length == 2:
        print('[0, 1]')
        return 0
    
    if length > 2:
        fib = [0, 1]
        for i in range(2, length):
            fib.append(fib[i-1] + fib[i-2])
        print(fib)
        return 0 
    pass