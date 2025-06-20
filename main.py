import sys
from stats import num_words
from stats import character_count
if len(sys.argv) != 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
bookpath = sys.argv[1]

def get_book_text(bookpath):
    with open(bookpath) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text(bookpath)
    letters_counted = character_count(book_text)
    wordcount = num_words(book_text)
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {bookpath}...")
    print ("----------- Word Count ----------")
    print (f"Found {wordcount} total words")
    #print (letters_counted)
    print ("--------- Character Count -------")
    from stats import sorted_results
    result = sorted_results(letters_counted)
    for char_dict in result:
        if char_dict["char"].isalpha():
            print (f"{char_dict["char"]}: {char_dict["num"]}")
    print ("============= END ===============")
main()
