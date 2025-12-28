def to_float_array(arr):
    li = []
    for x in arr:
        if "." in x:
            li.append(float(x))
        else:
            li.append(int(x))
    return li
