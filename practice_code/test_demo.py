import random



question = ["are you hungry ?", "are you sleepy ?", "are you stuby ?"]
answer = ["hungry","sleepy","stuby"]
random.shuffle(question)#重新排列
for i in question:
    ans = input(i)
    j = 0 
    while j < len(question):

        if ans in answer[j] and answer[j] in i :
            print("☆★")
            break
        else:
            j += 1
            
    


