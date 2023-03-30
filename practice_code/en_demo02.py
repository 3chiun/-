import requests as req
import bs4
# test = input("""put the damn english word here with ',' : """)

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
# for i in select(c_bridge(test)):
#     print(i) 
if __name__ == "__main__":
    word = input("word")
    c_bridge(word)
