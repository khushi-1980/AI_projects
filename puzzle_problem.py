def print_in_format(matrix):
    for i in range(9):
        if i%3==0 and i>0:
            print(" ")
        print(str(matrix[i])+" ",end=" ")
        
def count(s):
    c=0
    ideal=[1 ,2 ,3,
           4 ,5 ,6 ,
           7 ,8 ,0 ]
    for i in range(9):
        if s[i]!=0 and s[i]!=ideal[i]:
            c+=1
    return c
    
def move(ar,p,st):
    rh=99  #  dummy value
    store_state=st.copy()
    for i in range(len(ar)):
        dupe_state=st.copy()
        temp=dupe_state[p]
        dupe_state[p]=dupe_state[ar[i]]
        dupe_state[ar[i]]=temp
        
        trh=count(dupe_state)      
        print("value of p",p ,"value of i",i)
        print("before checking condition of trh ",store_state,trh,"rh",rh)
        if trh<rh:
            rh=trh
            store_state=dupe_state.copy()
        print("after checking the condition store_state",store_state,trh,"rh",rh)
    return store_state,trh

state=[1 ,2 ,3 ,
       0 ,5 , 6,
       4 ,7 ,8 ]
h=count(state)
level=1
print("\n------------------Level"+str(level)+"-------------------")
print_in_format(state)
print("\n Heuristic value(misplaced):"+str(h))

while h>0:
    pos=int(state.index(0))
    print("pos",pos)
    level+=1
    if pos==0:
        arr=[1 ,3 ]
        state,h=move(arr,pos,state)
    elif pos==1:
        arr=[0 ,2 ,4 ]
        state,h=move(arr,pos,state) 
    elif pos==2:
        arr=[1 ,5 ]
        state,h=move(arr,pos,state)
    elif pos==3:
        arr=[0 ,4 ,6 ]
        state,h=move(arr,pos,state) 
    elif pos==4:
        arr=[1 ,3 ,5 ,7 ]
        state,h=move(arr,pos,state)
    elif pos==5:
        arr=[2 ,4 ,8 ]
        state,h=move(arr,pos,state) 
    elif pos==6:
        arr=[3 ,7 ]
        state,h=move(arr,pos,state)
    elif pos==7:
        arr=[4 ,6 ,8 ]
        state,h=move(arr,pos,state) 
    elif pos==8:
        arr=[5 ,6 ]
        state,h=move(arr,pos,state)         
    print("\n------------------Level"+str(level)+"-------------------")
    print_in_format(state)
    print("\n Heuristic value(misplaced):"+str(h))
        
        
        