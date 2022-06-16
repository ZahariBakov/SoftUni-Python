words = input().split()
palindrome_word = input()
palindrome_list = []

for i in words:
    if i[::-1] == i:
        palindrome_list.append(i)

count = words.count(palindrome_word)

print(palindrome_list)
print(f"Found palindrome {count} times")
