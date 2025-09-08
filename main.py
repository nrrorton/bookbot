from stats import get_num_words, get_chars_dict, dict_sort
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    list_dict = dict_sort(chars_dict)
    for item in list_dict:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()