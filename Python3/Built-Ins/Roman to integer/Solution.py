class Solution:
    
    def romanToInt(self, s: str) -> int:
        index_array = []                          #  list of indexes of "two-element" numbers
        sum_array = []                            #  list of integers
       
        def add_wrong_indexes(i: int) -> None:
            index_array.append(i)
            index_array.append(i+1)
        
        for i in range(len(s)-1):                 #  finding the "two-element" numbers
            if s[i] == "I" and s[i+1] == "V":
                add_wrong_indexes(i)
                sum_array.append(4)
            if s[i] == "I" and s[i+1] == "X":
                add_wrong_indexes(i)
                sum_array.append(9)
            if s[i] == "X" and s[i+1] == "L":
                add_wrong_indexes(i)
                sum_array.append(40)
            if s[i] == "X" and s[i+1] == "C":
                add_wrong_indexes(i)
                sum_array.append(90)
            if s[i] == "C" and s[i+1] == "D":
                add_wrong_indexes(i)
                sum_array.append(400)
            if s[i] == "C" and s[i+1] == "M":
                add_wrong_indexes(i)
                sum_array.append(900)
        for i in [indx for indx in range(len(s)) if indx not in index_array]: #  finding the "one-element" numbers
            if s[i] == "I":
                sum_array.append(1)
            if s[i] == "V":
                sum_array.append(5)
            if s[i] == "X":
                sum_array.append(10)
            if s[i] == "L":
                sum_array.append(50)
            if s[i] == "C":
                sum_array.append(100)
            if s[i] == "D":
                sum_array.append(500)
            if s[i] == "M":
                sum_array.append(1000) 
        return sum(sum_array)
                
