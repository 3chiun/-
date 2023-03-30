#model.split word
def change(word):
    word = word.split(",")
    count = 0
    word_list = []
    word_finish = []
    for word_get in word:
        for simpleword_get in word_get:           
            if count > 0 and count < len(word_get)-1:
                word_list.append("_")
            else:
                word_list.append(simpleword_get)
            count += 1
        word = "".join(word_list)
        word_finish.append(word)
        word_list = []
        count = 0    
    return word_finish

# word = input("""put the damn english word here with ',' : """)
# print(change(word))




