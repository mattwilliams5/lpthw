#!/usr/local/bin/python3

# this one is like your scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# This just takes one argument

def print_one(arg1):
    print(f"arg1: {arg1}")

# This one takes no arguements
def print_none():
    print("I go nothin'.")


print_two("Matt", "Williams")
print_two_again("Matt", "Williams")
print_one("First!")
print_none()
