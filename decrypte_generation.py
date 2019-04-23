import PyPDF2


def character_get(number):
    character = char_list[number]
    return character


# 94个字符
char = r'`1234567890-=~!@#$%^&*()_+abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[]\{}|;\':",./<>?'
char_list = list(char)
a = char_list.pop(62)

pdfReader = PyPDF2.PdfFileReader(open('FLBL.pdf', 'rb'))
circle = 1
while circle <= 6:
    print(f'starting circle:{circle}')
    index = [0 for i in range(circle)]
    inner_circle = 0
    temp_list = ["" for k in range(circle)]
    while index[-1] < len(char_list):
        for i in range(len(index)-1):
            if index[i] == len(char_list):
                index[i] = 0
                index[i+1] += 1
        for j in range(len(index)-1):
            temp_list[j] = char_list[index[j]]
        password = ''.join(temp_list)
        result = pdfReader.decrypt(password)
        if result == 1:
            print(f"The password: {password}")
            break
        index[0] += 1
        inner_circle += 1
    circle += 1
    print(f'circle:{circle-1} end')
print(f'process done, the password lenth may longer than{circle}')
