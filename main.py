def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in this document\n\n")

    for char in chars_sorted_list:
        if not char["char"].isalpha():
            continue
        print(f"The '{char["char"]}' character was found {char["num"]} times")



def count_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def dict_to_sorted_list(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char": char, "num": dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()