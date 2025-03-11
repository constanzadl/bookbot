def get_num_words(file):
    words = file.split()
    return(len(words))

def get_num_chars(file):
    characters = {}
    file = file.lower()
    for word in file:
        for char in word:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def sort_on(dict):
    return dict["count"]

def sorted_dictionary(dic):
    complete_dictionary = []
    for key in dic:
        key_dic = {"char": key, "count": dic[key]}
        complete_dictionary.append(key_dic)
    complete_dictionary.sort(reverse=True, key=sort_on)
    return complete_dictionary
