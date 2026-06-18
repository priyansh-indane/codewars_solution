def switcher(arr):
    mapping = {str(26 - i): chr(ord('a') + i) for i in range(26)}
    mapping['27'] = '!'
    mapping['28'] = '?'
    mapping['29'] = ' '
    return ''.join(mapping[n] for n in arr)
