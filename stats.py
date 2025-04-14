def word_count(text):
    wc = text.split()
    num_of_words = len(wc)
    return num_of_words

def count_chars(text):
    new_text = text.lower()
    char_count = {}
    for c in new_text:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    return char_count
    
def sort_list(char_count):
    chars_list = []
    for char, count in char_count.items():
            chars_list.append({"char": char, "count": count})
    chars_list.sort(reverse=True, key=lambda d: d["count"])
    return chars_list