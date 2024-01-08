# importing modules
import shutil
from pywebio.input import *
from pywebio.output import *
from pywebio.session import run_js
 
def writefile(info):
    f = open("book.dat", "a")
    s1 = info['book']+"-"+info['price']+'-'+info['dates']+'-'+info['name']+'-'+info['rdate']+'-'+info['admin']+'\n';
    f.write(s1)
    f.close()
    
def searchfile(info):
        f1 = open('book.dat', 'r')
        Lines = f1.readlines()
 
        count = 0
        # Strips the newline character
        for line in Lines:
            x = line.split("-")
            if x[0] == info['book']:
                put_table([
                ['Book', 'Price','Date of Issue','Borrower Name','Return Date','Admin name',],
                [x[0], x[1],x[2],x[3],x[4],x[5]]
                ])
                count+=1
                put_text("Book available")
        if count == 0:
            put_text(f"book not found")
def searchperson(info):
        f1 = open('book.dat', 'r')
        Lines = f1.readlines()
 
        count = 0
        # Strips the newline character
        for line in Lines:
            x = line.split("-")
            if x[3] == info['name']:
                put_table([
                ['Book', 'Price','Date of Issue','Borrower Name','Return Date','Admin name',],
                [x[0], x[1],x[2],x[3],x[4],x[5]]
                ])
                count+=1
                put_text("The person has issued a book")
        if count == 0:
            put_text(f"person not found")

def delb(info):
 f1 = open('book.dat', 'r')
 Lines = f1.readlines()
 count = 0
 f2=open('delbook.dat','w')
 for line in Lines:
             x = line.split("-")
             if x[0] != info['book']:
                 f2.write(line)
                 count=1
                 put_text("book deleted")
                 
                 
 if count == 0:
                 put_text(f"book not found")
                    
      
while True:
  with use_scope('scope3'):
    clear('scope3');
    put_row(put_code("Library Management system"))

    put_text("1 -> VIEW BOOKS")
    put_text("2 -> ADD BOOKS")
    put_text("3 -> DELETE BOOKS")
    put_text("4 -> ENTER PERSON TO BE SEARCHED ")
    put_text("5 -> SEARCH IF BOOK IS AVAILABLE")
    put_text("6 -> Exit")
    p = int(input("What is your choice"))

    if p == 2:
        info = input_group("Books borrowed",[
        input('Enter name of the the book', name='book'),
        input('Enter the price of the book', name='price'),
        input('Enter date (dd/mm/yy)', name='dates'),
        input("Enter the borrower's name", name='name'),
        input('Enter return date (dd/mm/yy)', name='rdate'),
        input('Enter the of admin ', name='admin'),
        

    ], validate=writefile)



    if p == 1:
        f1 = open("book.dat", "r")
        f=f1.readlines()
        count=0
        for line in f:
            x = line.split("-")
            put_table([
            ['Name of Book', 'Price','Date ','Borrower Name ','Return Date','admin name'],
            [x[0],x[1],x[2],x[3],x[4],x[5]]
             ])
            count+=1
        if count == 0:
            img = open('fileempty.png', 'rb').read()  
            put_image(img, width='50px')

    if p == 3:
           info = input_group(" ENTER BOOK TO BE DELETED",[
        input('Please enter  name', name='book'),
    ], validate=delb)
           with open('delbook.dat', 'r') as source_file:
               content = source_file.read()

           with open('book.dat', 'w') as destination_file:
               destination_file.write(content)

    if p == 5:
        info = input_group(" ENTER BOOK TO CHECK IF IT IS AVAILABLE",[
        input('Please enter  name', name='book'),
    ], validate=searchfile)


    if p == 4:
        info = input_group(" ENTER NAME IF THE PERSON HAS ISSUED THE BOOK",[
        input('Please enter  name', name='name'),
    ], validate=searchperson)

    if actions("Continue?",["continue", "exit"])=="exit":
        break


