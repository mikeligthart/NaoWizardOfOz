from  Tkinter import *
from tkNotebook import Notebook
from embodimentExperiment import *

class WizardOfOzRemote(object):

    def __init__(self):
        #Default settings
        self.ipAddress = "192.168.1.102"
        self.port = 9559
        self.soundLocation = 'sounds/'
        self.chunkSize = 1024
        
        #Create canvas
        self.root = Tk()
        self.root.title("Nao remote")

        #Create notebook
        self.noteBook = Notebook(self.root, width=400, height=400, activefg='blue')
        self.noteBook.grid()

        #Create settings tab in notebook
        self.settingsTab = self.noteBook.add_tab(text = "Settings")
        self.drawSettingsTab()
        self.settingsTab.focus()

        #Create behavior tab in notebook
        self.behaviorTab = self.noteBook.add_tab(text = "Behaviors")
        self.drawBehaviorTab()

    def drawSettingsTab(self):
        #ipAddress GUI items
        Label(self.settingsTab, text="IP-address: ", anchor=W).grid(row=0, column = 0, sticky='EW')
        self.ipAddressEntry = Entry(self.settingsTab)
        self.ipAddressEntry.grid(row=0, column=1, sticky='EW')
        self.ipAddressEntry.insert(0,self.ipAddress)

        #port GUI items
        Label(self.settingsTab, text="Port: ", anchor=W).grid(row=1, column = 0, sticky='EW')
        self.portEntry = Entry(self.settingsTab)
        self.portEntry.grid(row=1, column=1, sticky='EW')
        self.portEntry.insert(0,self.port)

        #soundLocation GUI items
        Label(self.settingsTab, text="Sound file path: ", anchor=W).grid(row=2, column = 0, sticky='EW')
        self.soundLocationEntry = Entry(self.settingsTab)
        self.soundLocationEntry.grid(row=2, column=1, sticky='EW')
        self.soundLocationEntry.insert(0, self.soundLocation)

        #chunkSize GUI items
        Label(self.settingsTab, text="WAV chunk size: ", anchor=W).grid(row=3, column = 0, sticky='EW')
        self.chunkSizeEntry = Entry(self.settingsTab)
        self.chunkSizeEntry.grid(row=3, column=1, sticky='EW')
        self.chunkSizeEntry.insert(0, self.chunkSize)

        #Connect button
        Button(self.settingsTab, text="Connect", command=self.connect, anchor=E).grid(row=4, column=1, sticky='E')
        self.settingsErrorLabelText = StringVar()
        self.settingsErrorLabel = Label(self.settingsTab, textvariable=self.settingsErrorLabelText, wraplength=250, anchor=W, justify=LEFT)
        self.settingsErrorLabel.grid(row=5, column = 0, columnspan=2, sticky='EW')
        
    def drawBehaviorTab(self):
        Label(self.behaviorTab, text="Select a behavior for the Nao to execute:").grid(row=0, column = 0)
        Button(self.behaviorTab, text="Hi, how are you?").grid(column=0, row=1)

    def connect(self):
        try:
            #Retrieve parameters
            self.ipAddress = self.ipAddressEntry.get()
            self.port = int(self.portEntry.get())
            self.soundLocation = self.soundLocationEntry.get()
            self.chunkSize = int(self.chunkSizeEntry.get())

            #Create new EmbodimentExperiment instance
            self.experiment = EmbodimentExperiment(self.ipAddress, self.port, self.soundLocation, self.chunkSize)
            
        except ValueError:
            #Port or chunkSize aren't numbers
            self.settingsErrorLabel.config(fg = 'red')
            self.settingsErrorLabelText.set("An error occured!\nPort and WAV chunk size must be integers.")
        except Exception as e:
            #Most likely not connected to Nao
            self.settingsErrorLabel.config(fg = 'red')
            self.settingsErrorLabelText.set("An error occured!\n" + e.message)
        else:
            #If everything is OK the remote is connected
            self.settingsErrorLabel.config(fg = 'green')
            self.settingsErrorLabelText.set("Succesfully connected!")

    def run(self):
        #Starts and runs the GUI
        self.root.mainloop()

if __name__ == "__main__":
    remote = WizardOfOzRemote()
    remote.run()
