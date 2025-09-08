def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def dict_sort(chars):
    char_list = []
    for key, value in chars.items():
        if key.isalpha():
            new_dict = {"char": key, "num": value}
            char_list.append(new_dict)
            char_list.sort(key=lambda d: d["num"], reverse=True)
    return char_list
    
    
