def sum_digits(num):
     sum_digit=sum(int(i) for i in str(abs(num)))
     return sum_digit

def my_sort(lst):
   sorted_list=sorted(lst,key=sum_digits)
   return sorted_list
   

lst=[]
while True:
    num=input("Enter numbers [Enter stop to break loop] ")
    if num=='stop':
        break
    try:
     number=int(num)
     lst.append(number)

    except ValueError:
       print("Enter only positive numbers")


sum_digits(number)
result=my_sort(lst)
print(result)
