from stats import get_num_words
from stats import get_num_chars
from stats import sorted_dictionary
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
  
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file = get_book_text(sys.argv[1])
    dict = sorted_dictionary(get_num_chars(file))
    words = get_num_words(file)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for dic in dict:
        if dic["char"].isalpha():
            print(f"{dic['char']}: {dic['count']}")
    print("============= END ===============")
main()
