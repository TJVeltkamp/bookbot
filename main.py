import sys
from stats import get_num_words
from stats import get_letter_lib
from stats import sort_dict_list
def main(args):
    
    try:
        file=args[1]
        text =get_book_text(file)
        number =get_num_words(text)
        lib= get_letter_lib(text)
        sorted_list= sort_dict_list(lib)
        #print(sorted_list)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file}")
        print("----------- Word Count ----------")
        print(f"Found {number} total words")
        print("--------- Character Count -------")
        for item in sorted_list:
            print(f"{item['char']}: {item['num']}")
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

main(sys.argv)