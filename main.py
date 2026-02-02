import mysql.connector as mc
Conn=mc.connect(host="localhost",user="JIBB",password="11062023",database="Supermarket")
cur=Conn.cursor()


print("                      Welcome to Grand Super Market                              ")                                                  #BEGINNING OF SHOPPING
p=int(input("\n\n\nEnter Your Phone Number:"))
l=str(p)
ll=len(l)
count=1
while count==1:
    if ll>=11:
        print("\nEnter a valid phone number")
        q=int(input("Enter Your Phone Number:"))
        count=0
    elif ll<=9:
        print("\nEnter a valid phone number")
        q=int(input("Enter Your Phone Number:"))
        count=0
    else:
        break
    
while True:
    try:
        bg=float(input('Please enter your budget:'))
        if bg<=0:
            print("\nEnter valid budget")  
            continue
        else:
            s1=bg
            Sum=s1

#ENTRY OF BUDGET
    except ValueError:
        print('\nPrint budget as a number')
        continue
    else:
        break
a={'PName':[],'QTY':[],'PRICE':[],'Total':[]}
b=list(a.values())
na=b[0]
qu=b[1]
pr=b[2]
tot=b[3]
lst5=list(pr)

q=0

#ASKING USER FOR INPUT ON HOW TO PROCEED
while True:
    try:
        ch=int(input('\n1.Add item\n2.Proceed to checkout\n3.Check Item list\n4.Delete an item\n5.Reduce QTY of items\nEnter your choice:'))
    except ValueError:
        print('\nError:choose from the given options')
        continue
    else:
#ADDING ITEMS TO THE CART
        if ch==1 and s1>0:                                
            
            Conn=mc.connect(host="localhost",user="JIBB",password="11062023",database="Supermarket")
            cur=Conn.cursor()
            qr="Select PNAME from products"
            cur.execute(qr)
            lst=[]
            d=cur.fetchall()
            for r in d:
                str1=list(r)
                lst.append(str1[0])

            count=1
            while count==1:
                pn=input('\n\n\nEnter product name:')    
                qw=str(pn)
                L=qw.title()
                D=L+"%';"                                                                                                          
#RECEIVING PRODUCT NAME
                if L in lst:    
                    count=0
                elif L not in lst:
                    print("Required item not in Stock. Please select from item list")
                    Conn=mc.connect(host="localhost",user="JIBB",password="11062023",database="Supermarket")
                    cur=Conn.cursor()
                    qry="Select * from PRODUCTS;"
                    cur.execute(qry)
                    d=cur.fetchmany(50)
                    print('PID ','---------','PNAME','----------','QTY')                   
#LIST OF ALL ITEMS AVAILABLE IN THE STORE
                    for r in d:
                        t=list(r)
                        strrr=str(t[2])
                        e=len(strrr)
                        o=len(t[1])                                                                                               
#CREATION OF LIST TABLE
                        u=len(t[0])
                        l=10-o
                        v=8-e
                        k=8-u

                        if len(t[1])<=10:
                            T=str(t[0])+(' '*k)
                            T2=str(t[1])+(' '*l)
                            T3=str(t[2])+(' '*v)
                            print(T,'     ',T2,'     ',T3)
                
                        elif len(t[1])>10:
                            print(t[0],'     ',t[1],'     ',t[2])
                        
                        Conn.close()
                    pn=input('\n\nEnter product name:')
                    qw=str(pn)
                    L=qw.title()
                    D=L+"%';"
                    count=1

                Conn=mc.connect(host="localhost",user="JIBB",password="11062023",database="Supermarket")
                cur=Conn.cursor()
                if L==L:
                    P=L[:2]
                    QR="Select * from "+L+";"
                    cur.execute(QR)
                    d=cur.fetchmany(10)
                    print("\n"+P+'ID ','---------',P+'NAME','----------','QTY','---------','PRICE','-----','DISCOUNT')
                    for r in d:
                        t=list(r)
                        strr=str(t[3])
                        strrr=str(t[2])
                        e=len(strrr)
                        o=len(t[1])
                        i=len(strr)
                        u=len(t[0])
                        x=8-i
                        l=10-o
                        v=8-e
                        k=8-u

                        if len(t[1])<=10:
                            T=str(t[0])+(' '*k)
                            T2=str(t[1])+(' '*l)
                            T4=str(t[3])+(' '*x)
                            T3=str(t[2])+(' '*v)
                            print(T,'      ',T2,'      ',T3,'     ',T4,'    ',t[4])
                            count=1
                        
                        elif len(t[1])>10:
                            l=15-o
                            T=str(t[0])+(' '*k)
                            T2=str(t[1])+(' '*l)
                            T4=str(t[3])+(' '*x)
                            T3=str(t[2])+(' '*v)
                            print(T,'      ',T2,' ',T3,'     ',T4,'    ',t[4])
                            count=1   
                    Conn=mc.connect(host="localhost",user="JIBB",password="11062023",database="Supermarket")
                    cur=Conn.cursor() 
                    qr="Select "+P+"NAME from "+L+";"
                    cur.execute(qr)
                    LST=[]
                    d=cur.fetchall()
                    for r in d:
                        STR=list(r)
                        LST.append(STR[0])
            
                    while count==1:    
                        bn=input("\nEnter Type of "+L+" needed:")
                        qw=str(bn)
                        LL=qw.title()
                        DD=LL+" "+L
                        D=DD+"%';"
                        print(DD)
                        print(LST)
                        if DD in LST:
                            count=0
                        else:
                            print("\n\nRequired item not in Stock. Please select from item list")
                            print("\n"+P+'ID ','---------',P+'NAME','----------','QTY','---------','PRICE','-----','DISCOUNT')
                            qr="Select * from "+L+";"
                            cur.execute(qr)
                            d=cur.fetchall()
                            for r in d:
                                t=list(r)
                                strr=str(t[3])
                                strrr=str(t[2])
                                e=len(strrr)
                                o=len(t[1])
                                i=len(strr)
                                u=len(t[0])
                                x=8-i
                                l=10-o
                                v=8-e
                                k=8-u

                                if len(t[1])<=10:
                                    T=str(t[0])+(' '*k)
                                    T2=str(t[1])+(' '*l)
                                    T4=str(t[3])+(' '*x)
                                    T3=str(t[2])+(' '*v)
                                    print(T,'      ',T2,'      ',T3,'     ',T4,'    ',t[4])
                                    count=1
                                
                                elif len(t[1])>10:
                                    l=15-o
                                    T=str(t[0])+(' '*k)
                                    T2=str(t[1])+(' '*l)
                                    T4=str(t[3])+(' '*x)
                                    T3=str(t[2])+(' '*v)
                                    print(T,'      ',T2,' ',T3,'     ',T4,'    ',t[4])
                                    count=1    
           
            Conn=mc.connect(host="localhost",user="JIBB",password="11062023",database="Supermarket")
            cur=Conn.cursor()
            qr="Select QTY from "+L+" where "+P+"NAME LIKE '"+D
            cur.execute(qr)    
            data=cur.fetchone()
            for qty in data:
                
                print("Total Stock left is",qty)                                                     
#RECEIVING QUANTITY OF PRODUCT
   
            Conn=mc.connect(host="localhost",user="JIBB",password="11062023",database="Supermarket")
            cur=Conn.cursor()
            pr="Select PRICE from "+L+" where "+P+"NAME LIKE '"+D
            cur.execute(pr)
            Data=cur.fetchone()
            for Row in Data:
                print("Price is",Row)   
            Conn.close()                                         
#RECEIVING THE PRICE OF THE PRODUCT
            Conn=mc.connect(host="localhost",user="JIBB",password="11062023",database="Supermarket")
            cur=Conn.cursor()
            dr="Select DISCOUNT from "+L+" where "+P+"NAME LIKE '"+D
            cur.execute(dr)
            
            DATA=cur.fetchone()
            for dis in DATA:
                print("Discount available is",dis,"%")                                            
#CHECKING FOR DISCOUNT ON SPECIFIC ITEM
            print("Amount remaining:Rs.",s1)
                

               
            while True:
                try:
                    q=int(input("\nQuantity required is :"))
                except ValueError:
                    print('Print number as QTY')                                                   
#QUANTITY REQUIRED BY USER
                    continue
                else:
                    break                                                                                                    
            while q>qty or q<=0:
                if q>qty:
                    print("\nNot enough stock")
                    q=int(input("Quantity required is :"))
                elif q<=0:                                                                       
#INCASE QUANTITY REQUIRED IS GREATER THEN STOCK OR QUANTITY REQUIRED IS ZERO
                    print("\nZero or lesser items cannot be added to cart")
                    q=int(input("Quantity required is :"))
                else:
                    continue
                
            else:
                sum=((Row*q)-((Row*(dis/100))*q))                                                   
#TOTAL PRICE OF ITEM OF CERTAIN QUANTITY AND DISCOUNT APPLIED
            lol=str(q)
            Conn=mc.connect(host="localhost",user="JIBB",password="11062023",database="Supermarket")
            cur=Conn.cursor()
            Qr="Update "+L+" set QTY=QTY-"+lol 
            qr=Qr+" where "+P+"NAME LIKE '"+D                                                      
#UPDATING STOCK TO THE TABLE
            cur.execute(qr)
            Conn.commit()




            if sum>s1:
                print('Amount is out of budget')                                                    
 #IF TOTAL PRICE IS MORE THEN BUDGET REMAINING
                continue
            else:
                if LL in na:
                    qr="Select Price from "+L+" where "+P+"NAME LIKE '"+D
                    cur.execute(qr)
                    Data=cur.fetchone()
                    for Qty in Data:
                        TTT=Qty
                    Ind=na.index(LL)
                    na[Ind]=LL    
                    QTYY=qu[Ind]                                                            
#INCASE USER INPUTS SAME ITEM AGAIN
                    q+=QTYY
                    qu[Ind]=q
                    sum=((Row*q)-((Row*(dis/100))*q))
                    lst5[Ind]=TTT
                    tot[Ind]=sum
                    s1=s1-sum
                    print('\nAmount left',s1)
                    print("\nItems in cart")
                    for i in na:
                        t=list(r)
                        u=len(i)
                        k=8-u
                        T=("|")+str(i)+(' '*k)+("|")
                        print(T)

                else:
                    if sum<=s1:
                        qr="Select Price from "+L+" where "+P+"NAME LIKE '"+D
                        cur.execute(qr)
                        Data=cur.fetchone()
                        for Qty in Data:
                            TTT=Qty
                        sum=((Row*q)-((Row*(dis/100))*q))
                        Conn.commit
                        str2=str(LL)
                        Tot=tot.append(sum)                                             
#ENTERING VALUES INTO THE NAME,QUANTITY,PRICE,TOTAL LISTS
                        Na=na.append(str2)
                        Qu=qu.append(q)
                        Pr=lst5.append(TTT)
                        s1=s1-sum
                        print('\nAmount left',s1)
                        print("\nItems in cart")
                        for i in na:
                            t=list(r)
                            u=len(i)
                            k=8-u
                            T=("|")+str(i)+(' '*k)+L+("|")
                            print(T)
#IF USER WANTS TO EXIT TO FINAL CHECKOUT                
        elif ch==2:
            break
        elif s1<=0:
            print('\nNo budget')
            break
#IF USER WANTS TO CHECK THE LIST OF ITEMS IN THE STORE      
        elif ch==3:
            Conn=mc.connect(host="localhost",user="JIBB",password="11062023",database="Supermarket")
            cur=Conn.cursor()
            qry="Select * from PRODUCTS;"
            cur.execute(qry)
            d=cur.fetchmany(50)
            print('PID ','---------','PNAME','----------','QTY')                   
#LIST OF ALL ITEMS AVAILABLE IN THE STORE
            for r in d:
                t=list(r)
                strrr=str(t[2])
                e=len(strrr)
                o=len(t[1])                                                                                              
                u=len(t[0])                  
                l=10-o
                v=8-e                                                                                                     
#CREATION OF LIST TABLE
                k=8-u

                if len(t[1])<=10:
                    T=str(t[0])+(' '*k)
                    T2=str(t[1])+(' '*l)
                    T3=str(t[2])+(' '*v)
                    print(T,'     ',T2,'     ',T3)
                
                elif len(t[1])>10:
                    print(t[0],'     ',t[1],'     ',t[2])
            Conn.close()
#REMOVAL OF ITEM FROM THE CART
        elif ch==4:
            Conn=mc.connect(host="localhost",user="JIBB",password="11062023",database="Supermarket")
            cur=Conn.cursor()
            qr="Select PNAME from products"
            cur.execute(qr)
            lst=[]
            d=cur.fetchall()
            for r in d:
                str1=list(r)
                lst.append(str1[0])

            count=1
            while count==1:
                pn=input('\nEnter product name:')    
                qw=str(pn)
                L=qw.title()
                D=L+"%';"                                        
                if L in lst:
                    count=0
                else:
                    Y="Yes"
                    N="No"
                    print("Required item not in Stock. Please select from item list")                                                
#IF ITEM REQUIRED NOT IN STOCK
                    ans=input("Do you want to view the item list(Yes/No):")
                    if ans==Y:
                        Conn=mc.connect(host="localhost",user="JIBB",password="11062023",database="Supermarket")
                        cur=Conn.cursor()
                        qry="Select * from PRODUCTS;"
                        cur.execute(qry)
                        d=cur.fetchmany(50)
                        print('PID ','---------','PNAME','----------','QTY','---------','PRICE','-----','DISCOUNT')                   
#LIST OF ALL ITEMS AVAILABLE IN THE STORE
                        for r in d:
                            t=list(r)
                            strr=str(t[3])
                            strrr=str(t[2])
                            e=len(strrr)
                            o=len(t[1])                                                                                               
                            i=len(strr)
                            u=len(t[0])
                            x=8-i
                            l=10-o
                            v=8-e
                            k=8-u
                                                                                                                                       
#CREATION OF LIST TABLE
                            if len(t[1])<=10:
                                T=str(t[0])+(' '*k)
                                T2=str(t[1])+(' '*l)
                                T4=str(t[3])+(' '*x)
                                T3=str(t[2])+(' '*v)
                                print(T,'     ',T2,'     ',T3,'     ',T4,'     ',t[4])
                
                            elif len(t[1])>10:
                                print(t[0],'     ',t[1],'     ',t[2],'     ',t[3],'     ',t[4])
                    elif ans==N:
                            continue
                    else:
                            print("Enter from the given options")
                            continue
            Conn=mc.connect(host="localhost",user="JIBB",password="11062023",database="Supermarket")
            cur=Conn.cursor()
            qw=str(pn)
            L=qw.title()
            qty=0
            pr="Select PRICE from PRODUCTS where PNAME LIKE '"+D
            cur.execute(pr)
            Data=cur.fetchone()
            for Row in Data:
                mnm=Row
            q=qty                                                                                                                  
#DELETING ITEM FROM CART
            for i in range(1):
                Ind=na.index(L)
                Pr=lst5.remove(lst5[Ind])
                Qu=qu.remove(qu[Ind])
                Na=na.remove(na[Ind])
                Tot=tot.remove(tot[Ind])
            print("Item has been deleted")
            print("\nItems in cart")
            for i in na:
                        t=list(r)
                        u=len(i)
                        k=8-u
                        T=("|")+str(i)+(' '*k)+("|")
                        print(T) 
#REDUCING QUANTITY OF AN ITEM
        elif ch==5:
            Conn=mc.connect(host="localhost",user="JIBB",password="11062023",database="Supermarket")
            cur=Conn.cursor()
            qr="Select PNAME from products"
            cur.execute(qr)
            lst=[]
            d=cur.fetchall()
            for r in d:
                str1=list(r)
                lst.append(str1[0])

            count=1
            while count==1:
                pn=input('\n\n\nEnter product name:')    
                qw=str(pn)
                L=qw.title()
                D=L+"%';"                                        
                if L in lst:
                    count=0
                else:
                    Y="Yes"
                    N="No"
                    print("Required item not in Stock. Please select from item list")                                                 
#INCASE ITEM TO BE REDUCED NOT IN STOCK
                    ans=input("Do you want to view the item list(Yes/No):")
                    if ans==Y:
                        Conn=mc.connect(host="localhost",user="JIBB",password="11062023",database="Supermarket")
                        cur=Conn.cursor()
                        qry="Select * from PRODUCTS;"
                        cur.execute(qry)
                        d=cur.fetchmany(50)
                        print('PID ','---------','PNAME','----------','QTY','---------','PRICE','-----','DISCOUNT')                   
                        
#LIST OF ALL ITEMS AVAILABLE IN THE STORE
                        for r in d:
                            t=list(r)
                            strr=str(t[3])
                            strrr=str(t[2])
                            e=len(strrr)
                            o=len(t[1])                                                                                               
#CREATION OF LIST TABLE
                            i=len(strr)
                            u=len(t[0])
                            x=8-i
                            l=10-o
                            v=8-e
                            k=8-u

                            if len(t[1])<=10:
                                T=str(t[0])+(' '*k)
                                T2=str(t[1])+(' '*l)
                                T4=str(t[3])+(' '*x)
                                T3=str(t[2])+(' '*v)
                                print(T,'     ',T2,'     ',T3,'     ',T4,'     ',t[4])
                
                            elif len(t[1])>10:
                                print(t[0],'     ',t[1],'     ',t[2],'     ',t[3],'     ',t[4])
                    elif ans==N:
                            continue
                    else:
                            print("Enter from the given options")
                            continue
            Conn=mc.connect(host="localhost",user="JIBB",password="11062023",database="Supermarket")
            cur=Conn.cursor()

            pr="Select PRICE from PRODUCTS where PNAME LIKE '"+D
            cur.execute(pr)
            Data=cur.fetchone()
            for Row in Data:
                mnm=Row
                Conn.close()
            Conn=mc.connect(host="localhost",user="JIBB",password="11062023",database="Supermarket")
            cur=Conn.cursor()
            dr="Select DISCOUNT from PRODUCTS where PNAME LIKE '"+D
            cur.execute(dr)
            
            DATA=cur.fetchone()
            for dis in DATA:
                MNM=dis
            Qty=int(input("Enter Qty you would want to reduce:"))
            ind=na.index(L)
            q=qu[ind]
            qty=q-Qty
            if qty>0:
                Sum=s1+((mnm*Qty)-((mnm*(MNM/100))*Qty))
                print("\nItem Quantity has been reduced")
                print("\nItems in cart")
                for i in na:
                        t=list(r)
                        u=len(i)
                        k=8-u
                        T=("|")+str(i)+(' '*k)+("|")
                        print(T) 
            elif qty==0:
                print("\nItem has been removed from cart")
                Sum=s1+((mnm*Qty)-((mnm*(MNM/100))*Qty))
            else:
                print(0-qty," items will be sold to the store")
                Sum=s1-((mnm*(qty*Qty))-((mnm*(MNM/100))*(qty*Qty)))
            s2=((mnm*qty)-((mnm*(MNM/100))*qty))
            print("Amount left is",Sum)
            Sum=sum
            lol=str(Qty)
            Conn.close()

            Conn=mc.connect(host="localhost",user="JIBB",password="11062023",database="Supermarket")
            cur=Conn.cursor()
            Qr="Update PRODUCTS set QTY=QTY+"+lol 
            qr=Qr+" where PNAME LIKE '"+D
            cur.execute(qr)
            Conn.commit()
            for pn in na:
                if pn in na:
                    continue
                else:
                    Na=na.append(L)
            for i in range(1):
                ind=na.index(L)
                qu[ind]=qty                                                                                       
#REDUCTION OF THE QUANTITY OF AN ITEM
                tot[ind]=s2
                lst5[ind]=mnm
                      
            if qty==0:
                Na=na.remove(L)
                Qu=qu.remove(qty)                                                                       
#INCASE QTY REQUIRED AFTER REDUCING IS 0
                Pr=lst5.remove(mnm)
                Tot=tot.remove(s2)
            else:
                continue
                
        else:
            print("\nPlease select an option from the given list")
        
Conn.close()
#FINAL BILL AND CHECKOUT
print('\nAmount left:Rs.',s1)
print("-"*80)
print(" "*28,"Grand Super Market")
print(" "*25,"Phone Number:8147313177")                                                                 
print(" "*28,"GST:29AAMFGO467B1ZH")
print(" "*27,"FSSAI:11222334000555")
print("-"*80)
print("-"*80)
import datetime                                                                               
#FORMATION OF THE FINAL BILL 
     
m=current_time = datetime.datetime.now()
print("Bill No    Date          Time") 
print("-"*80)
print("P2486   ",m)
print('-'*80)
print('Item                   Price        Qty      Total Rs')                
print('-'*80) 
sumqu=0
sumtot=0
for i in range(len(na)):
    LEN=len(na[i])
    Len=len(str(lst5[i]))
    LeN=len(str(qu[i]))
    K=15-LEN
    M=4-Len
    B=3-LeN 
    print(na[i]," "*K,"       ",lst5[i]," "*M,"     ",qu[i]," "*B,"    ",tot[i])
    sumqu+=qu[i]
    sumtot+=tot[i]
print("-"*80)
print("Total Quantity                  ",sumqu,"\nGrand Total                               ",sumtot)
print("SGST 3.0%                                   ",(3/100*sumtot))
print("CGST 3.0%                                   ",(3/100*sumtot))
NS=sumtot+(3/100*sumtot)*2
print("Net Amount                                ",NS)
print("\n                 Thank You for shopping at Grand Super Market")
print("\n                              HAVE A NICE DAY")
print("-"*80)
#END OF SHOPPING