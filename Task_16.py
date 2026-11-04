def ploskost(lst):
    idx = 0
    while idx < len(lst):
        if isinstance(lst[idx], list):
            ploskost(lst[idx])
            lst[idx:idx+1] = lst[idx]
        else:
            idx += 1  
    return lst


list_a = [1, 8, [20, 11, 2], [7, [19, [14, 5, 2], 12, [34]]]]
print(f"Cписок до: {list_a}")

print(f"Список после: {ploskost(list_a)}")