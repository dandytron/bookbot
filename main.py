def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    letter_count.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in this document\n\n")
    for letter in letter_count:
        print(f"The '{letter["letter"]}' character was found {letter["num"]} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    word_counter = 0
    for word in words:
        word_counter += 1
    return word_counter

def count_letters(text):
    lowered_letters = text.lower()
    letter_count_list = []
    for char in lowered_letters:
        if char.isalpha():
            is_in_list = False
            for dictionary in letter_count_list:
                if dictionary["letter"] == char:
                    dictionary["num"] += 1
                    is_in_list = True
            if is_in_list == False:
                new_char = {
                    "letter": char,
                    "num": 1
                }
                letter_count_list.append(new_char)
    return letter_count_list

def sort_on(dict):
    return dict["num"]

main()