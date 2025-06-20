def num_words(file_contents):
    numwords = 0
    book_content = file_contents
    words = book_content.split()
    for words in words:
        numwords += 1
    return numwords

def character_count(file_contents):
    book_content = file_contents
    lower_case = book_content.lower()
    letters = {}
    for char in lower_case:
      if char in letters:
            letters[char] += 1
      else:
          letters[char] = 1
    return letters

def sort_on(letter):
     return letter["num"]

def sorted_results(letters_counted):
    character_lists = []
    for letter in letters_counted:
        character_lists.append({"char": letter, "num": letters_counted[letter]})
    character_lists.sort(reverse=True, key=sort_on)
    return character_lists



