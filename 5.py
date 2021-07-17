def v2(n): #функция для перевода в двоичную сс
    a = int(n)
    nm2 = ''
    while a > 0:
        nm2 = str(a%2) + nm2
        a = a // 2
    return(nm2)

def v10(n): #функция для перевода в десятичную сс
    s = n
    a = int(n)
    ch = 0
    ste = 0
    for j in range(len(s)-1,-1,-1):
        ch = ch + int(s[j]) * (2**(ste))
        ste +=1
    return(str(ch))

s = '2' + '8' * 150 + '3' # задаем строку
while '87' in s or '882' in s or '8883' in s:
    if '8883' in s: #если встретилось 8883, то переводим в 2сс, как в условии
        s = v2(int(s))
        while '1111' in s: #работаем с двоичной строкой
            s = s.replace('000', '1')
            s = s.replace('111', '0')
        s = v10((s)) #переводим назад в 10сс, а затем меняем цифры на такие, как сказано в условии
        s = s.replace('0', '2')
        s = s.replace('4', '8')
        s = s.replace('6', '2')
        s = s.replace('1', '8')
        s = s.replace('3', '8')
        s = s.replace('5', '3')
        s = s.replace('9', '8')
    elif '87' in s:
        s = s.replace('87','2', 1)
    elif '882' in s:
        s = s.replace('882', '3', 1)

print(s)
