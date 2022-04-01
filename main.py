from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
# from authenticate import *

# Add database name and password
mypass = "admin"
mydatabase="db"

# connect to database
con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# create GUI window (main window)
root = Tk()

suffix = u"\u00A9" + " Divyang Soni"
root.title("Library Management System " + suffix)
root.minsize(width=400,height=400)
root.geometry("800x600")

# Set Application Icon
root.call('wm', 'iconphoto', root._w, PhotoImage(file='C:/Users/DIVYANG/Desktop/LMS Python/icon.png'))

# Take n greater than 0.25 and less than 5
same=True
n=0.5

# Adding a background image
background_image = Image.open("lib3.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)


img = ImageTk.PhotoImage(background_image)

# Create canvas to display image
Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

# Create frame to display Heading
headingFrame1 = Frame(root,bg="#00ffbf",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

# Create Heading Label
headingLabel = Label(headingFrame1, text="Welcome to \n Library Management System", bg='black', fg='white', font=('Sans Serif',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

# Add Book button
btn1 = Button(root,text="Add Book",bg='black', fg='white', command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45, relheight=0.1)

# Delete Book button
btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45, relheight=0.1)

# View Books button
btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45, relheight=0.1)
    
# Issue Book to Student Button
btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command=issueBook)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45, relheight=0.1)

# Return Book Button
btn5 = Button(root,text="Return Book",bg='black', fg='white', command=returnBook)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45, relheight=0.1)

root.mainloop()
