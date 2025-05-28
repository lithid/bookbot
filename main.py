import sys
from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted_chars


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    book_words = get_book_text(book)
    print("----------- Word Count ----------")
    num_words = get_num_words(book_words)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in get_sorted_chars(get_num_chars(book_words)):
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")


main()
