s = '*' + '123321' * 100 + '+' #задаем произвольную строку(работает действительно на любой)
#фактически алгоритм работает так, что он как бы сортирует знаки, чтобы получилась
#строка вида 1111...111*3333...333+22222.2222
while '21' in s or '31' in s or '23' in s  :
    if '21' in s:
        s = s.replace('21', '12',1)
    if '31' in s:
        s = s.replace('31', '13',1)
    if '23' in s:
        s = s.replace('23', '32',1)


    if '3*' in s:
        s = s.replace('3*', '*3',1)
    if '2*' in s:
        s = s.replace('2*', '*2',1)
    if '*1' in s:
        s = s.replace('*1', '1*',1)

    if '+3' in s:
        s = s.replace('+3', '3+', 1)
    if '2+' in s:
        s = s.replace('2+', '+2', 1)
    if '+1' in s:
        s = s.replace('+1', '1+',1)

    if '+*' in s or '*+' in s:
        s = s.replace('*', '')
        s = '*' + s


s = str(eval(s)) #Эта уже готовая функция считает значение строки. Именно на знании
#этой функции построена вся задача. Без неё было бы в разы труднее
c185 = c370 = 0 # водим счётчики для 185 и 370, а потом считаем разницу в их количестве
for j in range(len(s)-2):
    if s[j] =='3' and s[j+1] == 7 and s['j+2'] == 0:
        c370+=1
    if s[j] =='1' and s[j+1] == 8 and s['j+2'] == 5:
        c185+=1

print(c370 - c185)
