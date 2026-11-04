def unique_elements(spisok):
    result = []
    for elem in spisok:
        if isinstance(elem, list):
            for pod_elem in unique_elements(elem):
                if pod_elem not in result:
                    result.append(pod_elem)
        else:
            if elem not in result:
                result.append(elem)
    return result

list_a = [1, 24, 2, [1, 8, 18] , 5, [62, [10, [12], 14, [20, 32, 17]]]]


print(f"Вывод уникальных элементов: {unique_elements(list_a)}")
