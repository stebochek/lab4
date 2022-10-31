from random import *
# блок генератора ключа

def key(num):
    block1 = ''
    num = int(num) % 10
    for i in range(5):
        block1 += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'[randint(0, len('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') - 1)]
        block = block1 + '-'
        temp = block1.replace(block1[randint(0, len(block1) - 1)], '', 1)
    for i in range(3):
        if i == 2:
            temp = temp[num:] + temp[:num]
            block += temp
        elif i % 2 == 0:
            temp = temp[num:] + temp[:num]
            block += temp + '-'
        elif i % 2 == 1:
            temp = temp[-num:] + temp[:-num]
            block += temp + '-'
        temp = temp.replace(temp[randint(0, len(temp) - 1)], '', 1)
    return block
