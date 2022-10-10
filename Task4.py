# Например, строчку aaababbcbbb он переводит в (a, 3) (b, 1) (a, 1) (b, 2) (c, 1) (b, 3).

text = 'aaababbcbbbzzzzzaaaaaaabbywwwwwwwwwww'

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

print(text)
print(coding(text))
print(decoding(coding(text)))