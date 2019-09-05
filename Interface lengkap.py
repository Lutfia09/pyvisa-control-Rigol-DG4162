import Tkinter as tk
import ttk

#import Tkinter
#import visa
#from Tkinter import *
#from ttk import *


#import visa

#rm = visa.ResourceManager()
#rm.list_resources()
#Rigol = rm.open_resource(u'USB0::0x1AB1::0x0641::DG4E163652069::INSTR',)
#Rigol=rm.open_resources(u'TCPIP0::169.254.176.48::INSTR',)
#Rigol.write(':COUPling:STATe OFF')
#Rigol.write(':COUPling:STATe?')
#print(Rigol.read())
#Rigol.write(':COUPling:CHannel:BASE CH2')
#Rigol.write(':COUPling:CHannel:BASE?')
#print(Rigol.read())

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageSINE, PageSQUARE, PageRAMP, PagePULSE, PageNOISE, PageARB, PageHARMONIC, PageUSER):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to Rigol's Software", fg='blue',
                         font=("Times New Roman", 20, "bold", "italic")).place(x=525, y=200)

        buttonSINE = tk.Button(self, width=10, text="SINE",fg='dark green', font=("Engravers MT", 10, "bold"),
                            command=lambda: controller.show_frame(PageSINE))
        buttonSINE.place(x=420, y=300)

        buttonSQUARE = tk.Button(self, width=10, text="SQUARE", fg='dark green', font=("Engravers MT", 10, "bold"),
                            command=lambda: controller.show_frame(PageSQUARE))
        buttonSQUARE.place(x=570, y=300)

        buttonRAMP = tk.Button(self, width=10, text="RAMP", fg='dark green', font=("Engravers MT", 10, "bold"),
                            command=lambda: controller.show_frame(PageRAMP))
        buttonRAMP.place(x=720, y=300)

        buttonPULSE = tk.Button(self, width=10, text="PULSE", fg='dark green', font=("Engravers MT", 10, "bold"),
                            command=lambda: controller.show_frame(PagePULSE))
        buttonPULSE.place(x=870, y=300)

        buttonNOISE = tk.Button(self, width=10, text="NOISE", fg='dark green', font=("Engravers MT", 10, "bold"),
                            command=lambda: controller.show_frame(PageNOISE))
        buttonNOISE.place(x=420, y=400)

        buttonARB = tk.Button(self, width=10, text="Arb", fg='dark green', font=("Engravers MT", 10, "bold"),
                            command=lambda: controller.show_frame(PageARB))
        buttonARB.place(x=570, y=400)

        buttonHARMONIC = tk.Button(self, width=10, text="HARMONIC", fg='dark green', font=("Engravers MT", 10, "bold"),
                            command=lambda: controller.show_frame(PageHARMONIC))
        buttonHARMONIC.place(x=720, y=400)

        buttonUSER = tk.Button(self, width=10, text="USER", fg='dark green', font=("Engravers MT", 10, "bold"),
                            command=lambda: controller.show_frame(PageUSER))
        buttonUSER.place(x=870, y=400)

        
class PageSINE(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Sine", fg='blue',
                         font=("Times New Roman", 20, "bold")).place(x=650, y=175)
        
        label = tk.Label(self, text='Frequency', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=250)
        self.entFrequency = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entFrequency.place(x=375, y=250)
        label = tk.Label(self, text='Hz', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=250)
       
        label = tk.Label(self, text='Periode', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=750, y=250)
        self.entPeriode = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entPeriode.place(x=1025, y=250)
        label = tk.Label(self, text='sec', fg='black',
              font=("Times New Roman", 12)).place(x=1200, y=250)

        label = tk.Label(self, text='Amplitudo', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=300)
        self.entAmplitudo = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entAmplitudo.place(x=375, y=300)
        label = tk.Label(self, text='Vpp', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=300)

        label = tk.Label(self, text='High Level', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=750, y=300)
        self.entHighLevel = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entHighLevel.place(x=1025, y=300)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 12)).place(x=1200, y=300)
        
        label = tk.Label(self, text='Offset', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=350)
        self.entOffset = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entOffset.place(x=375, y=350)
        label = tk.Label(self, text='Vdc', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=350)
        
        label = tk.Label(self, text='Low Level', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=750, y=350)
        self.entLowLevel = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entLowLevel.place(x=1025, y=350)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 12)).place(x=1200, y=350)
        
        label = tk.Label(self, text='Start Phase', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=400)
        self.entPhase = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entPhase.place(x=375, y=400)
        label = tk.Label(self, text='degree', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=400)
      
        label = tk.Label(self, text='Align Phase', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=450)
    
        button1 = tk.Button(self, text="Back to Home",fg='black',
              font=("Times New Roman", 12, "bold"), command=lambda: controller.show_frame(StartPage))
        button1.place(x=620, y=500)

        self.btnSendSine = tk.Button(self, width=8, text="SEND",
                                  fg='black', font=("Times New Roman", 12, "bold"),
            command=self.onSendSine)
        self.btnSendSine.place(x=770, y=500)

    def onSendSine(self, event=None):
        Frequency = self.entFrequency.get()
        Amplitudo = self.entAmplitudo.get()
        Offset = self.entOffset.get()
        Phasa = self.entPhase.get()
        Rigol.write('APPLy:SINusoid '+str(Frequency)+","+str(Amplitudo)+","+str(Offset)+","+str(Phasa))
        

class PageSQUARE(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Square", fg='blue',
                         font=("Times New Roman", 20, "bold")).place(x=635, y=100)

        label = tk.Label(self, text='Frequency', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=200)
        self.entFrequency = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entFrequency.place(x=375, y=200)
        label = tk.Label(self, text='Hz', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=200)

        label = tk.Label(self, text='Periode', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=750, y=200)
        self.entPeriode = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entPeriode.place(x=1025, y=200)
        label = tk.Label(self, text='sec', fg='black',
              font=("Times New Roman", 12)).place(x=1200, y=200)
        
        label = tk.Label(self, text='Amplitudo', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=250)
        self.entAmplitudo = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entAmplitudo.place(x=375, y=250)
        label = tk.Label(self, text='Vpp', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=250)

        label = tk.Label(self, text='High Level', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=750, y=250)
        self.entHighLevel = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entHighLevel.place(x=1025, y=250)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 12)).place(x=1200, y=250)

        label = tk.Label(self, text='Offset', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=300)
        self.entOffset = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entOffset.place(x=375, y=300)
        label = tk.Label(self, text='Vdc', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=300)
        
        label = tk.Label(self, text='Low Level', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=750, y=300)
        self.entLowLevel = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entLowLevel.place(x=1025, y=300)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 12)).place(x=1200, y=300)
        
        label = tk.Label(self, text='Start Phase', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=350)
        self.entPhase = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entPhase.place(x=375, y=350)
        label = tk.Label(self, text='degree', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=350)
      
        label = tk.Label(self, text='Duty Cycle', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=400)
        self.entDutyCycle = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entDutyCycle.place(x=375, y=400)
        label = tk.Label(self, text='%', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=400)

        label = tk.Label(self, text='Align Phase', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=450)
        
        button1 = tk.Button(self, text="Back to Home",fg='black',
              font=("Times New Roman", 12, "bold"), command=lambda: controller.show_frame(StartPage))
        button1.place(x=620, y=525)

        self.btnSendSquare = tk.Button(self, width=8, text="SEND",
                                  fg='black', font=("Times New Roman", 12, "bold"),
            command=self.onSendSquare)
        self.btnSendSquare.place(x=770, y=525)

    def onSendSquare(self, event=None):
        Frequency = self.entFrequency.get()
        Amplitudo = self.entAmplitudo.get()
        Offset = self.entOffset.get()
        Phasa = self.entPhase.get()
        Duty = self.entDutyCycle.get()
        Rigol.write('APPLy:SQUare '+str(Frequency)+","+str(Amplitudo)+","+str(Offset)+","+str(Phasa))
        Rigol.write(':FUNCtion:SQUare:DCYCle '+str(Duty))

        
class PageRAMP(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Ramp", fg='blue',
                         font=("Times New Roman", 20, "bold")).place(x=635, y=100)

        label = tk.Label(self, text='Frequency', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=200)
        self.entFrequency = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entFrequency.place(x=375, y=200)
        label = tk.Label(self, text='Hz', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=200)

        label = tk.Label(self, text='Periode', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=750, y=200)
        self.entPeriode = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entPeriode.place(x=1025, y=200)
        label = tk.Label(self, text='sec', fg='black',
              font=("Times New Roman", 12)).place(x=1200, y=200)
        
        label = tk.Label(self, text='Amplitudo', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=250)
        self.entAmplitudo = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entAmplitudo.place(x=375, y=250)
        label = tk.Label(self, text='Vpp', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=250)
        
        label = tk.Label(self, text='High Level', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=750, y=250)
        self.entHighLevel = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entHighLevel.place(x=1025, y=250)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 12)).place(x=1200, y=250)

        label = tk.Label(self, text='Offset', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=300)
        self.entOffset = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entOffset.place(x=375, y=300)
        label = tk.Label(self, text='Vdc', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=300)
        
        label = tk.Label(self, text='Low Level', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=750, y=300)
        self.entLowLevel = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entLowLevel.place(x=1025, y=300)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 12)).place(x=1200, y=300)
        
        label = tk.Label(self, text='Start Phase', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=350)
        self.entPhase = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entPhase.place(x=375, y=350)
        label = tk.Label(self, text='degree', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=350)
      
        label = tk.Label(self, text='Symmetry', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=400)
        self.entSymmetry = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entSymmetry.place(x=375, y=400)
        label = tk.Label(self, text='%', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=400)

        label = tk.Label(self, text='Align Phase', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=450)

        button1 = tk.Button(self, text="Back to Home",fg='black',
              font=("Times New Roman", 12, "bold"), command=lambda: controller.show_frame(StartPage))
        button1.place(x=620, y=525)

        self.btnSendRamp = tk.Button(self, width=8, text="SEND",
                                  fg='black', font=("Times New Roman", 12, "bold"),
            command=self.onSendRamp)
        self.btnSendRamp.place(x=770, y=525)

    def onSendRamp(self, event=None):
        Frequency = self.entFrequency.get()
        Amplitudo = self.entAmplitudo.get()
        Offset = self.entOffset.get()
        Phasa = self.entPhase.get()
        Symmetry = self.entSymmetry.get()
        Rigol.write('APPLy:RAMP '+str(Frequency)+","+str(Amplitudo)+","+str(Offset)+","+str(Phasa))
        Rigol.write(':FUNCtion:RAMP:SYMMetry '+str(Symmetry))

        
class PagePULSE(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Pulse", fg='blue',
                         font=("Times New Roman", 20, "bold")).place(x=635, y=100)
        
        label = tk.Label(self, text='Frequency', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=200)
        self.entFrequency = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entFrequency.place(x=375, y=200)
        label = tk.Label(self, text='Hz', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=200)

        label = tk.Label(self, text='Periode', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=750, y=200)
        self.entPeriode = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entPeriode.place(x=1025, y=200)
        label = tk.Label(self, text='sec', fg='black',
              font=("Times New Roman", 12)).place(x=1200, y=200)

        label = tk.Label(self, text='Amplitudo', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=250)
        self.entAmplitudo = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entAmplitudo.place(x=375, y=250)
        label = tk.Label(self, text='Vpp', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=250)     

        label = tk.Label(self, text='High Level', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=750, y=250)
        self.entHighLevel = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entHighLevel.place(x=1025, y=250)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 12)).place(x=1200, y=250)

        label = tk.Label(self, text='Offset', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=300)
        self.entOffset = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entOffset.place(x=375, y=300)
        label = tk.Label(self, text='Vdc', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=300)
        
        label = tk.Label(self, text='Low Level', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=750, y=300)
        self.entLowLevel = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entLowLevel.place(x=1025, y=300)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 12)).place(x=1200, y=300)
        
        label = tk.Label(self, text='Width', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=750, y=350)
        self.entWidth = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entWidth.place(x=1025, y=350)
        label = tk.Label(self, text='sec', fg='black',
              font=("Times New Roman", 12)).place(x=1200, y=350)

        label = tk.Label(self, text='Duty Cycle', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=400)
        self.entDutyCycle = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entDutyCycle.place(x=375, y=400)
        label = tk.Label(self, text='%', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=400)

        label = tk.Label(self, text='Leading', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=450)
        self.entLeading = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entLeading.place(x=375, y=450)
        label = tk.Label(self, text='sec', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=450)
        
        label = tk.Label(self, text='Trailing', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=750, y=400)
        self.entTrailing = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entTrailing.place(x=1025, y=400)
        label = tk.Label(self, text='sec', fg='black',
              font=("Times New Roman", 12)).place(x=1200, y=400)

        label = tk.Label(self, text='Start Phase', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=350)
        self.entPhase = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entPhase.place(x=375, y=350)
        label = tk.Label(self, text='degree', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=350)
        
        label = tk.Label(self, text='Align Phase', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=500)
        
        button1 = tk.Button(self, text="Back to Home",fg='black',
              font=("Times New Roman", 12, "bold"), command=lambda: controller.show_frame(StartPage))
        button1.place(x=620, y=575)

        self.btnSendPulse = tk.Button(self, width=8, text="SEND",
                                  fg='black', font=("Times New Roman", 12, "bold"),
            command=self.onSendPulse)
        self.btnSendPulse.place(x=770, y=575)

    def onSendPulse(self, event=None):
        Frequency = self.entFrequency.get()
        Amplitudo = self.entAmplitudo.get()
        Offset = self.entOffset.get()
        Phasa = self.entPhase.get()
        Duty = self.entDutyCycle.get()
        Leading = self.entLeading.get()
        Rigol.write('APPLy:PULSe '+str(Frequency)+","+str(Amplitudo)+","+str(Offset)+","+str(Phasa))
        Rigol.write(':PULSe:DCYCle '+str(Duty))
        Rigol.write(':PULSe:TRANsition '+str(Leading))
        
class PageNOISE(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Noise", fg='blue',
                         font=("Times New Roman", 20, "bold")).place(x=650, y=175)

        label = tk.Label(self, text='Amplitudo', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=300)
        self.entAmplitudo = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entAmplitudo.place(x=375, y=300)
        label = tk.Label(self, text='Vpp', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=300)    

        label = tk.Label(self, text='High Level', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=750, y=300)
        self.entHighLevel = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entHighLevel.place(x=1025, y=300)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 12)).place(x=1200, y=300)

        label = tk.Label(self, text='Offset', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=350)
        self.entOffset = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entOffset.place(x=375, y=350)
        label = tk.Label(self, text='Vdc', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=350)
        
        label = tk.Label(self, text='Low Level', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=750, y=350)
        self.entLowLevel = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entLowLevel.place(x=1025, y=350)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 12)).place(x=1200, y=350)
    
        button1 = tk.Button(self, text="Back to Home",fg='black',
              font=("Times New Roman", 12, "bold"), command=lambda: controller.show_frame(StartPage))
        button1.place(x=620, y=450)

        self.btnSendNoise = tk.Button(self, width=8, text="SEND",
                                  fg='black', font=("Times New Roman", 12, "bold"),
            command=self.onSendNoise)
        self.btnSendNoise.place(x=770, y=450)

    def onSendNoise(self, event=None):
        Amplitudo = self.entAmplitudo.get()
        Offset = self.entOffset.get()
        Rigol.write('APPLy:NOISe '+str(Amplitudo)+","+str(Offset))
        
        
class PageARB(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Arb", fg='blue',
                         font=("Times New Roman", 20, "bold")).place(x=660, y=25)

        label = tk.Label(self, text='Frequency', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=50, y=75)
        entFrequency = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entFrequency.place(x=375, y=75)
        label = tk.Label(self, text='Hz', fg='black',
              font=("Times New Roman", 8)).place(x=550, y=75)

        label = tk.Label(self, text='Periode', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=800, y=75)
        entPeriode = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entPeriode.place(x=1125, y=75)
        label = tk.Label(self, text='sec', fg='black',
              font=("Times New Roman", 8)).place(x=1300, y=75)

        label = tk.Label(self, text='Amplitudo', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=50, y=100)
        entAmplitudo = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entAmplitudo.place(x=375, y=100)
        label = tk.Label(self, text='Vpp', fg='black',
              font=("Times New Roman", 8)).place(x=550, y=100)

        label = tk.Label(self, text='High Level', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=800, y=100)
        entHighLevel = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entHighLevel.place(x=1125, y=100)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 8)).place(x=1300, y=100)

        label = tk.Label(self, text='Offset', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=50, y=125)
        entOffset = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entOffset.place(x=375, y=125)
        label = tk.Label(self, text='Vdc', fg='black',
              font=("Times New Roman", 8)).place(x=550, y=125)
        
        label = tk.Label(self, text='Low Level', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=800, y=125)
        entLowLevel = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entLowLevel.place(x=1125, y=125)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 8)).place(x=1300, y=125)
        
        label = tk.Label(self, text='Start Phase', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=50, y=150)
        entPhase = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entPhase.place(x=375, y=150)
        label = tk.Label(self, text='degree', fg='black',
              font=("Times New Roman", 8)).place(x=550, y=150)
      
        label = tk.Label(self, text='Align Phase', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=50, y=175)
        entAlignPhase = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))

        label = tk.Label(self, text='Point by point', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=50, y=200)
        #entFrequency = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        #entFrequency.place(x=225, y=400)
       
        label = tk.Label(self, text='Select Wave Form', fg='black',
                         font=("Times New Roman", 8, "bold")).place(x=50, y=225)

        label = tk.Label(self, text='Built in', fg='black',
                         font=("Times New Roman", 8, "bold")).place(x=75, y=250)

        label = tk.Label(self, text='Common', fg='black',
                         font=("Times New Roman", 8, "bold")).place(x=100, y=275)
        cb1 = ttk.Combobox(self, values=["DC", "AbsSine", "AbsSineHalf", "AmpALT", "AttALT",
                                         "GaussPulse", "NegRamp", "NPulse", "PPulse", "SineTra",
                                         "SineVer", "StairDn", "StairUD", "StairUp", "Trapezia"]).place(x=225, y=275)

        label = tk.Label(self, text='Engine', fg='black',
                         font=("Times New Roman", 8, "bold")).place(x=100, y=300)
        cb2 = ttk.Combobox(self, values=["BandLimited", "BlaseiWave", "Butterworth", "Chebyshev1", "Chebyshev2",
                                         "Combin", "CPulse", "CWPulse", "DampedOsc", "DualTone",
                                         "Gamma", "GateVibr", "LFMPulse", "MCNoise", "Discharge",
                                         "Pahcur", "Quake", "Radar", "Ripple", "RoundHalf",
                                         "RoundPM", "StepResp", "SwingOsc", "TV", "Voice"]).place(x=225, y=300)
                    
        label = tk.Label(self, text='Seg Mod', fg='black',
                         font=("Times New Roman", 8, "bold")).place(x=100, y=325)
        cb3 = ttk.Combobox(self, values=["AM", "FM", "PFM", "PM", "PWM"]).place(x=225, y=325)
                    
        label = tk.Label(self, text='Biolect', fg='black',
                         font=("Times New Roman", 8, "bold")).place(x=100, y=350)
        cb4 = ttk.Combobox(self, values=["Cardiac", "EOG", "EEG", "EMG", "Pulseilogram", "ResSpeed"]).place(x=225, y=350)
                    
        label = tk.Label(self, text='Medical', fg='black',
                        font=("Times New Roman", 8, "bold")).place(x=100, y=375)
        cb5 = ttk.Combobox(self, values=["LFPulse", "Tens1", "Tens2", "Tens3"]).place(x=225, y=375)

        label = tk.Label(self, text='Standard', fg='black',
                        font=("Times New Roman", 8, "bold")).place(x=100, y=400)
        cb6 = ttk.Combobox(self, values=["Ignition", "ISO16750-2 SP", "ISO16750-2 VR", "ISO7637-2 TP1", "ISO7637-2 TP2A",
                                         "ISO7637-2 TP2B", "ISO7637-2 TP3A", "ISO7637-2 TP3B", "ISO7637-2 TP4", "ISO7637-2 TP5A",
                                         "ISO7637-2 TP5B", "SCR", "Surge"]).place(x=225, y=400)

        label = tk.Label(self, text='Math', fg='black',
                        font=("Times New Roman", 8, "bold")).place(x=100, y=425)
        cb7 = ttk.Combobox(self, values=["Airy", "Besselj", "Bessely", "Cauchy", "Cubic",
                                         "Dirichlet", "Erf", "Erfc", "ErfcInv", "ErfInv",
                                         "ExpFall", "ExpRise", "Gauss", "HaverSine", "Laguerre",
                                         "Laplace", "Legend", "Log", "LogNormal", "Lorentz",
                                         "Maxwell", "Rayleigh", "Versierra", "Weibull", "ARB_X2"]).place(x=225, y=425)

        label = tk.Label(self, text='Trigonometri', fg='black',
                         font=("Times New Roman", 8, "bold")).place(x=100, y=450)
        cb8 = ttk.Combobox(self, values=["CosH", "CosInt", "Cot", "CotHCon", "CotHPro",
                                         "CscCon", "CscPro", "CscHCon", "CscHPro", "RecipCon",
                                         "RecipPro", "SecCon", "SecPro", "SecH", "Sinc",
                                         "SinH", "SinInt", "Sqrt", "Tan", "TanH"]).place(x=225, y=450)

        label = tk.Label(self, text='Anti Trigonometri', fg='black',
                        font=("Times New Roman", 8, "bold")).place(x=100, y=475)
        cb9 = ttk.Combobox(self, values=["ACos", "ACosH", "ACotCon", "ACotPro", "ACotHCon",
                                         "ACotHPro", "ACscCon", "ACscPro", "ACscHCon", "ACscHPro",
                                         "ASecCon", "ASecPro", "ASecH", "ASin", "ASinH",
                                         "ATan", "ATanH"]).place(x=225, y=475)

        label = tk.Label(self, text='Window Function', fg='black',
                       font=("Times New Roman", 8, "bold")).place(x=100, y=500)
        cb10 = ttk.Combobox(self, values=["Barlett", "BarthannWin", "Blackman", "BlackmanH", "BohmanWin",
                                         "Boxcar", "ChenWin", "FlattopWin", "Hamming", "Hanning",
                                         "Kaiser", "NuttalWin", "ParzenWin", "TaylorWin", "Triang",
                                         "TurkeyWin"]).place(x=225, y=500)

        label = tk.Label(self, text='Volatile Wave Form', fg='black',
                     font=("Times New Roman", 8, "bold")).place(x=75, y=525)        

        label = tk.Label(self, text='DC', fg='black',
                     font=("Times New Roman", 8, "bold")).place(x=75, y=550)

        #entFrequency = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        #entFrequency.place(x=225, y=400)

        #label = tk.Label(self, text='Create Wave Form', fg='black',
        #     font=("Times New Roman", 12, "bold")).place(x=100, y=450)
        #entFrequency = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        #entFrequency.place(x=225, y=450)
        
        #label = tk.Label(self, text='Edit Wave Form', fg='black',
        #     font=("Times New Roman", 12, "bold")).place(x=100, y=500)
        #entFrequency = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        #entFrequency.place(x=225, y=500)

        label = tk.Label(self, text='Create Wave Form', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=500, y=225)
        
        label = tk.Label(self, text='Cycle Periode', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=525, y=250)
        entCyclePeriode = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entCyclePeriode.place(x=650, y=250)
        label = tk.Label(self, text='sec', fg='black',
              font=("Times New Roman", 8)).place(x=825, y=250)

        label = tk.Label(self, text='High Level', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=525, y=275)
        entHighLevel = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entHighLevel.place(x=650, y=275)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 8)).place(x=825, y=275)

        label = tk.Label(self, text='Low Level', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=525, y=300)
        entLowLevel = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entLowLevel.place(x=650, y=300)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 8)).place(x=825, y=300)

        label = tk.Label(self, text='Points', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=525, y=325)
        entPoints = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entPoints.place(x=650, y=325)

        label = tk.Label(self, text='Interp', fg='black',
                       font=("Times New Roman", 8, "bold")).place(x=525, y=350)
        cb11 = ttk.Combobox(self, values=["Linear", "Off"]).place(x=650, y=350)

        label = tk.Label(self, text='Edit Points', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=525, y=375)

        label = tk.Label(self, text='Points', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=550, y=400)
        entFrequency = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entFrequency.place(x=675, y=400)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 8)).place(x=850, y=400)

        label = tk.Label(self, text='Time', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=550, y=425)
        entFrequency = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entFrequency.place(x=675, y=425)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 8)).place(x=850, y=425)

        label = tk.Label(self, text='Voltage', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=550, y=450)
        entFrequency = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entFrequency.place(x=675, y=450)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 8)).place(x=850, y=450)

        label = tk.Label(self, text='Insert', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=550, y=475)
        entFrequency = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entFrequency.place(x=675, y=475)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 8)).place(x=850, y=475)

        label = tk.Label(self, text='Delete', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=550, y=500)
        
        label = tk.Label(self, text='Ok', fg='black',
              font=("Times New Roman", 8, "bold")).place(x=550, y=525)

        button1 = tk.Button(self, text="Back to Home",fg='black',
              font=("Times New Roman", 12, "bold"), command=lambda: controller.show_frame(StartPage))
        button1.place(x=620, y=625)
        
class PageHARMONIC(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.v=tk.IntVar()
        self.radioButton()

        label = tk.Label(self, text="Harmonic", fg='blue',
                         font=("Times New Roman", 20, "bold")).place(x=625, y=75)

        label = tk.Label(self, text='Frequency', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=50, y=150)
        self.entFrequency = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entFrequency.place(x=225, y=150)
        label = tk.Label(self, text='Hz', fg='black',
              font=("Times New Roman", 12)).place(x=400, y=150)

        label = tk.Label(self, text='Periode', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=500, y=150)
        self.entPeriode = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entPeriode.place(x=675, y=150)
        label = tk.Label(self, text='sec', fg='black',
              font=("Times New Roman", 12)).place(x=850, y=150)

        label = tk.Label(self, text='Amplitudo', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=50, y=200)
        self.entAmplitudo = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entAmplitudo.place(x=225, y=200)
        label = tk.Label(self, text='Vpp', fg='black',
              font=("Times New Roman", 12)).place(x=400, y=200)

        label = tk.Label(self, text='High Level', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=500, y=200)
        self.entHighLevel = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entHighLevel.place(x=675, y=200)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 12)).place(x=850, y=200)

        label = tk.Label(self, text='Offset', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=50, y=250)
        self.entOffset = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entOffset.place(x=225, y=250)
        label = tk.Label(self, text='Vdc', fg='black',
              font=("Times New Roman", 12)).place(x=400, y=250)

        label = tk.Label(self, text='Low Level', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=500, y=250)
        self.entLowLevel = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entLowLevel.place(x=675, y=250)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 12)).place(x=850, y=250)
        
        label = tk.Label(self, text='Start Phase', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=50, y=300)
        self.entPhase = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entPhase.place(x=225, y=300)
        label = tk.Label(self, text='degree', fg='black',
              font=("Times New Roman", 12)).place(x=400, y=300)
        
        label = tk.Label(self, text='Align Phase', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=50, y=350)
        entAlignPhase = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        
        label = tk.Label(self, text='Order', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=50, y=400)
        self.entOrder = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        self.entOrder.place(x=225, y=400)
        
        label = tk.Label(self, text='Type', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=50, y=450)
        #entFrequency = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        #entFrequency.place(x=175, y=450)

        label = tk.Label(self, text='SN', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=50, y=500)
        #entFrequency = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        #entFrequency.place(x=175, y=500)
        
        label = tk.Label(self, text='Phase', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=50, y=550)
        #entFrequency = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        #entFrequency.place(x=175, y=550)
        
        button1 = tk.Button(self, text="Back to Home",fg='black',
              font=("Times New Roman", 12, "bold"), command=lambda: controller.show_frame(StartPage))
        button1.place(x=620, y=600)

        self.btnSendHarmonic = tk.Button(self, width=8, text="SEND",
                                  fg='black', font=("Times New Roman", 12, "bold"),
            command=self.onSendHarmonic)
        self.btnSendHarmonic.place(x=770, y=600)

    def onSendHarmonic(self, event=None):
        Frequency = self.entFrequency.get()
        Amplitudo = self.entAmplitudo.get()
        Offset = self.entOffset.get()
        Phasa = self.entPhase.get()
        Order = int(self.entOrder.get())
        Rigol.write('APPLy:HARMonic '+str(Frequency)+","+str(Amplitudo)+","+str(Offset)+","+str(Phasa))
        Rigol.write(':HARMonic:ORDEr '+str(Order))

    def radioButton(self):
        tk.Radiobutton(self, text="ODD",
                    command = self.tampilkan,variable=self.v,value=1).place(x=225, y=450)
        tk.Radiobutton(self, text="EVEN",
                    variable=self.v,command = self.tampilkan,value=2).place(x=325, y=450)

    def tampilkan(self):
        if self.v.get()==1:
            Rigol.write(':HARMonic:TYPe ODD')
        elif self.v.get()==2:
            Rigol.write(':HARMonic:TYPe EVEN')
        
        
class PageUSER(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="User", fg='blue',
                         font=("Times New Roman", 20, "bold")).place(x=650, y=175)

        label = tk.Label(self, text='Frequency', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=250)
        entFrequency = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entFrequency.place(x=375, y=250)
        label = tk.Label(self, text='Hz', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=250)

        label = tk.Label(self, text='Periode', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=750, y=250)
        entPeriode = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entPeriode.place(x=1025, y=250)
        label = tk.Label(self, text='sec', fg='black',
              font=("Times New Roman", 12)).place(x=1200, y=250)

        label = tk.Label(self, text='Amplitudo', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=300)
        entAmplitudo = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entAmplitudo.place(x=375, y=300)
        label = tk.Label(self, text='Vpp', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=300) 

        label = tk.Label(self, text='High Level', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=750, y=300)
        entHighLevel = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entHighLevel.place(x=1025, y=300)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 12)).place(x=1200, y=300)

        label = tk.Label(self, text='Offset', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=350)
        entOffset = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entOffset.place(x=375, y=350)
        label = tk.Label(self, text='Vdc', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=350)
        
        label = tk.Label(self, text='Low Level', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=750, y=350)
        entLowLevel = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entLowLevel.place(x=1025, y=350)
        label = tk.Label(self, text='Volt', fg='black',
              font=("Times New Roman", 12)).place(x=1200, y=350)
        
        label = tk.Label(self, text='Start Phase', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=400)
        entPhase = tk.Entry(self, bd=3, font=("Times New Roman", 10, "bold", "italic"))
        entPhase.place(x=375, y=400)
        label = tk.Label(self, text='degree', fg='black',
              font=("Times New Roman", 12)).place(x=550, y=400)
        
        label = tk.Label(self, text='Align Phase', fg='black',
              font=("Times New Roman", 12, "bold")).place(x=100, y=450)
            
        button1 = tk.Button(self, text="Back to Home",fg='black',
              font=("Times New Roman", 12, "bold"), command=lambda: controller.show_frame(StartPage))
        button1.place(x=620, y=500)
        

app = SeaofBTCapp()
app.title("Software RIGOL DG4162")
app.geometry("1920x1080+10+10")
app.mainloop()


