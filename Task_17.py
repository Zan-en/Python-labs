def sliyanie(slov1, slov2):
    for kluch, znach in slov2.items():
        if kluch in slov1:
            if isinstance(slov1[kluch], dict) and isinstance(znach, dict):
                sliyanie(slov1[kluch], znach)
            elif isinstance(slov1[kluch], set) and isinstance(znach, set):
                slov1[kluch].update(znach)
            elif isinstance(slov1[kluch], list) and isinstance(znach, list):
                slov1[kluch].extend(znach)
            elif isinstance(slov1[kluch], tuple) and isinstance(znach, tuple):
                slov1[kluch] += znach
            else: 
                slov1[kluch] = znach
        else:
            slov1[kluch] = znach

slov_1 = { "a": 1, "b": {"c": 1, "f": [4], "k": (8)}}  
slov_2 = { "d": 1, "b": {"c": 2, "e": [3], "j": (2)}}

sliyanie(slov_1, slov_2)
print(f"Слияние двух словарей: {slov_1}")