#TAKE INPUT
old = []
process = []
print("Enter The Number of Processes")
n = int(input())
print("Please select the time quantum for the ")
gh = int(input())
print("Enter Arrival Time, Burst Time and Priority Of Each Process")
for i in range(1,n+1):
    print(f"For P{i}")
    k = list(map(int,input().split()))
    old.append([i-1,k[0],k[1]])
    process.append([i-1,k[0],k[1]])

comp_time = 0
comp = list(range(n))
con = 0
que = []
prev_comp = 0
val = False
opp = []

process.sort(key=lambda x:x[1])
print("\n\nGnatt chart is as follows:\n")
while con<n:
    buffer = []
    for i in process:
        if i[1] in range(prev_comp,comp_time+1):
            buffer.append(i)
    for g in buffer:
        process.remove(g)
        que.append(g)
    if val:
        que.append(opp)

    if len(que) == 0:
        print(f"Time {comp_time} --> Not Allocated")
        comp_time += 1
        continue

    else:
        prev_comp = comp_time
        if que[0][2] - gh <= 0:
            comp_time += que[0][2]
            comp[que[0][0]] = comp_time
            print(f"Time {prev_comp}-{comp_time} --> Process {que[0][0]+1}")
            que.pop(0)
            con += 1
            val = False
        else:
            que[0][2] -= gh
            comp_time += gh
            print(f"Time {prev_comp}-{comp_time} --> Process {que[0][0]+1}")
            opp = que.pop(0)
            val = True
    
print("\n\nThe answer is:\n\n")
print("-"*61)
print("|Process    |Arrival    |Burst      |TurnAround |Waiting    |")
print("-"*61)
wait = []
turn = []
for x in old:
    print(f"|Process {x[0]+1}" + " "*(3-len(str(x[0]))),end = "|")
    print(f"{x[1]}" + " "*(11-len(str(x[1]))),end = "|")
    print(f"{x[2]}" + " "*(11-len(str(x[2]))),end = "|")
    llp = comp[x[0]]
    turn.append(llp - x[1])
    wait.append(llp - x[1] - x[2])
    print(f"{llp - x[1]}" + " "*(11-len(str(llp - x[1]))),end = "|")
    print(f"{llp - x[1] - x[2]}" + " "*(11-len(str(llp - x[1] - x[2]))),end = "|\n")
    print("-"*61)
                
print(f"\nAverage TurnAround Time : {sum(turn)/n}")
print(f"\nAverage Waiting Time : {sum(wait)/n}")

    
