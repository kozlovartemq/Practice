from collections import Counter as c

""" Using collections """

n = int(input())                      
words = c(input() for i in range(n))  # Creating a Counter
print(len(words))
for i in words.items():               # OR print(*words.values()) could've been used for Counter
    print(i[1], end=" ")              # instead of FOR

""" Without using collections """

n = input()
words = {}                   # Creating a dict
for i in range(int(n)):
    l = input()
    if l in words:
        words[l]+=1          # Adding +1 in values of a word, if repetition noticed
    else: words[l]=1         # Assign value = 1 of a word, if it's a first appearance
print(len(words))
for i in words:
    print(words[i], end=" ") # Printing a values of the dict with sep. " "
