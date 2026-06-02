def cookie(x):
    if type(x) is str:
        return "Who ate the last cookie? It was Zach!"

    elif type(x) is float or type(x) is int:
        return "Who ate the last cookie? It was Monica!"

    else:
        return "Who ate the last cookie? It was the dog!"
