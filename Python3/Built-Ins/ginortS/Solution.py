s = input()
lower = ''                          # Creating needed strings
upper = ''
chet = ''
nechet = ''
for i in range(len(s)):             # Filling strings
    if s[i].islower():
        lower = lower+s[i]
for i in range(len(s)):
    if s[i].isupper():
        upper = upper+s[i]
for i in range(len(s)):
    if s[i].isdigit():              # Filling strings with even and odd digits
        if int(s[i]) % 2 == 0:          
            chet = chet+s[i]
        else: nechet = nechet + s[i]       
print(''.join(sorted(lower)) + ''.join(sorted(upper)) + ''.join(sorted(nechet)) + ''.join(sorted(chet)))
                                    # Printing strings (strings including letters sorted alphabetically,
                                                      # strings including digits sorted by ascending)
