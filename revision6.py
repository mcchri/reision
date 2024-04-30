def sum(li):
    fi = li.pop(0)
    if len(li) == 0:
        return 0
    else:
        return sum(li) + fi

list_input = [1,2,4,5,3]
print(sum(list_input))

def factorial(num):
    if num == 0:
        return 1
    else:
        return factorial(num-1) * num

num = 4
print(factorial(num))

def sum_num(num):
    if num == 0:
        return 0
    else:
        return factorial(num-1) + num

num = 4
if num > 0:
    print(sum_num(num))
    
def expo(a,b):
    
    if b == 0:
        return 1
    else:
        return expo(a,b-1) * a

a=5
b=2
print(expo(a,b))

def has_digit(st):
    last_st = st[0:1]
    st = st.strip(last_st)
    if last_st.isdigit():
        return True
    elif len(st) == 0:
        return False
    else:
        return has_digit(st)

string = "asbgk1"
print(has_digit(string))