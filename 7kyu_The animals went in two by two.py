def two_by_two(animals):
    if not animals:
        return False
    return {a: 2 for a in set(animals) if animals.count(a) >= 2}
