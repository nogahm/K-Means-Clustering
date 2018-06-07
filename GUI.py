try:
    # for Python2
    from Tkinter import Tk, Label, Button, Entry, IntVar, END, W, E   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E   ## notice lowercase 't' in tkinter here

##from Tkinter import Tk, Label, Button, Entry, IntVar, END, W, E


class GUI:

    def __init__(self, master):
        self.master = master
        master.title("K-Means Clustering")

        self.total = 0
        self.entered_number = 0

        #Data path
        self.pathLabel = Label(master, text="Data path:")
        vcmd = master.register(self.validate) # we have to wrap the command
        self.pathEntry = Entry(master, validate="key") ##path for data
        self.browse_button = Button(master, text="Browse", command=lambda: self.update("browse"))

        #Num of clusters k
        self.numOfClusLabel = Label(master, text="Num of clusters k:")
        vcmd = master.register(self.validate)  # we have to wrap the command
        self.numOfClusEntry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        #Num of runs
        self.numOfRunsLabel = Label(master, text="Num of runs:")
        vcmd = master.register(self.validate)  # we have to wrap the command
        self.numOfRunsEntry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        #pre process
        self.prePro_button = Button(master, text="Pre-Process", command=lambda: self.update("Pre-Process"))

        #cluster
        self.cluster_button = Button(master, text="Cluster", command=lambda: self.update("cluster"))

        # LAYOUT
        self.pathLabel.grid(row=1, column=0)
        self.pathEntry.grid(row=1, column=1, sticky=W+E)
        self.browse_button.grid(row=1,column=2)

        self.numOfClusLabel.grid(row=2, column=0)
        self.numOfClusEntry.grid(row=2, column=1)

        self.numOfRunsLabel.grid(row=3, column=0)
        self.numOfRunsEntry.grid(row=3, column=1)

        self.prePro_button.grid(row=4, column=1)

        self.cluster_button.grid(row=5, column=1)

    def validate(self, new_text):
        if not new_text:  # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else:  # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.pathEntry.delete(0, END)

root = Tk()
my_gui = GUI(root)
root.mainloop()