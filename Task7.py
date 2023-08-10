#1
def number_pattern(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(j,end='',)
        print()
num_of_row=input('Enter num of rows : ')
number_pattern(int(num_of_row))
#*********

#2
def sum_num(num1):
    sum=0
    for i in range(1,num1+1):
        sum+=i
    return sum
number=input('Enter the number : ')
print(f'Sum is : {sum_num(int(number))}')
#*********

#3
name=input('Enter your name : ')
def print_name(name):
    for i in range(0,len(name)):
        for j in range(0,i+1):
            print(name[j],end='')
        print()
        if i==len(name)-1:
                     #range(0,6)
            for x in range(len(name)-1,-1,-1):#x=6
                for j in range(x):
                    print(name[j],end='')
                print()
print_name(name)
#*********

##4
word=input('Enter a word to reverse  : ')
def word_reverse(word):
    for i in range(len(word)-1,-1,-1):
        print(word[i],end='')

word_reverse(word)
print()
#*********

##5
range_num=int(input('Enter range : '))
def print_range(range_of_num):
    while 1<= range_of_num:
        print(range_of_num,' ',end='')
        range_of_num-=1

print_range(range_num)
print()
#*********

#6
def  multiples_of_5():
    for i in range(1,11):
        print(i*5,' ',end='')
print('the first 10 multiples of 5 ')
multiples_of_5()
print()
#*********

#7
Limit_number=int(input('Enter the Limit number: '))
Max_display_on_screen=int(input('Enter the maximum outputs to display(Max_display_on_screen) : '))
Target_number=int(input('Enter the Target number :'))
def num_display(Limit,Max,Target):#300,8,4
    num = 1
    for i in range(Target,Limit+1):
        if(num<=Max):
            print(num*Target,' ',end='')
            num+=1
        else:
            break
num_display(Limit_number,Max_display_on_screen,Target_number)