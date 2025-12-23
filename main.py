import sys
from stats import count_words, sorted_dict


def main(file_path):
    words = count_words(file_path)
    letter_list = sorted_dict(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in letter_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])
