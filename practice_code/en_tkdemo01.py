from itertools import count
from tkinter import*

import requests as req
import bs4
import random
import time
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
def sentence_QA(QAsentence_word):
    # QAsentence_word = input("""put the damn english word here with ',' : """)
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
def win_CH():
    def CH_end():
        def start_CH():
            def CH_Q(i):
                def CH_enter(): 
                        ans = test_input.get() 
                        
                        if ans == check[question[i]] :
                            win = Tk()
                            goodjob = ["☆恭喜★","☆你很棒★","☆天資聰穎★","☆歎為觀止★","☆非常好★","☆perfect★","☆excellent★","☆very good★","☆correct★","☆喔wow★","☆你已經達到神的境界★"]
                            good = Label(
                                    win,
                                    text=random.choice(goodjob)+" "*100,
                                    font=("新細明體",12,"bold"),
                                    fg ="#088A08",
                                    bg = "white"
                                )
                            good.grid()
                            time.sleep(1)
                            test_CH.destroy()
                            win.mainloop()
                            
                        else:
                            
                            win = Tk()
                            not_bad = ["其實是...{}","應該是...{}"]
                            bad = Label(
                                    win,
                                    text=random.choice(not_bad).format(check[question[i]])+" "*100,
                                    font=("新細明體",12,"bold"),
                                    fg ="#088A08",
                                    bg = "white"
                                )
                            bad.grid()

                            incorrect_CH.append(str(question[i]))
                            incorrect_EN.append(str(check[question[i]]))
                            time.sleep(1)
                            test_CH.destroy()
                            win.mainloop()
                                
                test_CH = Tk()
                test_CH.title("sentese test")
                test_CH.geometry("1080x320")    
                test_CH.config(background="white")

                Q_CH = Label(
                    test_CH,
                    text=question[i]+":"+" "*100,
                    font=("新細明體",12,"bold"),
                    fg ="#088A08",
                    bg = "white"
                )
                test_input = Entry(
                        test_CH,
                        font = ("FrLt DFGirl",36),
                        fg = "#FF00FF"
                    )
                enter = Button(
                        test_CH,
                        state=ACTIVE,
                        text="確定",
                        font=("新細明體",36),
                        fg = "#4C0B5F",
                        bg="black",
                        activeforeground="#4C0B5F",
                        activebackground="black",
                        command=CH_enter
                    )
                Q_CH.grid()
                test_input.grid()
                enter.grid()
                test_CH.mainloop()
                
                    
            

            QA_word = txt
            main_sen.destroy()

            ran = []
            incorrect_EN = []
            incorrect_CH = []

            
            
            check = S_bridge(QA_word)
            question = list(check.keys())

            for i in range(len(question)):
                ran.append(i)
            random.shuffle(ran)
            for i in ran:
                CH_Q(i)
            
            
            end0 = Tk()
            end0.title("wrong")
            end0.geometry("1080x320")
            end0.config(background="white")
            end = Label(
                    end0,
                    text="錯題如下請好好複習複習"+" "*100,
                    font=("新細明體",12,"bold"),
                    fg ="#088A08",
                    bg = "white"
                    )
            end.place(x=50,y=50)
            for f in range(len(incorrect_CH)):
                time.sleep(2)
                sen_answer_1 = Label(
                    end0,
                    text= incorrect_CH[f]+" "*100,
                    font=("新細明體",12,"bold"),
                    fg ="#088A08",
                    bg = "white"
                    )
                sen_answer_2 = Label(
                    end0,
                    text=incorrect_EN[f]+" "*100,
                    font=("新細明體",12,"bold"),
                    fg ="#088A08",
                    bg = "white"
                    )
                sen_answer_1.place(x=50,y=200)
                sen_answer_2.place(x=50,y=300)
                end0.update()
            end0.mainloop()
        txt = CH_input.get()
        win_CH.destroy()
        main_sen = Tk()
        main_sen.title("start")
        main_sen.geometry("1080x320")
        main_sen.config(background="white")
        CH_head = Label(
            main_sen,
            text="中翻英測試",
            font=("新細明體",36,"bold"),
            fg ="#000000",
            bg = "white"
        )
        CH_body = Label(
            main_sen,
            text="題目會是中文的翻譯，以英文做回答",
            font=("新細明體",22,"bold"),
            fg ="#000000",
            bg = "white"
        )
        
        CH_bon = Button(
            main_sen,
            state=ACTIVE,
            text="開始",
            font=("新細明體",22),
            fg = "#00FFFF",
            bg="white",
            activeforeground="#FF00FF",
            activebackground="white",
            command=start_CH   
        )
        CH_head.pack()
        CH_body.pack()
        CH_bon.pack()
        time.sleep(3)
        # main_sen.destroy()
        main_sen.mainloop()
    main_win.destroy()
    win_CH = Tk()
    win_CH.title("search for sentese")
    win_CH.geometry("1080x320")    
    win_CH.config(background="white")

    CH_title = Label(
        win_CH,
        text="以中文考英文",
        font=("新細明體",36,"bold"),
        fg ="#000000",
        bg = "white"
    )
    CH_explain = Label(
        win_CH,
        text="輸入多個想要考的英文單字用逗點(,)隔開",
        font=("新細明體",30,"bold"),
        fg ="#8000FF",
        bg = "white"
    )
    CH_input = Entry(
        win_CH,
        font = ("FrLt DFGirl",36),
        fg = "#FF00FF"
    )
    
    get_in = Button(
        win_CH,
        state=ACTIVE,
        text="開始搜尋",
        font=("新細明體",36),
        fg = "#4C0B5F",
        bg="black",
        activeforeground="#4C0B5F",
        activebackground="black",
        command=CH_end
        
    )
    CH_title.pack()
    CH_explain.pack()
    CH_input.pack()
    get_in.pack()
        
    win_CH.mainloop()

def win_seninput():
    def sen_end():
        def start_sen():
            def sen_Q(i):
                def sen_enter(): 
                        ans = test_input.get()  
                        for j in range(len(answer)):
                            if ans == answer[j] and answer[j] in question_2[i] :
                                win = Tk()
                                goodjob = ["☆恭喜★","☆你很棒★","☆天資聰穎★","☆歎為觀止★","☆非常好★","☆perfect★","☆excellent★","☆very good★","☆correct★","☆喔wow★","☆你已經達到神的境界★"]
                                good = Label(
                                        win,
                                        text=random.choice(goodjob)+" "*100,
                                        font=("新細明體",12,"bold"),
                                        fg ="#088A08",
                                        bg = "white"
                                    )
                                good.grid()
                                time.sleep(1)
                                test_sen.destroy()
                                win.mainloop()
                                break
                            else:
                                while answer[j] in question_2[i]:
                                    win = Tk()
                                    not_bad = ["其實是...{}","應該是...{}"]
                                    bad = Label(
                                            win,
                                            text=random.choice(not_bad).format(answer[j])+" "*100,
                                            font=("新細明體",12,"bold"),
                                            fg ="#088A08",
                                            bg = "white"
                                        )
                                    bad.grid()

                                    incorrect_sen.append(str(question_1[i]))
                                    incorrect_word.append(str(answer[j]))
                                    time.sleep(1)
                                    test_sen.destroy()
                                    win.mainloop()
                                    break
                test_sen = Tk()
                test_sen.title("sentese test")
                test_sen.geometry("1080x320")    
                test_sen.config(background="white")

                Q_sen = Label(
                    test_sen,
                    text=question_1[i]+":"+" "*100,
                    font=("新細明體",12,"bold"),
                    fg ="#088A08",
                    bg = "white"
                )
                test_input = Entry(
                        test_sen,
                        font = ("FrLt DFGirl",36),
                        fg = "#FF00FF"
                    )
                enter = Button(
                        test_sen,
                        state=ACTIVE,
                        text="確定",
                        font=("新細明體",36),
                        fg = "#4C0B5F",
                        bg="black",
                        activeforeground="#4C0B5F",
                        activebackground="black",
                        command=sen_enter
                    )
                Q_sen.grid()
                test_input.grid()
                enter.grid()
                test_sen.mainloop()
                
                    
            

            QAsentence_word = txt
            main_sen.destroy()

            ran = []
            incorrect_sen = []
            incorrect_word = []
            question_1,question_2 = dig(QAsentence_word, select(c_bridge(QAsentence_word)))

            answer = QAsentence_word.split(",") 
            for i in range(len(question_1)):
                        ran.append(i)
                        random.shuffle(ran)
            for i in ran:
                sen_Q(i)
            
            end0 = Tk()
            end0.title("wrong")
            end0.geometry("1080x320")
            end0.config(background="white")
            end = Label(
                    end0,
                    text="錯題如下請好好複習複習"+" "*100,
                    font=("新細明體",12,"bold"),
                    fg ="#088A08",
                    bg = "white"
                    )
            end.place(x=50,y=50)
            for f in range(len(incorrect_sen)):
                time.sleep(2)
                sen_answer_1 = Label(
                    end0,
                    text= incorrect_sen[f]+" "*100,
                    font=("新細明體",12,"bold"),
                    fg ="#088A08",
                    bg = "white"
                    )
                sen_answer_2 = Label(
                    end0,
                    text=incorrect_word[f]+" "*100,
                    font=("新細明體",12,"bold"),
                    fg ="#088A08",
                    bg = "white"
                    )
                sen_answer_1.place(x=50,y=200)
                sen_answer_2.place(x=50,y=300)
                end0.update()
            end0.mainloop()

        txt = sen_input.get()
        win_sen.destroy()
        main_sen = Tk()
        main_sen.title("start")
        main_sen.geometry("1080x320")
        main_sen.config(background="white")
        sen_head = Label(
            main_sen,
            text="句型挖空測試",
            font=("新細明體",36,"bold"),
            fg ="#000000",
            bg = "white"
        )
        sen_body = Label(
            main_sen,
            text="每一個句子都會有一個字只留首尾，需要填入該字",
            font=("新細明體",22,"bold"),
            fg ="#000000",
            bg = "white"
        )
        
        sen_bon = Button(
            main_sen,
            state=ACTIVE,
            text="開始",
            font=("新細明體",22),
            fg = "#00FFFF",
            bg="white",
            activeforeground="#FF00FF",
            activebackground="white",
            command=start_sen   
        )
        sen_head.pack()
        sen_body.pack()
        sen_bon.pack()
        time.sleep(3)
        # main_sen.destroy()
        main_sen.mainloop()
    main_win.destroy()
    win_sen = Tk()
    win_sen.title("search for sentese")
    win_sen.geometry("1080x320")    
    win_sen.config(background="white")

    sen_title = Label(
        win_sen,
        text="句型挖空",
        font=("新細明體",36,"bold"),
        fg ="#000000",
        bg = "white"
    )
    sen_explain = Label(
        win_sen,
        text="輸入多個想要考的英文單字用逗點(,)隔開",
        font=("新細明體",30,"bold"),
        fg ="#8000FF",
        bg = "white"
    )
    sen_input = Entry(
        win_sen,
        font = ("FrLt DFGirl",36),
        fg = "#FF00FF"
    )
    
    get_in = Button(
        win_sen,
        state=ACTIVE,
        text="開始搜尋",
        font=("新細明體",36),
        fg = "#4C0B5F",
        bg="black",
        activeforeground="#4C0B5F",
        activebackground="black",
        command=sen_end
        
    )
    sen_title.pack()
    sen_explain.pack()
    sen_input.pack()
    get_in.pack()
        
    win_sen.mainloop()

def win_searchinput():
    def search_end():
        def start_s():
            words = txt
            # print(words)
            dic = S_bridge(words)
            # print(dic)
            main_search.destroy()
            play_search = Tk()
            play_search.title("CH-EN")
            play_search.geometry("1080x320")
            play_search.config(background="white")
            search = list(dic.keys())

            for i in range(len(search)):
                time.sleep(1.5)
                search_EN = Label(
                    play_search,
                    text=dic[search[i]]+" "*150,
                    font=("新細明體",12,"bold"),
                    fg ="#088A08",
                    bg = "white"
                )
                search_CH = Label(
                    play_search,
                    text=search[i]+" "*150,
                    font=("新細明體",12,"bold"),
                    fg ="#088A08",
                    bg = "white"
                ) 
                search_EN.place(x=100,y=100)
                search_CH.place(x=100,y=200)
                play_search.update()    
                
        text_1 = "英文"
        text_2 = "中文"
        txt = search_input.get()    
        win_search.destroy()
        main_search = Tk()
        main_search.title("start")
        main_search.geometry("1080x320")
        main_search.config(background="white")
        search_EN = Label(
            main_search,
            text=text_1,
            font=("新細明體",36,"bold"),
            fg ="#000000",
            bg = "white"
        )
        search_CH = Label(
            main_search,
            text=text_2,
            font=("新細明體",36,"bold"),
            fg ="#000000",
            bg = "white"
        )
        
        search_bon = Button(
            main_search,
            state=ACTIVE,
            text="開始",
            font=("新細明體",22),
            fg = "#00FFFF",
            bg="white",
            activeforeground="#FF00FF",
            activebackground="white",
            command=start_s   
        )
        search_EN.pack()
        search_CH.pack()
        search_bon.pack()
        main_search.mainloop()
    main_win.destroy()
    win_search = Tk()
    win_search.title("search word")
    win_search.geometry("1080x320")    
    win_search.config(background="white")

    search_title = Label(
        win_search,
        text="查英文單字",
        font=("新細明體",36,"bold"),
        fg ="#000000",
        bg = "white"
    )
    search_explain = Label(
        win_search,
        text="輸入多個想要查的英文單字用逗點(,)隔開",
        font=("新細明體",30,"bold"),
        fg ="#8000FF",
        bg = "white"
    )
    search_input = Entry(
        win_search,
        font = ("FrLt DFGirl",36),
        fg = "#FF00FF"
    )
    
    get_in = Button(
        win_search,
        state=ACTIVE,
        text="開始搜尋",
        font=("新細明體",36),
        fg = "#4C0B5F",
        bg="black",
        activeforeground="#4C0B5F",
        activebackground="black",
        command=search_end
    )
    search_title.pack()
    search_explain.pack()
    search_input.pack()
    get_in.pack()
        
    win_search.mainloop()
#############################################################################################

main_win = Tk()
icon = PhotoImage(file="EN_logo.png")
main_win.title("my english test program")
main_win.geometry("1080x680")
main_win.iconphoto(True,icon)
main_win.config(background="white")

title_img = PhotoImage(file="cutetitle.png")
title_main = Label(
    main_win,
    text="你好,請問我能為您提供什麼服務?",
    font=("新細明體",28,"bold"),
    fg="#0000FF",
    bg="white",
    image=title_img,
    compound="top"
)
space = Label( 
    main_win,
    text = "          ",
    font=("新細明體",32),
    bg = "white"
)


bon_f = Frame(main_win)

bon_search = Button(
    bon_f,
    state=ACTIVE,
    text="查英文單字",
    font=("新細明體",22),
    fg = "#00FFFF",
    bg="white",
    activeforeground="#FF00FF",
    activebackground="white",
    command=win_searchinput    
)
bon_sen = Button(
    bon_f,
    state=ACTIVE,
    text="句子挖空",
    font=("新細明體",22),
    fg = "#00FFFF",
    bg="white",
    activeforeground="#FF00FF",
    activebackground="white",
    command=win_seninput
)
bon_CH = Button(
    bon_f,
    state=ACTIVE,
    text="中翻英",
    font=("新細明體",22),
    fg = "#00FFFF",
    bg="white",
    activeforeground="#FF00FF",
    activebackground="white",
    command=win_CH    
)

title_main.pack()
bon_search.pack(side="left")
bon_sen.pack(side="left")
bon_CH.pack(side="left")
space.pack()
bon_f.pack()


main_win.mainloop()

