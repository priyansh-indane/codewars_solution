def spacey(array):
    arr = []
    for x in array:
        prev = arr[-1] if arr else ""
        arr.append(prev + x.replace(" ", ""))
    return arr
