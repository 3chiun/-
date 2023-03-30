from re import S
import requests as req
import bs4
import random
# test = input("""put the damn english word here with ',' : """)
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
     
#print(S_bridge(test)) 
def word_QA():
    QA_word = input("""put the damn english word here with ',' : """)
    ran = []
    incorrect_EN = []
    incorrect_CH = []
    count = 0
    notcount = 0
    error = 0
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
if __name__ == "__main__":
    word_QA()