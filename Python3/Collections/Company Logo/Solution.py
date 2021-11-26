from collections import Counter as c

if __name__ == '__main__':
    """ Using collections """
    #d = c(input()).most_common(3)
    d = c(input())                                            # Creating a Counter
    sort = sorted(d.items(), key= lambda x: (-x[1],x[0]))[:3] # Sorting by value by desc, and key by asc
    p = d[0]
    p2 = d[1]
    p3 = d[2]
    print(str(p[0])+ ' ' + str(p[1]))
    print(str(p2[0])+ ' ' + str(p2[1]))
    print(str(p3[0])+ ' ' + str(p3[1]))
    
    
    """ Without using collections """
    
    s = input()
    a = 'abcdefghijklmnopqrstuvwxyz'
    d = {}                                                      # Creating a dictionary (словарь) - key:value
    for i in a:
        d[i] = s.count(i)                                       # Filling the dictionary (letter:amount)
    d = {i:d[i] for i in d if d[i]!=0}                          # Deleting letters with amount = 0
    sort = sorted(d.items(), key=lambda x: x[1], reverse=True)  # Creating a sorted list of dict elements
    p = sort[0]                                                 # d.items() = [('a', 1), ('b', 2), ('c', 3)]
    p2 = sort[1]                                                # key - how to sort (lambda x: x[1]) - use second group values of d.items() by in ascending order
    p3 = sort[2]                                                # reverse=True - in descending order
    print(str(p[0])+ ' ' + str(p[1]))                           # Printing the three most common characters
    print(str(p2[0])+ ' ' + str(p2[1]))
    print(str(p3[0])+ ' ' + str(p3[1]))
