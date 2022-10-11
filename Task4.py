# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Например, строчку aaababbcbbb он переводит в (a, 3) (b, 1) (a, 1) (b, 2) (c, 1) (b, 3).


def coding(text: str):
    archive = [('just for volume',100500)]
    pre_letter = text[0]
    i = 0
    count = 1
    for letter in text:
        if letter == pre_letter:
            archive[i] = (letter, count+1)
            count += 1
        else:
            pre_letter = letter
            count = 1
            i += 1
            archive.append((letter, count))
    return archive
        
def decoding(arch: list):
    decode = ''
    for i in arch:
        decode += i[0] * i[1]
    return decode

path_in = 'C:/Users/User/Desktop/Geekbrains/Python/HW5/input.txt'
inp = open(path_in, 'r')
text = inp.read()
inp.close()

coding_text = coding(text)

path_out = 'C:/Users/User/Desktop/Geekbrains/Python/HW5/output.txt'
out = open(path_out, 'w')
out.write(str(coding_text))
out.close()

one_more_out = open(path_out, 'r')
text_for_decoding = one_more_out.read()


text_for_decoding = text_for_decoding[2:len(text_for_decoding)-2]
text_for_decoding = text_for_decoding.replace("'",'')
list_for_decoding = text_for_decoding.split('), (')
one_more_list = []
for i in list_for_decoding:
    k = i.split(', ')
    one_more_list.append((str(k[0]), int(k[1])))

print(text)
print(coding_text)
print(decoding(one_more_list))
