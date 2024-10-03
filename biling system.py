items={1:"Tea",2:"Poha",3:"samosa",4:"vada-pav",5:"dosa",6:"idali",7:"misal",8:"pavbhaji"}
#var[key]
price={1:10,2:20,3:15,4:15,5:30,6:35,7:80,8:60}
ik=[]
qun=[]
print("-"*100)
print(f'{" "*40} Sai Hotel')
print("-"*100)
while True:
    print("""
                Menu
        1.Tea     2.Poha
        3.Samosa  4.Vada-Pav
        5.Dosa    6.idali
        7.Misal   8.Pavbhaji
    """)
    i=int(input("Enter Your Choice: "))
    q=int(input("Enter Quantity: "))
    ik.append(i)
    qun.append(q)
    ch=input("Do You Want To Continue: ")
    if ch=="n":
        print("-"*85)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format("ItemName","Quantity","Price","Amount"))
        print("-"*85)
        sum=0
        for i in range(len(ik)):
            print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(items[ik[i]],qun[i],price[ik[i]],qun[i]*price[ik[i]]))
            print("-"*85)
            sum=sum+qun[i]*price[ik[i]]
        print(f"Your Total Amount:{sum}\nThank You!Visit Again")
        break



    







