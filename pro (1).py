import sys
from tkinter import *

mgui = Tk()

mgui.geometry('470x450+500+300')
mgui.title('Electricity Bill Caculator')

     
class Find_cash():
    ''' '''
    def __init__(self):
        ''' '''
        self.cash = 0
        self.cash_lis = [0, 0, 0, 0, 0, 0, 0]
        self.unit_lis = []
        self.cal_lis = [1.8632, 2.5026, 2.7549, 3.1381, 3.2315, 3.7362, 3.9361]
        
    def homeanddorm(self, unt):
        ''' '''
        #HOME
        if gui.option.get() == 1:
            gui.u1.configure(state='disabled')
            unt = float(u.utt)
            if unt > 50:
                if unt > 400:
                    self.unit_lis.append(unt-400)
                    unt -= unt-400
                if unt > 150:
                    self.unit_lis.append(unt-150)
                    unt -= unt-150
                if unt > 100:
                    self.unit_lis.append(unt-100)
                    unt -= unt-100
                if unt > 35:
                    self.unit_lis.append(unt-35)
                    unt -= unt-35
                if unt > 25:
                    self.unit_lis.append(unt-25)
                    unt -= unt-25
                if unt > 15:
                    self.unit_lis.append(unt-15)
                    unt -= unt-15
                if unt > 0:
                    self.unit_lis.append(unt)
                self.unit_lis.reverse()
                for i in range(len(self.unit_lis)):
                    self.cash_lis[i] = (self.cal_lis[i]*self.unit_lis[i])
                self.cash = sum(self.cash_lis)
                self.vat = (self.cash) * 7 / 100.0

                #OUTPUT
                gui.o1.delete(0, END)
                gui.o2.delete(0, END)
                gui.o3.delete(0, END)
                #Cash
                gui.o1.insert(1, '%.2f'%self.cash)
                #Vat
                gui.o2.insert(1, '%.2f'%self.vat)
                #Total
                gui.o3.insert(1, '%.2f'%(self.cash+self.vat))
            # if total unit less than 50
            else:
                #OUTPUT
                gui.o1.delete(0, END)
                gui.o2.delete(0, END)
                gui.o3.delete(0, END)
                #Cash
                gui.o1.insert(1, 0)
                #Vat
                gui.o2.insert(1, 0)
                #Total
                gui.o3.insert(1, 0)

        #DORM    
        elif gui.option.get() == 0:
            #Error
            if unt == '':
                messagebox.showinfo('Error', 'Please Enter Unit/Bath')
            #OUTPUT
            gui.o1.delete(0, END)
            gui.o2.delete(0, END)
            gui.o3.delete(0, END)
            #Cash
            gui.o1.insert(1, '%.2f' % (float(unt)* float(u.utt)))
            #Vat
            gui.o2.insert(1, '-')
            #Total
            gui.o3.insert(1, '%.2f' % (float(unt)* float(u.utt)))
            
class find_unit():
    ''' '''
    def __init__(self):
        ''' '''
        self.lis = []
        self.unitlis = []
    def valueGET(self, name, amount, power, tmpdy, day):
        try:
            name[0]
            float(amount)
            float(power)
            float(tmpdy)
            float(day)
            self.lis = [name, float(amount), float(power), float(tmpdy), float(day)]
            print (self.lis)
            self.unit = (self.lis[1])*(self.lis[2])/1000.0*(self.lis[3])*(int(self.lis[4]))
            self.unitlis.append(self.unit)
            print (self.unitlis)
            print (self.unit)
            self.utt = (sum(map(float, self.unitlis)))
            print (self.utt)
            gui.Lb1.insert(1, name+' '+'%.2f' % (self.unit)+' unit')
            gui.e6.delete(0, END)
            gui.e6.insert(0, '%.2f' % sum(self.unitlis))
        except:
            messagebox.showerror(
                "Error",
                "Please enter the correct information's type."
                )
            
class Mguiface():
    ''' '''
    def __init__(self):
        ''' '''
        #Selected Your Habitat
        mlabel = Label(text='Selected Your Habitat ').place(x=10, y=5)
        self.option = IntVar()
        self.s1 = Radiobutton(mgui, text = "Home", variable = self.option, \
                         value=1, height=0, \
                         width = 8, command = self.dis_ena)
        self.s2 = Radiobutton(mgui, text = "Dorm", variable = self.option, \
                         value=0, height=0, \
                         width = 8, command = self.dis_ena)
        self.s1.place(x=5, y=30) 
        self.s2.place(x=85, y=30)
        
        #Input Detail Electric Appliances....................#
        mlabel = Label(text='Enter Your Electric Appliances').place(x=10, y=60)
        Label(mgui, text='Enter Electric appliances : ').place(x=5, y=95)
        self.e1 = Entry(mgui)
        self.e1.place(x=150, y=95)

        Label(mgui, text='Enter Amount : ').place(x=57, y=125)
        self.e2 = Entry(mgui)
        self.e2.place(x=150, y=125)

        Label(mgui, text='Enter Power (W) : ').place(x=45, y=155)
        self.e3 = Entry(mgui)
        self.e3.place(x=150, y=155)

        Label(mgui, text='Enter Time use/day (Hr) : ').place(x=4, y=185)
        self.e4 = Entry(mgui)
        self.e4.place(x=150, y=185)

        Label(mgui, text='Enter Day use/Month : ').place(x=17, y=215)
        self.e5 = Entry(mgui)
        self.e5.place(x=150, y=215)
        #.....................................................#

        #Unit/Bath
        Label(mgui, text='Unit/Bath :  ').place(x=305, y=95)
        self.u1 = Entry(mgui, width = 7)
        self.u1.place(x=375, y=95)

        #Get Value 
        ok = Button(mgui, text='  OK  ', height=0, width = 6, command=lambda: u.valueGET(self.e1.get(),self.e2.get(),\
                                                                               self.e3.get(),self.e4.get(),self.e5.get())).place(x=180, y=243)
        #listbox for user Electric Appliances
        Label(mgui, text='Your Electric Appliances').place(x=295, y=130)
        self.Lb1 = Listbox(mgui, height=8, width=25)
        self.Lb1.place(x=300, y=155)

        #Total unit
        Label(mgui, text='Total Unit : ').place(x=300, y=295)
        self.e6 = Entry(mgui, width=10)
        self.e6.place(x=370, y=295)

        
        #OUTPUT ??
        Label(mgui, text='CASH  :').place(x=50, y=290)
        self.o1 = Entry(mgui, width = 15)
        self.o1.place(x=100, y=285)
        Label(mgui, text='VAT  :').place(x=55, y=320)
        self.o2 = Entry(mgui, width = 10)
        self.o2.place(x=100, y=315)
        Label(mgui, text='Total  :').place(x=55, y=350)
        self.o3 = Entry(mgui, width = 10)
        self.o3.place(x=100, y=345)
        #Cal
        Cal = Button(mgui, text=' Calculate ', height=0, width=7,\
                     command=lambda: c.homeanddorm(self.u1.get())).place(x=347, y=325)
        #CLEAR Button
        clear = Button(mgui, text=' Reset ', command=self.clear_text, height=0,\
                    width=6).place(x=155, y=415)

        #EXIT Button
        end = Button(mgui, text='  Exit  ', command=mgui.destroy, height=0, \
                 width = 6).place(x=230, y=415)

    def clear_text(self):
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)
            self.e6.delete(0, END)
            self.o1.delete(0, END)
            self.o2.delete(0, END)
            self.o3.delete(0, END)
            self.Lb1.delete(0, END)
            self.u1.delete(0, END)
            u.unitlis = []
            u.lis = []
    #Disable and Enable Unit/Bath Entry
    def dis_ena(self):
        ''' '''
        if gui.option.get() == 1:
            self.u1.delete(0, END)
            self.u1.configure(state='disabled')
            self.u1.update()
        else:
            self.u1.configure(state='normal')
            self.u1.update()
    #Reset
    def Reset(self):
        ''' '''
        
u = find_unit()
c = Find_cash()
gui = Mguiface()
mgui.mainloop()
