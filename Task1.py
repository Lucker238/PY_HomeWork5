# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'Грустная история абвгдеёжз. Однажды аававаБвв утром я абвввыф пошел ыфвабвфыв на работу. Мне ааабвбфыв это не особо абвва понравилось абвфыв (( АБВГД! Абв Конец!'
signs = {'.',',','?','!','-',':',';'}

def del_words(txt):
    txt_array = txt.split(' ')
    i = len(txt_array) - 1
    while i > 0:
        if 'абв' in txt_array[i].lower():
            if txt_array[i][-1] in signs:
                txt_array[i-1] += txt_array[i][-1]
            txt_array.pop(i)
        i -= 1
    if 'абв' in txt_array[i].lower():
        txt_array.pop(i)

    return ' '.join(txt_array)

print(del_words(text))