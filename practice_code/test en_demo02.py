import requests as req
words = input("""put the damn english word here with ',' : """).split(",")
for word in words:
    url = "https://translate.google.com.tw/?hl=zh-TW&sl=en&tl=zh-TW&text={}&op=translate".format(word)
    r = req.get(url)
    print(r)
    