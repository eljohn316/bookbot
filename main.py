import sys

from stats import get_num_words, count_letter_occurrences, sort_letter_count_record


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def get_filepath():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]


def main():
    filepath = get_filepath()
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    letter_count = count_letter_occurrences(text)
    report = sort_letter_count_record(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in report:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
