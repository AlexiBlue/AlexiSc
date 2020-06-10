import pyperclip
import time


def sychangetoen(subj):
    i = 0
    strongo = ''
    while i < len(subj):
        strongo = strongo + sychangetoenfn(subj[i])
        i+=1
    return strongo

def sychangetoenfn(symb):
    i = 0
    while i < len(rulng):
        if symb == rulng[i]:
            symb = enlng[i]
        i+=1
    return symb





def sychangetoru(subj):
    i = 0
    strongo = ''
    while i < len(subj):
        strongo = strongo + sychangetorufn(subj[i])
        i+=1
    return strongo

def sychangetorufn(symb):
    i = 0
    while i < len(rulng):
        if symb == enlng[i]:
            symb = rulng[i]
        i+=1
    return symb

rulng = ['ё','-','=','\\','й','ц','у','к','е','н','г','ш','щ','з','х','ъ','ф','ы','в','а','п','р','о','л','д','ж','э','я','ч','с','м','и','т','ь','б','ю','.','Ё','!','"','№',';','%',':','?','*','(',')','_','+','/','Й','Ц','У','К','Е','Н','Г','Ш','Щ','З','Х','Ъ','Ф','Ы','В','А','П','Р','О','Л','Д','Ж','Э','Я','Ч','С','М','И','Т','Ь','Б','Ю',',']
enlng = ['`','-','=','\\','q','w','e','r','t','y','u','i','o','p','[',']','a','s','d','f','g','h','j','k','l',';',"'",'z','x','c','v','b','n','m',',','.','/','~','!','@','#','$','%','^','&','*','(',')','_','+','|','Q','W','E','R','T','Y','U','I','O','P','{','}','A','S','D','F','G','H','J','K','L',':','"','Z','X','C','V','B','N','M','<','>','?']


print('1 - English to Russian')
print('2 - Russian to English')

if input() == '1':
    pyperclip.copy(sychangetoru(pyperclip.paste()))
    print('ok')
else:
    pyperclip.copy(sychangetoen(pyperclip.paste()))





