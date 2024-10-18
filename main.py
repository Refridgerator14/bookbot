def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_characters(text)
    print(f"--- A(z) {book_path} beszámoló megkezdése ---")
    print(f"{word_count} szó található a dokumentumban")
    print()

    for char_dict in characters_for_rep:
        print(f"A(z) '{char_dict['character']}' betü {char_dict['count']} szerepel")
    print("--- Beszámoló vége  ---")












def get_book_text(path):
    with open(path) as f:
        return f.read()







text = ""
def count_words(text) :
    words = text.split()
    return len(words)




def count_characters(text):
    lowered_text = text.lower()
    char_count = {char: 0 for char in 'abcdefghijklmnopqrstuvwxyz'}

    for char in lowered_text:
        if char.isalpha():
            char_count[char] += 1
        
    return char_count





with open('books/frankenstein.txt', 'r') as file:
    book_content = file.read()


char_count = count_characters(book_content)



def sort_on(char_dict):
    return char_dict["count"]


characters_for_rep = []






for character, count in char_count.items():

    character_dict = {"character": character, "count": count}
    characters_for_rep.append(character_dict)

characters_for_rep.sort(reverse=True, key=sort_on)
    


main()
    
          