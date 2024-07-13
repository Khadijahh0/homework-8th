def sum_color(colors):
    if not colors:
        return 0
    
    color=colors[0]

    time=2
    for i in range(1,len(colors)):
        if colors[i]!=color:
            time+=1
            color=colors[i]

        time+=2   

    return time


colors=[]

while True:
    color=input("Enter color: [False to stop loop] ")
    if color=='false':
        break
    colors.append(color)

result=sum_color(colors)
print(result)
