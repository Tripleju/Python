import model_mult as model_mult
import model_sum as model_sum


def ch_operation():
    operation=int(input("Choose operation:\n 1 - sum\n 2 - sub\n 3 - mult\n 4 - div\n 5 - pow\n 6 - sqrt\n 0 - previouse menu\n" ))
    # dict_operation=dict([(1,'sum'),(2,'sub'),(3,'mult'),(4,'div'),(5,"pow"),(6,'sqrt'),(0,'previose menu')])
    dict_models=dict([(1,model_sum),(2,'model_sub'),(3,model_mult),(4,'model_div'),(5,"model_pow"),(6,'model_sqrt')])
    print(operation)
    return dict_models.get(operation)

# print(ch_operation())

x=0
y=0
d=0
def init(a,c,b,f):
    global x
    # global xj
    global y
    # global yj
    global d

    x=complex(a,c)
    y=complex(b,f)
    return x,y


def get_complex_value():
    real_part1=int(input('Enter 1 real part: '))
    im_part1=int(input('Enter 1 imaginary part: '))
    real_part2=int(input('Enter 2 real part: '))
    im_part2=int(input('Enter 2 imaginary part: '))
    print(f"value 1= {complex(real_part1,im_part1)}")
    print(f"value 2= {complex(real_part2,im_part2)}")
    return real_part1,im_part1,real_part2,im_part2
# CV=get_complex_value()
# # print(CV)
# # print(CV[2])
# value1=init(CV[0],CV[1],CV[2],CV[3])[0]
# value2=init(CV[0],CV[1],CV[2],CV[3])[1]
# print(init(CV[0],CV[1],CV[2],CV[3])[0])

# print(value1)
# print(value2)

def do_it():
    return x+y

# print(do_it())

def get_complex_value1():
    real_part1=int(input('Enter 1 real part: '))
    im_part1=int(input('Enter 1 imaginary part: '))
    real_part2=int(input('Enter 2 real part: '))
    im_part2=int(input('Enter 2 imaginary part: '))
    value1= complex(real_part1,im_part1)
    value2= complex(real_part2,im_part2)
    print(f"value 1= {value1}")
    print(f"value 2= {value2}")
    return [value1, value2]

value_a=get_complex_value1()[0]
print((value_a))