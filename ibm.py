def subsetA(arr):
    # Write your code here
    p = len(arr)-1
    sarr = sorted(arr)
    while sum(sarr[:p]) >= sum(sarr[p:]):
        p -= 1
        
    A = set(sarr[p:])
    B = set(sarr[:p])
    inter = A.intersection(B)
    
    if inter != set():
        while inter in sarr[:p]:
            p -= 1
    
    return sarr[p:] # this is Greedy so it doesn't work

