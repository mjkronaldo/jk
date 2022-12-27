def Cumulative_sum(lists):   
    cum_list = []   
    lenlength = len(lists)   
    cum_list = [sum(lists[0:x:1]) for x in range(0, length+1)]   
    return cum_list[1:]  
  
lists = [10, 15, 20, 25, 30]   
print (Cumulative_sum(lists))  