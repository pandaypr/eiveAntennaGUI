# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


try:
    import tkinter as tk
    from Display import TestFrame
    from COMPorts import listOfPorts, initialConnection, ATCommands
    from tkinter import HORIZONTAL
except Exception as e:
    print("The library {}".format(e))

class loop(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EIVE")
        self.iconbitmap('eive.ico')
        self.geometry("600x600")

        for r in range(2):
            self.rowconfigure(r, weight=1)
        for c in range(2):
            self.columnconfigure(c, weight=1)

            # First frame
            self.COMFrame = TestFrame()
            self.COMFrame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')  # Outside of the frame Padding

            COMPorts = listOfPorts()
            ComPort = initialConnection(COMPorts)
            COMPort = tk.StringVar(self)
            COM = ComPort
            COMPort.set(ComPort)
            print(ComPort)
            print(COMPorts, COMPort)
            label = tk.Label(self.COMFrame,text="CONNECTION", font=('Arial Black', 13), borderwidth=2, relief="ridge", bg="yellow").grid(row=0, column=0)
            ConnectBtn = tk.Button(self.COMFrame, text=" Connect ").grid(row=1, column=0)
            DisconnectBtn = tk.Button(self.COMFrame, text="Disconnect").grid(row=2, column=0)
            COMPort = tk.OptionMenu(self.COMFrame, COMPort, *COMPorts)  # Use Entry to insert a input field
            COMPort.grid(row=1, column=1)
            BaudRate = tk.Entry(self.COMFrame, width=10, borderwidth=2)  # Use Entry to insert a input field
            BaudRate.insert(0, '19200')  # Displays this msg on the input field itself
            BaudRate.grid(row=2, column=1)


            #2nd Frame for Position
            self.AngleFrame = TestFrame()
            self.AngleFrame.grid(row=1, column=0, padx=10, sticky='nsew')  # Outside of the frame Padding
            label = tk.Label(self.AngleFrame, bg="yellow", text="POSITION", font=('Arial Black', 13), borderwidth=2, relief="ridge").grid(row=0, column=0)
            label = tk.Label(self.AngleFrame, text="AZIMUTH").grid(row=1, column=0)
            label = tk.Label(self.AngleFrame, text="ELEVATION").grid(row=1, column=2)

            #Azimuth Angle Value Set
            AZSet = tk.Entry(self.AngleFrame, width=8, borderwidth=2)
            AZSet.insert(0, ATCommands(ComPort, 'AT'))
            AZSet.config(state='normal')
            AZSet.grid(row=2, column=0)
            SetAZ = tk.Button(self.AngleFrame, text="Set",
                                       command=lambda: self.Click(ComPort, AZSet, OutputBox)).grid(row=2,column=1)

            # Azimuth Angle Value View
            AZSet = tk.Entry(self.AngleFrame, width=8, borderwidth=2, font=('Helvetica', 15))
            AZSet.insert(0, ATCommands(ComPort, 'AT'))
            AZSet.config(state='disabled')
            AZSet.grid(row=3, column=0)

            # Elevation Angle Value Set
            ELSet = tk.Entry(self.AngleFrame, width=6, borderwidth=2)
            ELSet.insert(0, ATCommands(ComPort, 'AT'))
            ELSet.config(state='normal')
            ELSet.grid(row=2, column=2)
            SetEL = tk.Button(self.AngleFrame, text="Set",
                              command=lambda: self.Click(ComPort, ELSet, OutputBox)).grid(row=2, column=3)

            # Elevation Angle Value View
            AZSet = tk.Entry(self.AngleFrame, width=6, borderwidth=2, font=('Helvetica', 15))
            AZSet.insert(0, ATCommands(ComPort, 'AT'))
            AZSet.config(state='disabled')
            AZSet.grid(row=3, column=2)

            #3rd Frame for MISC things
            self.Misc = TestFrame()
            self.Misc.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')  # Outside of the frame Padding

            label = tk.Label(self.Misc, bg="yellow", text="Messages", font=('Arial Black', 13), borderwidth=2,
                             relief="ridge").grid(row=0, column=0)
            AT = tk.Label(self.Misc, text="Status 1").grid(row=1, column=0)
            Signal = tk.Label(self.Misc, text="Status 2").grid(row=2, column=0)
            Network = tk.Label(self.Misc, text="Status 3").grid(row=3, column=0)
            Versions = tk.Label(self.Misc, text="Option 1").grid(row=4, column=0)
            SubNum = tk.Label(self.Misc, text="Option 2").grid(row=5, column=0)
            IMEI = tk.Label(self.Misc, text="Option 3").grid(row=6, column=0)
            SignalQualityBtn = tk.Label(self.Misc, text="Warning 1").grid(row=7, column=0)
            SignalQualityBtn = tk.Label(self.Misc, text="Warning 2").grid(row=8, column=0)
            SignalQualityBtn = tk.Label(self.Misc, text="Warning 3").grid(row=9, column=0)


            ATView = tk.Entry(self.Misc, width=20, borderwidth=2)
            ATView.insert(0, ATCommands(ComPort, 'AT'))
            ATView.config(state='disabled')
            ATView.grid(row=1, column=1)

            SignalView = tk.Entry(self.Misc, width=20, borderwidth=2)
            SignalView.insert(0, ATCommands(ComPort, 'AT+CSQ'))
            SignalView.config(state='disabled')
            SignalView.grid(row=2, column=1)

            NetworkView = tk.Entry(self.Misc, width=20, borderwidth=2)
            NetworkView.insert(0, ATCommands(ComPort, 'AT+CREG'))
            NetworkView.config(state='disabled')
            NetworkView.grid(row=3, column=1)

            VersionsView = tk.Entry(self.Misc, width=20, borderwidth=2)
            VersionsView.insert(0, ATCommands(ComPort, 'AT&V'))
            VersionsView.config(state='disabled')
            VersionsView.grid(row=4, column=1)

            SubNumView = tk.Entry(self.Misc, width=20, borderwidth=2)
            SubNumView.insert(0, ATCommands(ComPort, 'AT+CNUM'))
            SubNumView.config(state='disabled')
            SubNumView.grid(row=5, column=1)

            IMEIView = tk.Entry(self.Misc, width=20, borderwidth=2)
            IMEIView.insert(0, ATCommands(ComPort, 'AT+GSN'))
            IMEIView.config(state='disabled')
            IMEIView.grid(row=6, column=1)

            SignalQualityView = tk.Entry(self.Misc, width=20, borderwidth=2)
            SignalQualityView.insert(0, ATCommands(ComPort, 'AT+CSQ'))
            SignalQualityView.config(state='disabled')
            SignalQualityView.grid(row=7, column=1)

            SignalQualityView = tk.Entry(self.Misc, width=20, borderwidth=2)
            SignalQualityView.insert(0, ATCommands(ComPort, 'AT+CSQ'))
            SignalQualityView.config(state='disabled')
            SignalQualityView.grid(row=8, column=1)

            SignalQualityView = tk.Entry(self.Misc, width=20, borderwidth=2)
            SignalQualityView.insert(0, ATCommands(ComPort, 'AT+CSQ'))
            SignalQualityView.config(state='disabled')
            SignalQualityView.grid(row=9, column=1)

            #4th Frame for arror control
            self.Arrows = TestFrame()
            self.Arrows.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky='nsew')  # Outside of the frame Padding

            label = tk.Label(self.Arrows, bg="yellow", text="CONTROL", font=('Arial Black', 13), borderwidth=2,
                             relief="ridge").grid(row=0, column=0, columnspan=2)
            RightBtn = tk.Button(self.Arrows, text=u'\u25B6', font=('Helvetica', 25),
                                       command=lambda: self.Click(ComPort, AZSet, OutputBox)).grid(row=2,column=2)
            left = tk.Button(self.Arrows, text=u'\u25C0', font=('Helvetica', 25),
                                       command=lambda: self.Click(ComPort, AZSet, OutputBox)).grid(row=2,column=0)
            top = tk.Button(self.Arrows, text=u'\u25B2', font=('Helvetica', 25),
                                       command=lambda: self.Click(ComPort, AZSet, OutputBox)).grid(row=1,column=1)

            bottom = tk.Button(self.Arrows, text=u'\u25BC', font=('Helvetica', 25),
                                       command=lambda: self.Click(ComPort, AZSet, OutputBox)).grid(row=3,column=1)
            bottom =  tk.Button(self.Arrows, text=u'\u25A0', font=('Helvetica', 25),
                                       command=lambda: self.Click(ComPort, AZSet, OutputBox)).grid(row=2,column=1)
            label = tk.Label(self.Arrows, bg="yellow", text="Speed", font=('Arial Black', 8), borderwidth=2,
                             relief="ridge").grid(row=4, column=0)
            RotationSpeed = tk.Scale(self.Arrows, from_=0x00, to =0xFF, background="red",  borderwidth=2, relief="ridge",
                                     orient=HORIZONTAL, length = 200, resolution=10).grid(row=5, column = 0, columnspan=3)  # Use Entry to insert a input field

            # 5th Frame for Displaying the power of the recieved signal
            self.Power = TestFrame()
            self.Power.grid(row=2, column=1, padx=10, pady=10,sticky='nsew')  # Outside of the frame Padding
            label = tk.Label(self.Power, bg="yellow", text="Power Recieved", font=('Arial Black', 13), borderwidth=2,
                             relief="ridge").grid(row=0, column=0, columnspan=2)
            BaudRate = tk.Entry(self.Power, width=10, borderwidth=2,  font=('Helvetica', 25))  # Use Entry to insert a input field
            BaudRate.insert(0, '3dB')  # Displays this msg on the input field itself
            BaudRate.grid(row=2, column=1)


""" self.Modem = TestFrame()
            self.Modem.grid(row=0, column=10, rowspan=2, padx=5, pady=10, sticky='nsew')  # Outside of the frame Padding
            OutputBox = tk.Text(self.Modem, height=20, width=50)
            OutputBox.pack()

        def Click(self, COM, e, OutputBox):
            # History to be built
            command = e.get()
            response = ATCommands(COM, command)
            e.delete(0, 'end')
            command1 = command + " : \t "
            response1 = response + '\n'
            enteredCommand = OutputBox.insert(tk.END, command1)
            out = OutputBox.insert(tk.END, response1)
            # e.insert(0, response)
            return"""



loop().mainloop()