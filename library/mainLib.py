import pandas as pd
import sys
import random
def bookId():
    a=random.randint(0,9)
    b=random.randint(0,9)
    c=random.randint(0,9)
    d=random.randint(0,9)
    return 'BOOK'+str(a)+str(b)+str(c)+str(d)

def memId():
    a=random.randint(0,9)
    b=random.randint(0,9)
    c=random.randint(0,9)
    d=random.randint(0,9)
    return 'MEM'+str(a)+str(b)+str(c)+str(d)
def login():
    user = input('Enter user name')
    pswd = input('Enter password')
    df = pd.read_csv('idpass.csv')
    df = df.loc[df['user'] == user]
    if df.empty:
        print('Invalid username/password')
        return False
    else:
        df = df.loc[df['pswd'] == pswd]
        if df.empty:
            print('invalid username/password')
            return False
        else:
            print('Welcome user')
            return True
def book():
    print('='*50)
    print('1. Add a book')
    print('2. Search a book')
    print('3. Delete a book')
    print('4. Display all book')
    print('5. previous menu')
    b = int(input('Enter your choice'))
    return b

def member():
    print('='*50)
    print('1. Add a member')
    print('2. Search a member')
    print('3. Delete a member')
    print('4. Display all member')
    print('5. previous menu')
    m = int(input('Enter your choice'))
    return m

def issue():
    print('='*50)
    print('1. Issue a book')
    print('2. Return a book')
    print('3. Display all issued book')
    print('4. To view a chart')
    print('5. previous menu')
    i = int(input('Enter your choice'))
    return i
    
def showMenu():
    print('='*50)
    print('My own library')
    print('1. Register of book')
    print('2. Register of member')
    print('3. book isssue') 
    print('4. Exit')
    ch = int(input('Enter your choice'))
    return ch

def addBook():
    bookid=bookId()
    print("book Id is = ",bookid)
    title=input("enter book name = ")
    auth=input("enter author name = ")
    pub=input("enter publiser name = ")
    edi=int(input("enter edition = "))
    cost=int(input("enter cost = "))
    cate=input("enter category = ")
    df = pd.read_csv('book.csv')
    n = df['bookid'].count()
    df.loc[n] = [bookid, title, auth, pub, edi, cost, cate]
    df.to_csv('book.csv', index = False)
    print('book added successfully')
    
def searchBook():
    title=input('enter title of book')
    cat=input('enter catagery of book')
    df = pd.read_csv('book.csv')
    if df3.empty:
        print('Not found')
    else:
        print(df3)

def bookDel():
    bname=input("enter book name = ")
    cat=input("enter catgoery = ")
    
def dispBookAll():
    df = pd.read_csv('book.csv')
    df2 = df.to_string(index=False)
    print(df2)
    
def addMem():
    memid=memId()
    print("Member Id is = ",memid)
    name=input("enter member name = ")
    cno=int(input("enter contact no. = "))
    bookis=0
    df = pd.read_csv('member.csv')
    n = df['memid'].count()
    df.loc[n] = [memid,name,cno,bookis]
    df.to_csv('member.csv', index = False)
    print('member added successfully')

def bookIs():
    bname=input("enter book name = ")
    cat=input("enter catgoery = ")
    df = pd.read_csv('book.csv')
    df1 = df.loc[df['title']==bname]
    if df1.empty:
        print('Not found')
    else:
        df2 = df.loc[df['category']==cat]
        if df2.empty:
            print('Not found')
        else:
            mname=input("enter member name = ")
            mf = pd.read_csv('member.csv')
            mf1 = mf.loc[mf['memname']==mname]
            if mf1.empty:
                print('Not found')
            else:
                idate=input('date of book issue dd/mm/yyyy = ')
                rdate=input('date of book return issue dd/mm/yyyy = ')
                no=1
                df = pd.read_csv('issue.csv')
                n=df['mname'].count()
                df.loc[n] = [bname,cat,mname,idate,no,rdate]
                df.to_csv('issue.csv', index = False)
                print('book issued successfully')

def viewChart():
    print('Main menu')
    print('1. Books and their values')
    print('2. No of books issued by the members')
    ch = int(input('Enter your choice'))
    match ch:
        case 1:
            df = pd.read_csv('book.csv')
            df = df[['title', 'cost']]
            df.plot('title', 'cost', kind = 'bar')
            py.show()
    
if login():
    while True:
        ch = showMenu()
        match ch:
            case 1:
                b=book()
                match b:
                    case 1:
                        addBook()
                    case 2:
                        searchBook()
                    case 3:
                        pass
                    case 4:
                        dispBookAll()
                    case 5:
                        showMenu()
                    case _:
                        print('invalid choice')

            case 2:
                m=member()
                match m:
                    case 1:
                        addMem()
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        showMenu()
                    case _:
                        print('invalid choice')

            case 3:
                i= issue()
                match i:
                    case 1:
                        bookIs()
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        showMenu()
                    case _:
                        print('invalid choice')
            case 4:
                sys.exit(0)
            case _:
                print('invalid choice')
                break
