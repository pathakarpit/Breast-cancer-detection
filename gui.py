from project import *
from tkinter import *

root = Tk()
root.title('breast cancer detection')
root.geometry("295x350")

def cancer():
    x0 = variable0.get()
    x1 = variable1.get()
    x2 = variable2.get()
    x3 = variable3.get()
    x4 = variable4.get()
    x5 = variable5.get()
    x6 = variable6.get()
    x7 = variable7.get()
    x8 = variable8.get()
    
    ans = classifier.predict([[x0,x1,x2,x3,x4,x5,x6,x7,x8]])
    if ans[0] ==2:
        tumor_type = 'benign(not cancerous)'
    else:
        tumor_type = 'malignant(cancerous)'
        
    label = Label(root, text =tumor_type)
    label.grid(row=12, column=0)



label0 = Label(root, text ="Clump Thickness")
label0.grid(row=2, column=0)
variable0 = IntVar()
variable0.set('choose')
drop0 = OptionMenu(root, variable0, "1", "2", "3", "4", "5", '6', '7','8','9','10')
drop0.grid(row=2,column=1)

label1 = Label(root, text ="Uniformity of Cell Size")
label1.grid(row=3, column=0)
variable1 = IntVar()
variable1.set('choose')
drop1 = OptionMenu(root, variable1, "1", "2", "3", "4", "5", '6', '7','8','9','10')
drop1.grid(row=3,column=1)

label2 = Label(root, text ="Uniformity of Cell Shape")
label2.grid(row=4, column=0)
variable2 = IntVar()
variable2.set('choose')
drop2 = OptionMenu(root, variable2, "1", "2", "3", "4", "5", '6', '7','8','9','10')
drop2.grid(row=4,column=1)

label3 = Label(root, text ="Marginal Adhesion")
label3.grid(row=5, column=0)
variable3 = IntVar()
variable3.set('choose')
drop3 = OptionMenu(root, variable3, "1", "2", "3", "4", "5", '6', '7','8','9','10')
drop3.grid(row=5,column=1)

label4 = Label(root, text ="Single Epithelial Cell Size")
label4.grid(row=6, column=0)
variable4 = IntVar()
variable4.set('choose')
drop4 = OptionMenu(root, variable4, "1", "2", "3", "4", "5", '6', '7','8','9','10')
drop4.grid(row=6,column=1)

label5 = Label(root, text ="Bare Nuclei")
label5.grid(row=7, column=0)
variable5 = IntVar()
variable5.set('choose')
drop5 = OptionMenu(root, variable5, "1", "2", "3", "4", "5", '6', '7','8','9','10')
drop5.grid(row=7,column=1)

label6 = Label(root, text ="Bland Chormation")
label6.grid(row=8, column=0)
variable6 = IntVar()
variable6.set('choose')
drop6 = OptionMenu(root, variable6, "1", "2", "3", "4", "5", '6', '7','8','9','10')
drop6.grid(row=8,column=1)

label7 = Label(root, text ="Normal Nucleoli")
label7.grid(row=9, column=0)
variable7 = IntVar()
variable7.set('choose')
drop7 = OptionMenu(root, variable7, "1", "2", "3", "4", "5", '6', '7','8','9','10')
drop7.grid(row=9,column=1)

label8 = Label(root, text ="Mitoses")
label8.grid(row=10, column=0)
variable8 = IntVar()
variable8.set('choose')
drop8 = OptionMenu(root, variable8, "1", "2", "3", "4", "5", '6', '7','8','9','10')
drop8.grid(row=10,column=1)

button = Button(root, text = 'check', command = cancer)
button.grid(row=11, column=0)

root.mainloop()



