import stats
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(t):
    with open(t, 'r') as file:
        return file.read()

def main():
    t = sys.argv[1]
    text = get_book_text(t)
    print(f"Book path received: {t}")
    char_count = stats.count_chars(text)
    word_count = stats.word_count(text)
    print(f"{word_count} words found in the document")
    print(char_count)

    sorted_chars = stats.sort_list(char_count)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at:", t)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
        
    print("============= END ===============")


if __name__ == "__main__":
    main()    