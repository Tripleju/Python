#2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные
#  данные хранятся в отдельных текстовых файлах.

""" in
Enter the name of the file with the text:
'text_words.txt'
Enter the file name to record:
'text_code_words.txt'
Enter the name of the file to decode:
'text_code_words.txt'

out
aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

out in file
'text_words.txt'
aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
vbbwwPPuuuTTYyWWQQ

'text_code_words.txt'
5a29v4s3D3d2F4g2O3i2a1
1v2b2w2P3u2T1Y1y2W2Q
 """
from itertools import count, groupby, starmap
from math import prod
from os import path   #exists

file_input=input('Enter the name of the file with the text: ')
file_record=input('Enter the file name to record: ')
file_decode=input('Enter the name of the file to decode: ')
my_list1='aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa'
my_list2='vbbwwPPuuuTTYyWWQQ'

print(my_list1)
print(my_list2)
def code_list(my_list):
    for char, same in groupby(my_list):
        count=sum(1 for _ in same)
        yield str(count)+char

compress_res1=''.join(code_list(list(my_list1)))
compress_res2=''.join(code_list(list(my_list2)))

def decrypt(str_):
    str_numb = ''
    str_lett = ''
    for i in str_:
        if i.isalpha():
            str_lett += i
            str_numb += ' '
        else:
            str_numb += i
    list_num = list(map(int, str_numb.split()))
  
    return ''.join([l*n for l,n in zip(str_lett, list_num)]) #как применить здесь starmap так и не поняла пока, то что поняла показалось долго
 
decrypt_res1=decrypt(compress_res1)
decrypt_res2=decrypt(compress_res2)


with open(file_input,'a',encoding='utf-8') as in_f:
    in_f.write(str(my_list1))
    in_f.write('\n')
    in_f.write(str(my_list2))
    in_f.write('\n')
    

with open(file_record,'a',encoding='utf-8') as record_f:
    record_f.write(compress_res1)
    record_f.write('\n')
    record_f.write(compress_res2)
    record_f.write('\n')

#записываю результат декодинга тоже в файл, хотя в задании 
# не указано. но это пригодится если 3й файл будет указан на входе отличным от второго
with open(file_decode,'a',encoding='utf-8') as decode_f:
    decode_f.write(decrypt_res1)
    decode_f.write('\n')
    decode_f.write(decrypt_res2)
    decode_f.write('\n')
 
 #что проверять через os.path.exist не поняла в данном случае. файлики же заново создаются

