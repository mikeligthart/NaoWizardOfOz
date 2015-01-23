from  Tkinter import *
from tkNotebook import Notebook
from embodimentExperiment import *

class WizardOfOzRemote(object):

    def __init__(self):
        #Default settings
        self.ipAddress = "192.168.1.102"#"131.174.106.230"
        self.port = 9559
        self.soundPort = 50007
        self.isConnected = False
        
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
        Label(self.settingsTab, text="Port Nao: ", anchor=W).grid(row=1, column = 0, sticky='EW')
        self.portEntry = Entry(self.settingsTab)
        self.portEntry.grid(row=1, column=1, sticky='EW')
        self.portEntry.insert(0,self.port)

        #soundPort
        Label(self.settingsTab, text="Port playASoundServer: ", anchor=W).grid(row=2, column = 0, sticky='EW')
        self.soundPortEntry = Entry(self.settingsTab)
        self.soundPortEntry.grid(row=2, column=1, sticky='EW')
        self.soundPortEntry.insert(0, self.soundPort)

        #Connect button
        Button(self.settingsTab, text="Connect", command=self.connect, anchor=E).grid(row=3, column=1, sticky='E')

        #Error messages
        self.settingsErrorLabelText = StringVar()
        self.settingsErrorLabel = Label(self.settingsTab, textvariable=self.settingsErrorLabelText, wraplength=250, anchor=W, justify=LEFT)
        self.settingsErrorLabel.grid(row=4, column = 0, columnspan=2, sticky='EW')

        
    def connect(self):
        try:
            #Retrieve parameters
            self.ipAddress = self.ipAddressEntry.get()
            self.port = int(self.portEntry.get())
            self.soundPort = int(self.soundPortEntry.get())

            #Create new EmbodimentExperiment instance
            self.experiment = EmbodimentExperiment(self.ipAddress, self.port, self.soundPort)
            
        except ValueError:
            #Port or chunkSize aren't numbers
            self.settingsErrorLabel.config(fg = 'red')
            self.settingsErrorLabelText.set("An error occured!\nThe ports must be an integer")
        except Exception as e:
            #Most likely not connected to Nao
            self.settingsErrorLabel.config(fg = 'red')
            self.settingsErrorLabelText.set("An error occured!\n" + e.message)
        else:
            #If everything is OK the remote is connected
            self.isConnected = True
            self.settingsErrorLabel.config(fg = 'green')
            self.settingsErrorLabelText.set("Succesfully connected!")
            self.enableBehaviorButtons()        
            
    def drawBehaviorTab(self):
        ## SETTINGS ##
        #Change experimental settings
        Label(self.behaviorTab, text="Experimental settings:", anchor=W).grid(row=0, column = 0, sticky='W')
        self.isPhysical = BooleanVar()
        self.isPhysical.set(True)
        self.isSocial = BooleanVar()
        self.isSocial.set(True)
        Radiobutton(self.behaviorTab, text="Physical", variable=self.isPhysical, value=True).grid(row=1, column=0)
        Radiobutton(self.behaviorTab, text="Virtual", variable=self.isPhysical, value=False).grid(row=1, column=1)
        Radiobutton(self.behaviorTab, text="Neutral", variable=self.isSocial, value=False).grid(row=2, column=0)
        Radiobutton(self.behaviorTab, text="Social", variable=self.isSocial, value=True).grid(row=2, column=1)

        #Select behaviors
        self.behaviorSelectLabelText = StringVar()
        self.behaviorSelectLabelText.set("Connect to Naoqi in order to select a behavior")
        Label(self.behaviorTab, textvariable=self.behaviorSelectLabelText).grid(row=3, column = 0)

        ## BUTTONS ##
        #[buttonText, trial, buttonRow, buttonColumn]
        behaviorButtonsOutline = [["Initialization (before participant is in room)", 0, 4, 0],
                                ["Close the shop", 999, 4, 1],
                                ["1. Hi, how are you?", 1, 5, 0],
                                ["2. What is the matter?", 2, 6, 0],
                                ["3. Cold outside", 3, 7, 0],
                                ["4. Robot football", 4, 8, 0],
                                ["5. Keep fit", 5, 9, 0],
                                ["6. Theater", 6, 10, 0],
                                ["7. Comedian", 7, 11, 0]]

        self.behaviorButtons = self.buildBehaviorButtons(behaviorButtonsOutline)

    def buildBehaviorButtons(self, drafts):
        behaviorButtons = []
        for draft in drafts:
            button = Button(self.behaviorTab, text=draft[0], anchor=W, bg='grey', command=lambda b=draft[1]: self.behavior(b), state=DISABLED)
            button.grid(row=draft[2], column=draft[3], sticky='EW')
            behaviorButtons.append(button)
        return behaviorButtons
    
    def enableBehaviorButtons(self):
        #Make the behavior buttons selectable after connecting to a Naoqi instance
        self.behaviorSelectLabelText.set("Select a behavior for the Nao to execute:")
        for behaviorButton in self.behaviorButtons:
            behaviorButton.config(state=NORMAL)
        
    ## RUN RIGHT BEHAVIOR ##
    def behavior(self, trial):
        if trial == 0:
            self.experiment.initialization()
        elif trial == 999:
            self.experiment.close()
        else:
            self.experiment.behavior(trial, self.isPhysical.get(), self.isSocial.get())

    ## RUN PROGRAM ##
    def run(self):
        #Starts and runs the GUI
        self.root.mainloop()

## AUTOSTART ##
if __name__ == "__main__":
    remote = WizardOfOzRemote()
    remote.run()
