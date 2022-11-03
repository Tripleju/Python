x=0
y=0
# d=''

def init(a,b):
    global x
    global y
    # global d
    x=a
    y=b


import user_interface as us_int


def do_it(d):

    if d=='/':
        value= x/y
    elif d=='//':
        value=x//y
    elif d=='%':
        value=x%y
    return value


def symb(d):
    symbol=d
    return symbol