from tkinter import *
import matplotlib.pyplot as plt
import csv
root1 = Tk()

root1.geometry('1920x1080')
root1.title("Welcome to Industrial Expense Manager")
root1.configure(background="#33E3FF")

def root2():
    root2a = Toplevel()
    root2a.geometry('1920x1080')
    root2a.title("Daily Industrial Expense Manager ")
    root2a.configure(background='white')
    head = Label(root2a, text="Welcome to Daily Industrial Expense Manager! ", bg="white", fg='red', font=(None, 28))
    head.place(x=250, y=10)

    menur = Menu(root2a)
    root2a.config(menu=menur)

    submr = Menu(menur)
    menur.add_cascade(label="OPEN ", menu=submr)
    submr.add_command(label="OPEN YEARLY EXPENSE CALCULATOR", command=window)
    submr.add_command(label="OPEN EXPENSE VS SALES TRACKER", command=windowdown)
    submr.add_command(label="Print")
    submr.add_command(label="Quit Daily Industrial Expense Manager ", command=root2a.destroy)

    subm2r = Menu(menur)
    menur.add_cascade(label="Creators", menu=subm2r)
    subm2.add_command(label="Made by Arnav Suman and Shaurya Rakesh! ")

    space8 = Label(root2a, text="", bg='white', font=(None, 35))
    space8.grid(row=2)

    date = Label(root2a, text="Enter date in DD/MM/YYYY format:", bg='white', font=(None, 25))
    date.grid(row=3, column=0)

    ldate = Entry(root2a, width=50, bg='grey', font=(None, 20))
    ldate.grid(row=3, column=1, ipady=10)

    space2 = Label(root2a, text="", bg='white', font=(None, 25))
    space2.grid(row=4, column=1)

    title = Label(root2a, text="Enter title of expense: ", bg='white', font=(None, 25))
    title.grid(row=5, column=0)

    ltitle = Entry(root2a, width=50, bg='grey', font=(None, 20))
    ltitle.grid(row=5, column=1, ipady=10)

    space3 = Label(root2a, text="", fg="white", font=(None, 25))
    space3.grid(row=6, column=1)

    exp = Label(root2a, text="Enter amount of expense( in Lakhs) : ", bg='white', font=(None, 25))
    exp.grid(row=7, column=0)

    lexp = Entry(root2a, width=50, bg='grey', font=(None, 20))
    lexp.grid(row=7, column=1, ipady=10)

    space4 = Label(root2a, text="", bg='white', font=(None, 25))
    space4.grid(row=8, column=1)
    list1 = []
    list2 = []

    fcsv = open('DailyIndustrialExpenseManager.csv', 'a', newline='')
    writer = csv.writer(fcsv)
    writer.writerow(("Title", "Date", "Expense"))
    fcsv.close()

    def sumexp():
        a = float(lexp.get())
        b = ltitle.get()
        c = str(ldate.get())
        list1.append(a)
        list2.append(b)
        sumlist = "The Total Expenses are: "+" "+str(round(sum(list1), 2))+" "+"Lakhs uptill "+c
        ent = Label(root2a, text=sumlist, font=(None, 20), bg='white')
        ent.grid(row=9, column=1)
        fcsv = open('DailyIndustrialExpenseManager.csv', 'a', newline='')
        tup1 = (b, c, a)
        writer = csv.writer(fcsv)
        writer.writerow(tup1)
        fcsv.close()
        ldate.delete(0, END)
        lexp.delete(0, END)
        ltitle.delete(0, END)
    button = Button(root2a, text="Click to add to List and Show Total", padx=10, pady=10, font=(None, 20),
                    command=sumexp)
    button.grid(row=9, column=0)

    space5 = Label(root2a, text="", font=(None, 25))
    space5.grid(row=10, column=1)

    def newwin():
        fig = plt.figure("PIE CHART DISTRIBUTION OF EXPENSES")
        plt.pie(list1, labels=list2, radius=1.5, autopct="%0.2f%%", startangle=45, shadow=True,)
        plt.axis('equal')
        plt.title("Expense Graph")
        plt.show(block=True)
    button2 = Button(root2a, text="Show Pie Chart Distribution of Expenses ", padx=10, pady=10, font=(None, 20),
                     command=newwin)
    button2.grid(row=11, column=0)

    space6 = Label(root2a, text="", font=(None, 25))
    space6.grid(row=12, column=1)

    quitroot2 = Button(root2a, text='Close window', padx=10, pady=10, font=(None, 23), command=root2a.destroy)
    quitroot2.grid(row=13)

    root2a.mainloop()

def window():
    top = Toplevel()
    top.geometry('1920x1080')
    top.configure(background="white")
    top.title("Welcome to Yearly Industrial Expense Manager")

    menu2 = Menu(top)
    top.config(menu=menu2)

    subm2top = Menu(menu2)
    menu2.add_cascade(label="OPEN ", menu=subm2top)
    subm2top.add_command(label="OPEN EXPENSE VS SALES TRACKER", command=windowdown)
    subm2top.add_command(label="OPEN DAILY EXPENSE TRACKER", command=root2)
    subm2top.add_command(label="Print")
    subm2top.add_command(label="Quit Yearly Industrial Expense Manager ", command=top.destroy)

    subm3top = Menu(menu2)
    menu2.add_cascade(label="Creators", menu=subm3top)
    subm3top.add_command(label="Made by Arnav Suman and Shaurya Rakesh! ")

    headss = Label(top, text="Welcome to Yearly Industrial Expense Manager! ", bg='white', fg='red', font=(None, 28))
    headss.place(x=300)

    spacess8 = Label(top, text="", bg="white", font=(None, 35))
    spacess8.grid(row=2)

    year = Label(top, text="Enter Year (integer): ", bg='white', font=(None, 25))
    year.grid(row=3)
    lyear = Entry(top, width=50, bg='grey', font=(None, 20))
    lyear.grid(row=3, column=1, ipady=10)

    spaces1 = Label(top, bg="white", font=(None, 25))
    spaces1.grid(row=4)

    cost = Label(top, text="Enter Expense(in Lakhs) : ", bg='white', font=(None, 25))
    cost.grid(row=5)
    lcost = Entry(top, width=50, bg='grey', font=(None, 20))
    lcost.grid(row=5, column=1, ipady=10)

    spaces2 = Label(top, bg="white", font=(None, 25))
    spaces2.grid(row=6)

    fcsv2 = open('Yearly Industrial Expense Manager.csv', 'a', newline='')
    writer2 = csv.writer(fcsv2)
    writer2.writerow(("Year", "Expense (Lakhs)"))
    fcsv2.close()

    lists1 = []
    lists2 = []

    def sumyear():
        aa = int(lyear.get())
        bb = float(lcost.get())
        lists1.append(bb)
        lists2.append(aa)
        sumcost = "The Total Expenses are: "+" "+str(round(sum(lists1), 2))+" Lakhs uptill "+str(aa)
        zz = Label(top, bg='white', text=sumcost, font=(None, 20))
        zz.grid(row=7, column=1)
        fcsv2 = open('Yearly Industrial Expense Manager.csv', 'a', newline='')
        tup123 = (aa, bb)
        writer3 = csv.writer(fcsv2)
        writer3.writerow(tup123)
        fcsv2.close()
        lcost.delete(0, END)
        lyear.delete(0, END)

    buttons1 = Button(top, text="Click to add to List and Show Total", padx=10, pady=10, font=(None, 20),
                      command=sumyear)
    buttons1.grid(row=7)

    spaces3 = Label(top, bg="white", font=(None, 25))
    spaces3.grid(row=8)

    def bargraphs():
        plt.plot(lists2, lists1)
        plt.title('Yearly Expense Graph')
        plt.ylabel('Expenses in Lakhs')
        plt.xlabel('Year')
        plt.show()

    buttons2 = Button(top, text="Click to show Bar Graph ", padx=10, pady=10, font=(None, 20), command=bargraphs)
    buttons2.grid(row=9)

    spaces4 = Label(top, bg="white", font=(None, 25))
    spaces4.grid(row=10)

    buttons3 = Button(top, text="Close Window ", padx=10, pady=10, font=(None, 20), command=top.destroy)
    buttons3.grid(row=11)

    top.mainloop()

def windowdown():
    down = Toplevel()
    down.geometry('1920x1080')
    down.title("Welcome to Income Vs Expense Tracker")
    down.configure(background="white")

    menu3 = Menu(down)
    down.config(menu=menu3)

    subm3 = Menu(menu3)
    menu3.add_cascade(label="OPEN ", menu=subm3)
    subm3.add_command(label="OPEN YEARLY EXPENSE CALCULATOR", command=window)
    subm3.add_command(label="OPEN DAILY EXPENSE CALCULATOR", command=root2)
    subm3.add_command(label="Print")
    subm3.add_command(label="Close Income Vs Expense Tracker ", command=down.destroy)

    subm32 = Menu(menu)
    menu3.add_cascade(label="Creators", menu=subm32)
    subm32.add_command(label="Made by Arnav Suman and Shaurya Rakesh! ")

    headdown = Label(down, text='Welcome to Income Vs Expense Tracker', bg='white', fg='red', font=(None, 30))
    headdown.place(x=350)

    space_down = Label(down, text="", bg="white", font=(None, 25))
    space_down.grid(row=1)

    label1_down = Label(down, text='Enter Year: ', bg='white', font=(None, 25))
    label1_down.grid(row=2, column=0)
    elabel1_down = Entry(down, width=50, bg='grey', font=(None, 20))
    elabel1_down.grid(row=2, column=1)

    space_down1 = Label(down, text="", bg="white", font=(None, 25))
    space_down1.grid(row=3)

    label2_down = Label(down, text='Enter Expenses(in Lakhs): ', bg='white', font=(None, 25))
    label2_down.grid(row=4, column=0)
    elabel2_down = Entry(down, width=50, bg='grey', font=(None, 20))
    elabel2_down.grid(row=4, column=1)

    space_down2 = Label(down, text="", bg="white", font=(None, 25))
    space_down2.grid(row=5)

    label3_down = Label(down, text='Enter Sales(in Lakhs): ', bg='white', font=(None, 25))
    label3_down.grid(row=6, column=0)
    elabel3_down = Entry(down, width=50, bg='grey', font=(None, 20))
    elabel3_down.grid(row=6, column=1)

    space_down2 = Label(down, text="", bg="white", font=(None, 25))
    space_down2.grid(row=7)

    list1_down = []
    list2_down = []
    list3_down = []

    fcsv4 = open('Income Vs Expense Tracker.csv', 'a', newline='')
    writer4 = csv.writer(fcsv4)
    writer4.writerow(("Year", "Expense", "Sales", "Profit/Loss(Lakhs)"))
    fcsv4.close()

    def add_down():
        a_down = elabel1_down.get()
        b_down = float(elabel2_down.get())
        c_down = float(elabel3_down.get())
        list1_down.append(a_down)
        list2_down.append(b_down)
        list3_down.append(c_down)
        sum_down = 'The Total Expenses till: ' + str(a_down) + ' are: ' + str(round(sum(list2_down), 2)) + 'Lakhs'
        sum_down2 = 'The Total Sales till : ' + str(a_down) + ' are: ' + str(round(sum(list3_down), 2)) + 'Lakhs'
        ent_down = Label(down, text=sum_down, bg='white', font=(None, 25))
        ent_down.grid(row=8, column=1)
        ent1_down = Label(down, text=sum_down2, bg='white', font=(None, 25))
        ent1_down.grid(row=9, column=1)
        pro = c_down - b_down
        pro = round(pro, 2)
        if pro < 0:
            numpro = 'Loss'
            col = 'red'
        else:
            numpro = 'Profit'
            col = 'green'

        sum_down3 = 'Net ' + str(numpro) + ' in year ' + str(a_down) + ' is ' + str(pro) + ' Lakhs'
        ent3_down = Label(down, text=sum_down3, bg='white', fg=col, font=(None, 25))
        ent3_down.grid(row=10, column=1)
        fcsv4 = open('Income Vs Expense Tracker.csv', 'a', newline='')
        tup12 = (a_down, b_down, c_down, pro)
        writer4 = csv.writer(fcsv4)
        writer4.writerow(tup12)
        fcsv4.close()
        elabel1_down.delete(0, END)
        elabel2_down.delete(0, END)
        elabel3_down.delete(0, END)

    def graphloss():
        plt.plot(list1_down, list2_down, label='Total Expenses')
        plt.plot(list1_down, list3_down, label='Total Sales')
        plt.xlabel('Year')
        plt.ylabel('Profit/Loss in Lakhs')
        plt.title('Expense Vs Sales Graph ')
        plt.legend()
        plt.show()

    button_down = Button(down, text='Click to Add and show Total ', font=(None, 20), padx=0, pady=8, command=add_down)
    button_down.grid(row=8, column=0)

    space_down3 = Label(down, text='', bg='white', font=(None, 25))
    space_down3.grid(row=9)

    button_down1 = Button(down, text='Click to Show Expense vs Sales Graph', padx=0, pady=8, font=(None, 20),
                          command=graphloss)
    button_down1.grid(row=10)

    space_down4 = Label(down, text='', bg='white', font=(None, 25))
    space_down4.grid(row=11)

    button_down2 = Button(down, text='Close Window', padx=4, pady=8, font=(None, 20), command=down.destroy)
    button_down2.grid(row=12)

    down.mainloop()

lbl = Label(text=' Welcome to Industrial Expense Calculator! ', bg='#33E3FF', font=(None, 45))
lbl.place(x=190, y=100)

butbase = Button(text='Open Daily Expense Manager ', padx=10, pady=10, font=(None, 28), bg='white', fg='black',
                 command=root2)
butbase.place(x=390, y=250)

butbase2 = Button(text='Open Yearly  Expense Manager ', padx=10, pady=10, font=(None, 28), bg='white', fg='black',
                  command=window)
butbase2.place(x=390, y=400)

butbase3 = Button(text='Open Sales-vs-Expense Graph ', padx=10, pady=10, font=(None, 28), bg='white', fg='black',
                  command=windowdown)
butbase3.place(x=390, y=550)

butbase4 = Button(text='Exit Aplication ', padx=10, pady=10, font=(None, 28), bg='white', fg='black',
                  command=root1.destroy)
butbase4.place(x=1100, y=700)

lbl2base = Label(text='Made by Arnav Suman & Shaurya Rakesh', bg='#33E3FF', font=(None, 25))
lbl2base.place(x=15, y=700)

menu = Menu(root1)
root1.config(menu=menu)

subm = Menu(menu)
menu.add_cascade(label="OPEN ", menu=subm)
subm.add_command(label="OPEN YEARLY EXPENSE CALCULATOR", command=window)
subm.add_command(label="OPEN EXPENSE VS SALES TRACKER", command=windowdown)
subm.add_command(label='OPEN DAILY EXPENSE CALCULATOR', command=root2)
subm.add_command(label="Print")
subm.add_command(label="Quit Application ", command=root1.destroy)

subm2 = Menu(menu)
menu.add_cascade(label="Creators", menu=subm2)
subm2.add_command(label="Made by Arnav Suman and Shaurya Rakesh! ")


root1.mainloop()