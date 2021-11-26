n, m = map(int, input().split()) # map(func, *iterables) - Computes the function using arguments from each of the iterables
array = input().split()          # split() - Return a LIST of the words in the STRING, def. sep. is ' '   
a = input().split()              # a is a LIST []
a = set(a)                       # a is a SET {} - no repeated unordered elements
b = input().split()
b = set(b)
Happiness = 0
for i in range(n):
    if array[i] in a:
        Happiness  += 1
    if array[i] in b:
        Happiness  -= 1
print(Happiness)
