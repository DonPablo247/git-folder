#code that stores arg num of even num in a list
#and arg number of odd numbers in another list

def oddeven_num(*args):
    evenlist =[ n for n in args if n % 2==0]
    oddlist =[n for n in args if n % 2==1]
    return f'evennumbers:{evenlist}\oddnumbers: {oddlist}'
inputvalues = oddeven_num(1,2,3,4,5,6,7,8,9,10)
print(inputvalues)