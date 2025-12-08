def median(lst):
    lst_sorted = sorted(lst)
    n = len(lst_sorted)
    mid = n//2
    if n % 2 == 0:
        return (lst_sorted[mid-1] + lst_sorted[mid])/2
    else:
        return lst_sorted[mid]
    