import os

file = 'removed_file.txt'

try:
    os.remove('removed_file.txt')
    print("File removed")
except FileNotFoundError:
    print("File already deleted!")
