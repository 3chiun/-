import en_demo01
import en_demo02
import requests as req
import bs4
import random


def dig(word, question_root):
    question = []
    question_2 = []
    words = word.split(",")
    for get_word in range(len(question_root)): # 一句一句取出
        debug_01 = 0
        for i in range(len(words)): # 字對照單字
                if words[i] in question_root[get_word] and debug_01 == 0: 
                    question_2.append(question_root[get_word])
                    question.append(question_root[get_word].replace(words[i] ,en_demo01.change(word)[i]))
                    debug_01 +=1
            
    return question,question_2 #list

def sentence_QA():
    QAsentence_word = input("""put the damn english word here with ',' : """)

    ran = []
    incorrect_sen = []
    incorrect_word = []
    count = 0
    notcount = 0
    question_1,question_2 = dig(QAsentence_word, en_demo02.select(en_demo02.c_bridge(QAsentence_word)))

    answer = QAsentence_word.split(",") 
    for i in range(len(question_1)):
        ran.append(i)
    random.shuffle(ran)
    for i in ran:
        ans = input(question_1[i]+":")
        for j in range(len(answer)):
            try:                    
                if ans == answer[j] and answer[j] in question_2[i] :
                    goodjob = ["☆恭喜★","☆你很棒★","☆天資聰穎★","☆歎為觀止★","☆非常好★","☆perfect★","☆excellent★","☆very good★","☆correct★","☆喔wow★","☆你已經達到神的境界★"]
                    print(random.choice(goodjob))
                    count += 1
                    break
                elif ans != answer[j] and answer[j] in question_2[i]:
                    not_bad = ["其實是...{}","應該是...{}"]
                    print(random.choice(not_bad).format(answer[j]))
                    incorrect_sen.append(str(question_1[i]))
                    incorrect_word.append(str(answer[j]))
                    notcount += 1
            except:
                    print("抱歉產生未知的問題")
    print("你答對了{}題, 答錯了{}題,錯題如下請好好複習複習".format(count,notcount)) 
    for f in range(len(incorrect_sen)):
        print(incorrect_sen[f],"\n答案是:"+incorrect_word[f])


# bug:如果句子中的一個字的部分是由該查詢單字組成也會被當成挖空對象
# ex: 目標:king 句子中的字:making 結果:mak__g 
if __name__ == "__main__":
    sentence_QA()
    
                
    
        
