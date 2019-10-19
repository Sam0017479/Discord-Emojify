import re

def emojify(text):
    emojified = ""

    textList = list(text)
    for i in textList:
        if re.search(r'[,". `~]', i):
            emojified += i
        else:
            emojified += f":regional_indicator_{i}: "
    
    print(emojified)

emojify("life could be dream, life could be dream. doo doo doo doo wop.")
