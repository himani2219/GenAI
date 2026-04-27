def capitalize_text(text):
    list = text.split()
    for i in range(len(list)):
        list[i] = list[i].capitalize()
    return " ".join(list)

def reverse_string(text):
    return text[::-1]

def word_count(text):
    list = text.split()
    return len(list)