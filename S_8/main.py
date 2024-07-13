def best_workers(lst):

    workers_department={}
   
    
    for i in lst:
        infos=i.split()
        bonus=int(infos[3])
        department=infos[4][0]
        
        if bonus>0 and department in workers_department:
            workers_department[department]+=1


        elif department not in workers_department:
           workers_department[department]=1


    max_bonus=max(workers_department.values())
    group=[i for i, val in workers_department.items() if val==max_bonus]
    
    for i in group:
        print(i)



employees=[]
counts=int(input("Enter number of employees: "))
for i in range(counts):
    i=input("Enter information in this order [Name, position, salary, bonus and department] ")
    employees.append(i)


file_name=input("enter file name: ")
with open(file_name,"w")  as f:
    for i in employees:
        f.write(f"{i}"'\n')


with open(file_name,"r") as f:
    line=f.readlines()

line=[i.strip() for i in line]

best_workers(line)
