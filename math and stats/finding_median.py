#Q find mean & median of given icet ranks

def median_ranks(ranks):
    l_rank = len(ranks)
    sort = sorted(ranks)
    l = len(sort)//2
    if l_rank%2 == 0:                                          
        mid_val1 = int(l)
        mid_val2 = int(l-1) 
        print(sort)  
        median = (sort[mid_val1] + sort[mid_val2])/2
        print(f"Total ranks : {l_rank}")
        print(sort[mid_val1])
        print(sort[mid_val2])
        return f"The median value is: {median}"
    elif l_rank%2 != 0:
        return sort[int(l)]

ranks = [123, 756, 867, 768, 545, 565, 354, 1, 90, 76, 45, 976, 856, 537, 953, 12, 8643, 6366]
print(median_ranks(ranks))
