"""main.py"""


def get_num_words(text):
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


def sort_on(e):
    return e["count"]


def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for k in chars_dict:
        sorted_list.append({"char": k, "count": chars_dict[k]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_book_contents(book_path):
    with open(book_path, "r") as f:
        text = f.read()
    return text


def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_contents(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    # print(chars_dict)
    sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words in the document.")
    print()

    for k in sorted_list:
        if not k["char"].isalpha():
            continue
        print(f"Character '{k["char"]}' appears {k["count"]} times.")

    print("--- End report ---")


if __name__ == "__main__":
    main()
