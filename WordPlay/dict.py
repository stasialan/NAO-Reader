dictionary = set()
def find_word(word):
    word=word.lower()
    return word in dictionary
def load_dict():
    f=open("dict.txt", "r")
    l=f.readlines()
    for a in l:
        dictionary.add(a[:-2])
    f.close()



