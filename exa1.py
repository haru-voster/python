from tkinter  import*
def getvals():
    if pdentry==['#','$','@']:
        print("ACCESS GRANTED")
    elif pdentry==['a-z ||A-Z']:
        print("ACCESS GRANTED")
    else:
       print("ACCESS DENIED")
tp=Tk(screenName=None, baseName=None, className='Tix')
tp.geometry('600x500')
#heading 
Label(tp,text="\nLOG IN HERE\n",font="algebraic 20 bold").grid(row=0,column=2)
#Field labelling
Fname=Label(tp, text="First name:",font="david 16 italic")
Sname=Label(tp,text="Second name:",font="david 16 italic")
uname=Label(tp,text="Username:",font="david 16 italic")
pd=Label(tp,text="password:",font="david 16 italic")
Fname.grid(row=1,column=2)
Sname.grid(row=2,column=2)
uname.grid(row=3,column=2)
pd.grid(row=4,column=2)

#assigning variable datatype
Fnamevalue=StringVar
Snamevalue=StringVar
unamevalue=StringVar
pdvalue=IntVar
checkvalue=IntVar
 #field entry
Fnameentry=Entry(tp, textvariable=Fnamevalue)
Snameentry=Entry(tp,textvariable=Snamevalue)
unameentry=Entry(tp, textvariable=unamevalue)
pdentry=Entry(tp,textvariable=pdvalue)
Fnameentry.grid(row=1,column=3)
Snameentry.grid(row=2,column=3)
unameentry.grid(row=3,column=3)
pdentry.grid(row=4,column=3)
#check box
checkbtn=Checkbutton(text="Remember me", variable="checkvalue").grid(row=5,column=3)
#button
Button(tp, text="submit",font="time 13 bold", command=getvals).grid(row=6,column=3)
tp.mainloop()
