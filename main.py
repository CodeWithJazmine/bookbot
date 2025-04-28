import sys
from stats import get_book_text
from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted_chars

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_file = sys.argv[1]

    book_text = get_book_text(book_file)

    num_words = get_num_words(book_text)

    num_chars = get_num_chars(book_text)

    sorted_chars = get_sorted_chars(num_chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]

        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()