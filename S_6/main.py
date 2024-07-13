def num_neighbors(lst):
    result = []
    for i in range(len(lst) - 1):
        if (lst[i] >= 0 and lst[i + 1] >= 0) or (lst[i] < 0 and lst[i + 1] < 0):
            result.append((lst[i], lst[i + 1]))
    return result

lst=[]
num=int(input("Enter: "))
for i in range(num):
    nums=int(input(f"{i+1}-sonni kiriting "))
    lst.append(nums)

result=num_neighbors(lst)
print(result)
