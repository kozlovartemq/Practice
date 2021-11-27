alp = list("abcdefghijklmnopqrstuvwxyz")
ReAlp = alp[::-1]
d = list(input().lower())
msg = []
for i in range(len(d)):
    if d[i] == ' ':
        g = ' '
    else:
        g = ReAlp[alp.index(d[i])]  # list.index(arg) returns the index of the arg in the list 
    msg.append(g)
res = ''.join(msg)
print(res)
