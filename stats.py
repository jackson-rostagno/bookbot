def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def count_words(file_path):
    text = get_book_text(file_path)
    return len(text.split())


def char_count(file_path):
    text = get_book_text(file_path).lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_on(d):
    return d["num"]


def sorted_dict(file_path):
    dict = char_count(file_path)
    list = []
    for char, count in dict.items():
        if char.isalpha():
            list.append({"char": char, "num": count})
    list.sort(reverse=True, key=sort_on)
    return list
