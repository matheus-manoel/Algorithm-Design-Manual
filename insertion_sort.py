def insertion_sort(string):
    str_lst = list(string)
    str_len = len(str_lst)
    
    for i in range(0, str_len):
        j = i
        
        while j>0 and str_lst[j] < str_lst[j-1]:
            str_lst[j], str_lst[j-1] = str_lst[j-1], str_lst[j]
            j = j - 1
            
    return str(str_lst)
        
print(insertion_sort("INSERTIONSORT"))
