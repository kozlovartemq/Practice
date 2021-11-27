s = list(input())                                                 # List() makes each character of a string as separate element
alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alpUP = alphabet.upper()
letters = alphabet.split()                                        # split() - makes a LIST from a string using separator (def. ' ')
lett2 = alpUP.split()
letters.append(' ')
letters = letters + lett2                                         # 'Join' lists
msg = []
for i in range(len(s)):                                           # Filling the 'msg' list with letters and ' ' only
    if s[i] in letters:
        msg.append(s[i])

print(''.join(msg[::-1]))                                         # [::-1] - In reverse order
