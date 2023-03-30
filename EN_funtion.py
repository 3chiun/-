import requests as req
import bs4
import random
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
def c_bridge(word):
    cows = []
    header = {
        'User-Agent' : "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
    }
    word_list = word.split(",")
    for words in word_list:
        try:
            url = "https://dictionary.cambridge.org/zht/詞典/英語-漢語-繁體/{}".format(words)
            re = req.get(url,headers=header)
            soup = bs4.BeautifulSoup(re.text, "html.parser")
            sentences = soup.find_all("span",class_="eg deg")
            try:
                for sen in sentences:
                    cows.append(sen.text)
                    # print(sen.text)
            except:
                print("none")
        except:
            print("""word not find 
                try to check your spelling or make sure you internet is conecting"""
            )
    return cows
def select(cows):
    question_root = []
    for sentence in cows:
        if len(sentence) > 15:
            # print(sentence)
            question_root.append(sentence)
        else:
            continue
    return question_root #list
def S_bridge(word):
    cows = []
    dic = {}
    header = {
        'User-Agent' : "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
    }
    word_list = word.split(",")
    for words in word_list:
        try:
            url = "https://dictionary.cambridge.org/zht/詞典/英語-漢語-繁體/{}".format(words)
            re = req.get(url,headers=header)
            soup = bs4.BeautifulSoup(re.text, "html.parser")
            sentences = soup.find_all("span",class_="trans dtrans dtrans-se break-cj")
            try:
                for sen in sentences:
                    cows.append(sen.text)
                    dic[sen.text] = words
                    #print(sen.text)
            except:
                print("none")
        except:
            print("""word not find 
                try to check your spelling or make sure you internet is conecting"""
            )
    return dic
def dig(word, question_root):
    question = []
    question_2 = []
    words = word.split(",")
    for get_word in range(len(question_root)): # 一句一句取出
        debug_01 = 0
        for i in range(len(words)): # 字對照單字
                if words[i] in question_root[get_word] and debug_01 == 0: 
                    question_2.append(question_root[get_word])
                    question.append(question_root[get_word].replace(words[i] ,change(word)[i]))
                    debug_01 +=1
            
    return question,question_2 #list

def sentence_QA():
    QAsentence_word = input("""put the damn english word here with ',' : """)
    ran = []
    incorrect_sen = []
    incorrect_word = []
    count = 0
    notcount = 0
    question_1,question_2 = dig(QAsentence_word, select(c_bridge(QAsentence_word)))

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

def word_QA():
    QA_word = input("""put the damn english word here with ',' : """)
    ran = []
    incorrect_EN = []
    incorrect_CH = []
    count = 0
    notcount = 0
    #error = 0
    check = S_bridge(QA_word)
    question = list(check.keys())
    # print(question)
    for i in range(len(question)):
        ran.append(i)
    random.shuffle(ran)
    for i in ran:
        ans = input(question[i]+":")    
        try:                    
            if ans == check[question[i]]  :
                goodjob = ["☆恭喜★","☆你很棒★","☆天資聰穎★","☆歎為觀止★","☆非常好★","☆perfect★","☆excellent★","☆very good★","☆correct★","☆喔wow★","☆你已經達到神的境界★"]
                print(random.choice(goodjob))
                count += 1
            elif ans != check[question[i]]  :
                not_bad = ["其實是...{}","應該是...{}"]
                print(random.choice(not_bad).format(check[question[i]]))
                incorrect_EN.append(str(check[question[i]]))
                incorrect_CH.append(str(question[i]))
                notcount += 1
            # else:
            #     error += 1
            #     print(error)
        except:
                print("抱歉產生未知的問題")
                break
    print("你答對了{}題, 答錯了{}題,錯題如下請好好複習複習".format(count,notcount)) 
    for f in range(len(incorrect_CH)):
        print(incorrect_CH[f],"\n答案是:"+incorrect_EN[f])