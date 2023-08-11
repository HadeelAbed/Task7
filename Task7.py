#1
def number_pattern(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(j,end='',)
        print()
# num_of_row=input('Enter num of rows : ')
# number_pattern(int(num_of_row))
# #*********
#
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
def main():
    user_input = input("Enter a word: ")
    reversed_word = user_input[::-1]
    print("Reversed word:", reversed_word)
main()
print()

# #*********
#
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
def main():
    for i in range(1, 11):
        print(i * 5, end=" ")
main()
print()

# #*********
#7
def main():
    Limit_number = int(input("Enter the limit number: "))
    Max_display_on_screen = int(input("Enter the max display count: "))
    Target_number = int(input("Enter the target number: "))

    count = 0
    current_number = Target_number

    while current_number <= Limit_number and count < Max_display_on_screen:
        print(current_number, end=" ")
        count += 1
        current_number += Target_number
main()
print()