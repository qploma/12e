s = '1' + '0' * 55  + '1' * 3 + '0' *50 +'11' #задаем строку и переписываем алгоритм
while '122' in s or '001' in s:
    if '122' in s:
        s = s.replace('122', '01', 1)
    else:
        s = s.replace('001', '12',1)
print(s) #выводим строку, это число в троичной сс, далее дорешивается руками