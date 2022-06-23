def is_isogram(string):
    iso = {}
    for char in string:
        if char.lower() in iso:
            return False;
        iso[char.lower()] = True;
    return True;