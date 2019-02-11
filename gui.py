# module 3 exercise: GUI with Tkinter

import tkinter as tk

class sampleGUI(tk.Tk):     # main window class for GUI, derived from the Tk class
    def __init__(self):
        super().__init__()      # initialize Tk parent class 
                                # because we want the init method to run
                                # telling the program to run the init function of tk
        
        # add title to window
        self.title("sample GUI exercise")
        # resize 
        self.resizable(True, False)   # horizontal only
        #self.resizable(False, True)   # vertical only
        #self.resizable(False, False)  # 
               # fOR Mac, the options are: True, True as default
        

        # create label widgets and see how grid works
        Lred = tk.Label(self, text="red", fg="red")           # create a label in red    # self is current window
        Lblue = tk.Label(self, text="blue", fg="blue")        # create a label in blue
        Lpurple = tk.Label(self, text="purple", fg="purple")  # create a label in purple
        Llblue = tk.Label(self, text="light blue", fg="light blue")  # create a long label
        
        Lred.grid()                      # row 0, col 0 
        Lblue.grid(row=0, column=2)      # row 0, col 2 but appears next to red                              
        #Lpurple.grid(row=1, column=1, columnspan=2)   # row 1, col1, column span 2
        Llblue.grid(row=0, column=1)    # 
        Lpurple.grid(row=1, column=1, columnspan=2, sticky='e')  # instead of being centered, now the purple is all the way to the east  
        
        self.grid_columnconfigure(1, weight=1)  #
        
        
        # create a button and callback function
        def fct() : print("Clicked!")         # 
        b = tk.Button(self, text="Click me", command=fct)   # button with "click me"
                                             # command here is the argument for callback
        b.grid()        
        '''
        '''
        # call back and lambda
        def printNum(n) : print(n, "is clicked")
        b1 = tk.Button(self, text = "button 1", command = lambda : printNum(1))    # lambda is used when receiving info
        b2 = tk.Button(self, text = "button 2", command = lambda : printNum(2))
        b1.grid()
        b2.grid(row=0, column=1)
        '''
        '''
        # create an entry text box and Tk variables           
        entryText = tk.StringVar()
        tk.Entry(self, textvariable=entryText).grid()
        
        # create a label to display user text
        labelText = tk.StringVar()
        l = tk.Label(self, textvariable=entryText, bg="light blue")    
        l.grid(sticky='we', columnspan=1)                               
        
        
        # create a set of radiobuttons
        def printChoice() : 
            c = cv.get()       # 
            labelText.set("You have chosen choice  " + str(c))     # callback function
        
        cv = tk.IntVar()      # control var is an int, can be a string, cv is just a variable name, it can be named anything
        rb1 = tk.Radiobutton(self, text="Choice 1", variable=cv, value=1, command=printChoice).grid(sticky='w')
        rb2 = tk.Radiobutton(self, text="Choice 2", variable=cv, value=2, command=printChoice).grid(sticky='w')
        rb3 = tk.Radiobutton(self, text="Choice 3", variable=cv, value=3, command=printChoice).grid(sticky='w')
                                                                               # set sticky to w so it stays on left side
        cv.set(1)  # auto-select the first button
        # cv.set(0)    # does not auto-select any choice 

        # create a label to display user choice
        labelText = tk.StringVar()
        l = tk.Label(self, textvariable=labelText, bg="white")   
        l.grid(sticky='we', columnspan=5)                  
        
        '''
        '''
        # create a scroll bar and a listbox
        # create scrollbar
        s = tk.Scrollbar(self)            
        
        # create a listbox
        listItems = "one two three four five six".split()
        #lbox = tk.Listbox(self, height=4)                          # allow 1 choice
        #lbox = tk.Listbox(self, height=4, selectmode="extended")   # allow multiple choices
        lbox = tk.Listbox(self, height=10, yscrollcommand=s.set)     # connects the Listbox with Scrollbar
        for item in listItems:
            lbox.insert(tk.END, item)   # fill in the list box with list items
                        # insert at the end, the last position. if wish to insert from the beginning, then tk.zero
        lbox.grid(sticky='we')
        
        # connect scrollbar to listbox
        s.config(command=lbox.yview)    # callback
        s.grid(row=0,column=1, sticky='nsw') # we have to specify the row number here, 
                                           # because if we don't, then the scrolbar would be shown below the lbox
        
        # create a button to get the user choice
        def fct() : 
            print("You chose", (lbox.curselection()[0]+1))       # run this for listbox with 1 selection
            #print("You chose", len(self.lbox.curselection()))        # run this for listbox with multiple selections
        tk.Button(self, text="Click to select choice in list", command=fct).grid()   # button 
        
        #  the number of widgets are the number of grids.

        # create a menu and menubutton
        def printChoice(n) :  print("You chose choice", n)
            
        mb = tk.Menubutton(self, text='choices')
        mb.grid()
        
        mb.menu = tk.Menu(mb, tearoff=0)    # mb is master of menu ***
        mb['menu'] = mb.menu
        
        mb.menu.add_command(label="choice 1", command=lambda:printChoice(1))   # lambda callback, it has an argument, 
                                                                               # we want to know which one does the user choose
        mb.menu.add_command(label="choice 2", command=lambda:printChoice(2))  
        
        subMenu = tk.Menu(mb.menu, tearoff=0)    # menu is master of submenu ***
        mb.menu.add_cascade(label="menu 3", menu=subMenu)
        
        subMenu.add_command(label="subchoice 1", command=lambda:printChoice(31))
        subMenu.add_command(label="subchoice 2", command=lambda:printChoice(32))
        
        
# this should be in a different module, and it should import the sampleGUI module
def main() :
    app = sampleGUI()          # create sample GUI object
    app.mainloop()             # the main loop method runs until the x is clicked on the main window
    
main()
        
