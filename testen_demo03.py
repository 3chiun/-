key = "123456"#6
garbled = "098889654612345678987"#21
# print(p[2])

for i in range(len(garbled)-len(key)-1):# 0~15=16 // 21-6-1=14 0~14=15    
    if garbled[i:i+len(key)] == key:
        print("find,第{}次".format(i+1))
        print(garbled[i:i+len(key)])
        garbled = garbled.replace(garbled[i:i+len(key)], "0")
        print(garbled)


    else:
        print("continue,第{}次".format(i+1))
        print(garbled[i:i+len(key)])
#理論值是第11次找到

        
