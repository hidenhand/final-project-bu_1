from re import U
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkinter.tix import COLUMN
from PIL import Image, ImageTk

# connection database sqlite
def createconnection():
    global conn, cursor

    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()

# function mainwindow
def mainwindow():
    root = Tk()
    x = root.winfo_screenwidth()/2 - w/2 # gran x
    y = root.winfo_screenheight()/2 - h/2 # gran y
    root.resizable(FALSE, FALSE) # not resize window
    root.geometry("%dx%d+%d+%d" % (w, h, x, y)) 
    root.config(bg="#fff")
    root.option_add("*font", "Calibri 12")
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=5)
    root.columnconfigure((0, 1), weight=1)

    return root

# login window
def loginlayout():
    loginframe = Frame(root, bg="#fff")
    loginframe.rowconfigure((0, 1), weight=1)
    loginframe.columnconfigure((0, 1, 2), weight=1)
    # background
    Label(loginframe, image=backgrond_login).grid(
        row=0, column=1, rowspan=2, columnspan=2, sticky="news")
    # input frame
    logininput = Frame(loginframe, bg="#fff")
    logininput.columnconfigure((0, 1), weight=1)
    logininput.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)\
    # return to home button
    Button(logininput, image=exit, relief="flat", bg="#fff").grid(
        row=0, column=0, sticky="wn", padx=20, pady=20)
    # header
    Label(logininput, text="LOGIN FORM", fg="#000", bg="#fff",
          font="bold 14").grid(row=0, column=0, columnspan=2)
    # email
    Label(logininput, text="Email", fg="#000",
          bg="#fff").grid(row=1, column=0, sticky="w", padx=60)
    firstnameinput = Entry(logininput, font="12", width=42)
    firstnameinput.grid(row=2, columnspan=2, sticky="n")
    # password
    Label(logininput, text="Password", fg="#000",
          bg="#fff").grid(row=3, column=0, sticky="w", padx=60)
    firstnameinput = Entry(logininput, font="12", width=42)
    firstnameinput.grid(row=4, columnspan=2, sticky="n")
    # register
    Label(logininput, text="No Account?", fg="#000", bg="#fff").grid(
        row=5, column=0, padx=60, sticky="w")
    register = Label(logininput, text="Register.", fg="#000",
                     bg="#fff")
    register.grid(row=5, column=0)
    # login
    Button(logininput, text="LOGIN", bg="#000", fg="#fff").grid(
        row=6, columnspan=2, ipady=10, ipadx=200)
    # event goto register window
    register.bind("<Button-1>", lambda b: registerlayout())

    logininput.grid(row=0, column=0, columnspan=2, rowspan=2,
                    sticky="news", padx=20, pady=20)

    loginframe.place(width=w, height=h)


def registerlayout():
    registerframe = Frame(root, bg="#fff")
    registerframe.rowconfigure((0, 1), weight=1)
    registerframe.columnconfigure((0, 1), weight=1)
    # background
    Label(registerframe, image=backgrond_login).grid(
        row=0, column=0, rowspan=2, columnspan=2, sticky="news")

    registerinput = Frame(registerframe, bg="#fff")
    registerinput.columnconfigure((0, 1), weight=1)
    registerinput.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
    # goto home button
    Button(registerinput, image=exit, relief="flat", bg="#fff").grid(
        row=0, column=0, sticky="wn", padx=20, pady=20)
    # header
    Label(registerinput, text="REGISTER FORM", fg="#000", bg="#fff",
          font="bold 14").grid(row=0, column=0, columnspan=2)
    # firstname
    Label(registerinput, text="Firstname", fg="#000",
          bg="#fff").grid(row=1, column=0, sticky="w", padx=60)
    firstnameinput = Entry(registerinput, font="12")
    firstnameinput.grid(row=2, column=0, sticky="en", padx=10)
    # lastname
    Label(registerinput, text="Lastname", fg="#000", bg="#fff").grid(
        row=1, column=1, sticky="w")
    lastnameinput = Entry(registerinput, font="12")
    lastnameinput.grid(row=2, column=1, sticky="wn", padx=10)
    # password
    Label(registerinput, text="Password", fg="#000",
          bg="#fff").grid(row=3, column=0, sticky="w", padx=60)
    firstnameinput = Entry(registerinput, font="12", width=42)
    firstnameinput.grid(row=4, columnspan=2, sticky="n")
    # confirm password
    Label(registerinput, text="Confirm Password", fg="#000",
          bg="#fff").grid(row=5, column=0, sticky="w", padx=60)
    firstnameinput = Entry(registerinput, font="12", width=42)
    firstnameinput.grid(row=6, columnspan=2, sticky="n")
    # register button
    Button(registerinput, text="Register", bg="#000", fg="#fff").grid(
        row=7, columnspan=2, ipady=10, ipadx=200)
    # display register window
    registerinput.grid(row=0, column=1, rowspan=2, columnspan=2, sticky="news")

    registerframe.place(width=w, height=h)


def header():
    headerframe = Frame(root, bg="#fff")
    headerframe.columnconfigure((0, 1), weight=1)
    headerframe.rowconfigure((0, 1), weight=1)
    # goto home
    Button(headerframe, text="LOGO BRAND", fg="#fff", relief="flat", bg="#000",
           font="bold 16", command=HeroSection).grid(row=0, column=0, sticky="nw", ipady=20, ipadx=10)
    # goto cart window
    Button(headerframe, text="0", image=cart_img, compound="bottom", relief="flat",
           bg="#fff", fg="#000").grid(row=0, column=1, sticky="ne", padx=130, ipadx=10, pady=5)
    # goto login
    Button(headerframe, text="Login", bg="#000", fg="#fff", relief="flat", font="bold 14", command=loginlayout).grid(
        row=0, column=1, sticky="en", ipady=5, ipadx=30, pady=20, padx=10)
    # search layout
    search = Entry(headerframe, width=40, font="16", fg="#000",
                   highlightthickness=1, bg="#F6EFEF")
    search.grid(row=0, column=0, columnspan=2, sticky="n", pady=30, ipadx=10)
    # search button
    Button(headerframe, image=search_img, relief="flat", bg="#fff").grid(
        row=0, column=1, sticky="n", pady=25, ipadx=10, ipady=5)

    headerframe.grid(row=0, columnspan=2, sticky="new")


def HeroSection():
    global heroframe

    heroframe = Frame(root, bg="#fff")
    heroframe.columnconfigure((0, 1, 2, 3), weight=1)
    heroframe.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

    # header
    Label(heroframe, text="Best Seller Product", fg="#000",
          bg="#fff", font="bold 16").grid(row=0, column=0)
    # fetch daat
    sql = "select * from product"
    cursor.execute(sql)
    result = cursor.fetchall()
    # product list
    u = 0
    for i, record in enumerate(result) :
        if i < 4 :
            Label(heroframe, image=image).grid(row=1,column=i)
        elif i < 8 :
            i = 0
            Label(heroframe, image=image).grid(row=2, column=i+u)
            u += 1
        elif i < 12 :
            t = generatebuttonpage()
            Label(heroframe, image=image).grid(row=1,column=t)
            t += 1

    heroframe.grid(row=1, columnspan=2, sticky="news")

def generatebuttonpage() :
    t = 0

    Button(heroframe,text="2").grid(row=3,column=0)

    return t


def productlayout():
    global productframe

    productframe = Frame(root, bg="#fff")
    productframe.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
    productframe.columnconfigure((0, 1), weight=1)
    sql = "select * from product where id=?"
    cursor.execute(sql,[data])
    result = cursor.fetchall()
    if result :
        # function display image
        imagelayout() 
        # name product
        Label(productframe, text=data[1], bg="#fff",
            fg="#000").grid(row=0, column=1, sticky="nw")
        # score product
        Label(productframe, image=star_img, bg="#fff").grid(
            row=1, column=1, sticky="wn")
        # detail
        Label(productframe, text=data[2], bg="#fff",
            fg="#000").grid(row=2, column=1, sticky="nw")
        # price
        Label(productframe, text="price %s $"%data[3], bg="#fff",
            fg="#000").grid(row=3, column=1, sticky="nw")
        # quantity
        Label(productframe, text="Quantity", bg="#fff",
            fg="#000").grid(row=4, column=1, sticky="nw")
        Spinbox(productframe, from_=0, to=100, font="14",
                justify=CENTER).grid(row=4, column=1, sticky="n")
        # add to cart
        Button(productframe, text="Add to cart",
            bg="#fff", fg="#000", relief="ridge", font="bold").grid(row=5, column=1, ipady=5, ipadx=5, sticky="nw")
        # goto cart window
        Button(productframe, text="Buy Now", bg="#000",
            fg="#fff", relief="flat", font="bold").grid(row=5, column=1, ipady=5, ipadx=5, sticky="n")

    productframe.grid(row=1, columnspan=2, sticky="news")


def imagelayout():
    imageframe = Frame(productframe, bg="#fff")
    imageframe.rowconfigure((0, 1), weight=1)
    imageframe.columnconfigure(0, weight=1)
    # main image
    Label(imageframe, image=images).grid(
        row=0, column=0, sticky="nw", padx=120)
    # second image
    Button(imageframe, image=image, relief="flat").grid(
        row=1, column=0, sticky="nw", padx=120)
    # third image
    Button(imageframe, image=image, relief="flat").grid(
        row=1, column=0, sticky="nw", padx=190)
    # fourth image
    Button(imageframe, image=image, relief="flat").grid(
        row=1, column=0, sticky="nw", padx=260)

    imageframe.grid(row=0, column=0, rowspan=5, sticky="nw")


def payment_layout():
    global cartframe

    cartframe = Frame(root, bg="#fff")
    cartframe.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
    cartframe.columnconfigure((0, 1, 2), weight=1)
    # goto cart
    Button(cartframe, image=exit, relief="flat", bg="#fff").grid(
        row=0, column=0, sticky="wn", padx=20, pady=20)
    # header
    Label(cartframe, text="Pay Name Market", bg="#fff").grid(
        row=1, column=0, sticky="wn", padx=20,)
    # price
    Label(cartframe, text="$ 100", bg="#fff").grid(
        row=3, column=0, sticky="wn", padx=20,)
    # create treeview for display all data after searching
    mytree = ttk.Treeview(cartframe, columns=(
        "col1", "col2", "col3", "col4"))
    mytree.grid(row=2, column=0, sticky="wn", padx=20, columnspan=2)
    # heading mytree
    mytree.heading("col1", text="Username")
    mytree.heading("col2", text="Password")
    mytree.heading("col3", text="Firstname")
    mytree.heading("col4", text="Lastname")
    # columns mytree
    mytree.column("col1", width=120, anchor=CENTER)
    mytree.column("col2", width=120, anchor=CENTER)
    mytree.column("col3", width=200, anchor=CENTER)
    mytree.column("col4", width=200, anchor=CENTER)
    mytree.column("#0", width=0, minwidth=0)
    # subtotal
    Label(cartframe, text="Subtotal", bg="#fff").grid(
        row=3, column=0, sticky="wn", padx=20)
    # price total product
    Label(cartframe, text="$ 100", bg="#fff").grid(row=3, column=1)
    # shiping price
    Label(cartframe, text="Shipping", bg="#fff").grid(
        row=4, column=0, sticky="w", padx=20,)
    # detail shiping
    Label(cartframe, text="detail", bg="#fff", fg="#898181").grid(
        row=5, column=0, sticky="w", padx=20, pady=20)
    # shiping price
    Label(cartframe, text="$ 10", bg="#fff").grid(row=4, column=1)
    # shiping + total product price
    Label(cartframe, text="Total", bg="#fff").grid(
        row=6, column=0, sticky="w", padx=20)
    # total price
    Label(cartframe, text="$ 1009", bg="#fff").grid(
        row=6, column=1)
    # payment layout
    billinput_layout()

    cartframe.place(width=w, height=h)


def billinput_layout():
    global paymentframe
    # main frame payment layout
    paymentframe = Frame(cartframe, bg="#E5E5E5")
    paymentframe.rowconfigure(
        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16), weight=1)
    paymentframe.columnconfigure((0, 1), weight=1)
    # header
    Label(paymentframe, text="Pay with card", bg="#E5E5E5").grid(
        row=0, column=0, sticky="w", padx=30)
    # email
    Label(paymentframe, text="Email", bg="#E5E5E5").grid(
        row=1, column=0, sticky="w", padx=30)
    # email input
    emailinput = Entry(paymentframe)
    emailinput.grid(row=2, column=0, columnspan=2, sticky="we", padx=30)
    # shiping
    Label(paymentframe, text="Shiping method",
          bg="#E5E5E5").grid(row=3, column=0, sticky="w", padx=30)
    # choice shiping
    Radiobutton(paymentframe, text="Febby\t$ 10", value=0,
                bg="#E5E5E5").grid(row=4, column=0, sticky="w", padx=30)
    Radiobutton(paymentframe, text="Febby\t$ 10", value=1,
                bg="#E5E5E5").grid(row=5, column=0, sticky="w", padx=30)
    # card number
    Label(paymentframe, text="Card number", bg="#E5E5E5").grid(
        row=6, column=0, sticky="w", padx=30)
    cardnumberinput = Entry(paymentframe)
    cardnumberinput.grid(row=7, column=0, columnspan=2, sticky="we", padx=30)
    # card date
    Label(paymentframe, text="Card date", bg="#E5E5E5").grid(
        row=8, column=0, sticky="w", padx=30)
    carddate = Entry(paymentframe)
    carddate.grid(row=9, column=0, sticky="we", padx=30)
    # card cvc
    Label(paymentframe, text="Card cvc", bg="#E5E5E5").grid(
        row=8, column=1, sticky="w")
    cardcvc = Entry(paymentframe)
    cardcvc.grid(row=9, column=1, sticky="w", ipadx=12)
    # name on card
    Label(paymentframe, text="Name on card",
          bg="#E5E5E5").grid(row=10, column=0, sticky="w", padx=30)
    cardnameinput = Entry(paymentframe)
    cardnameinput.grid(row=11, column=0, columnspan=2, sticky="we", padx=30)
    # billing address
    Label(paymentframe, text="Billing address",
          bg="#E5E5E5").grid(row=12, column=0, sticky="w", padx=30)
    address = Entry(paymentframe)
    address.grid(row=13, column=0, columnspan=2, sticky="we", padx=30)
    # city
    Label(paymentframe, text="City", bg="#E5E5E5").grid(
        row=14, column=0, sticky="w", padx=30)
    pininput = Entry(paymentframe)
    pininput.grid(row=15, column=0, sticky="we", padx=30)
    # postal code
    Label(paymentframe, text="Postal code",
          bg="#E5E5E5").grid(row=14, column=1, sticky="w")
    cityinput = Entry(paymentframe)
    cityinput.grid(row=15, column=1, sticky="w", ipadx=12)
    # button
    Button(paymentframe, text="Pay", fg="#fff", bg="#000", relief="flat",
           font="12").grid(row=16, column=0, columnspan=2, ipady=10, pady=10, sticky="we", padx=30)
    # display
    paymentframe.grid(row=0, column=2, rowspan=7, sticky="news")

# width and height
w = 1200
h = 600
# connection database
createconnection()
# tkinter 
root = mainwindow()
# images
image = PhotoImage(file="img/shopping-cart.png")
cart_img = PhotoImage(file="img/shopping-cart.png").subsample(2, 2)
search_img = PhotoImage(file="img/search.png").subsample(3, 3)
star_img = PhotoImage(file="img/star.png").subsample(2, 2)
banner = PhotoImage(file="img/banner.png").subsample(4, 4)
images = PhotoImage(file="img/image.png").subsample(2, 2)
exit = PhotoImage(file="img/sign-out.png").subsample(2, 2)
backgrond_login = PhotoImage(file="img/background_login.png")
# windows()
# loginlayout()
# registerlayout()
header()
HeroSection()
# productlayout()
# payment_layout()

root.mainloop()
