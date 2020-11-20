# write a program that collects two numbers from 1-10
# determine if a number is even odd or prime.

import random as x


class RandomNumber:
    def no_picked(self):
        first_number = x.randint(1, 10)
        second_number = x.randint(1, 10)
        return first_number, second_number


chosen_numbers = RandomNumber()
a = chosen_numbers.no_picked()
print(a)
u, v = a
print()
print(f"{u} is the first chosen number; while  {v}  is the second chosen number")
# u = int(u)
# v = int(v)
print()
print()


def prime_number(no_):
    no_ = int(no_)
    if no_ > 1:
        for y in range(2, no_):
            if (no_ % y) == 0:
                print(f'{no_} is NOT a PRIME number')
                break
            else:
                print(f"{no_} is a PRIME number")
                break
    else:
        print(f"{no_} is NOT a PRIME number")


def odd_number(no_):
    no_ = int(no_)
    if (no_ % 2) == 0:
        print(no_, 'is an EVEN number')
    else:
        print(no_, 'is an ODD number')


def check_number_status():
    while True:
        no_ = input("Type in a number: ")
        try:
            prime_number(no_)
            odd_number(no_)
        except ValueError:
            print('Not a valid input. please enter a number')

        continue


check_number_status()
