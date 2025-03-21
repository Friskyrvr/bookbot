def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents
        

def main(file):
    words = []
    text = get_book_text(file)
    words = text.split(' ')
    num_words = len(words)
    print(f"{num_words} words found in the document")


main("books/frankenstein.txt")
    