def nth_char(words):
    result = ""  # This must be defined before the loop starts
    for i in range(len(words)):
        word = words[i]
        result += word[i]
    return result
