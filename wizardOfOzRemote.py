from  Tkinter import *
from tkNotebook import Notebook
from embodimentExperiment import *

class WizardOfOzRemote(object):

    def __init__(self):
        #Default settings
        self.ipAddress = "131.174.106.230"#"131.174.106.203"
        self.port = 9559
        self.soundPort = 50007
        self.isConnected = False
        
        #Create canvas
        self.root = Tk()
        self.root.title("Nao remote")

        #Create notebook
        self.noteBook = Notebook(self.root, width=400, height=600, activefg='blue')
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

        #Connect to Nao button
        Button(self.settingsTab, text="Connect to Nao", command=self.connectToNao, anchor=E).grid(row=2, column=1, sticky='E')

        #port GUI items
        Label(self.settingsTab, text="Port playASoundServer: ", anchor=W).grid(row=3, column = 0, sticky='EW')
        self.soundPortEntry = Entry(self.settingsTab)
        self.soundPortEntry.grid(row=3, column=1, sticky='EW')
        self.soundPortEntry.insert(0,self.soundPort)

        #Connect to Sound server
        Button(self.settingsTab, text="Connect to playASoundServer", command=self.connectToPlayASoundServer, anchor=E).grid(row=4, column=1, sticky='E')

        #Error messages
        self.settingsErrorLabelText = StringVar()
        self.settingsErrorLabel = Label(self.settingsTab, textvariable=self.settingsErrorLabelText, wraplength=250, anchor=W, justify=LEFT)
        self.settingsErrorLabel.grid(row=5, column = 0, columnspan=2, sticky='EW')

        
    def connectToNao(self):
        try:
            #Retrieve parameters
            self.ipAddress = self.ipAddressEntry.get()
            self.port = int(self.portEntry.get())

            #Create new EmbodimentExperiment instance
            self.experiment = EmbodimentExperiment(self.ipAddress, self.port)
            
        except ValueError:
            #Port is not an int
            self.settingsErrorLabel.config(fg = 'red')
            self.settingsErrorLabelText.set("An error occured!\nThe port integer")
        except Exception as e:
            #Most likely not connected to Nao
            self.settingsErrorLabel.config(fg = 'red')
            self.settingsErrorLabelText.set("An error occured!\n" + e.message)
        else:
            #If everything is OK the remote is connected
            self.isConnected = True
            self.settingsErrorLabel.config(fg = 'green')
            self.settingsErrorLabelText.set("Succesfully connected to Nao!")
            self.enableBehaviorButtons()

    def connectToPlayASoundServer(self):
        try:
            #get values
            self.ipAddress = self.ipAddressEntry.get()
            self.soundPort = int(self.soundPortEntry.get())
            #connect
            self.experiment.connectToPlayASoundServer(self.ipAddress, self.soundPort)
        except ValueError:
            #Port is not an int
            self.settingsErrorLabel.config(fg = 'red')
            self.settingsErrorLabelText.set("An error occured!\nThe port integer")
            #Something else is going on
        except Exception as e:
            self.settingsErrorLabel.config(fg = 'red')
            self.settingsErrorLabelText.set("An error occured!\n" + e.message)
        else:
            self.settingsErrorLabel.config(fg = 'green')
            self.settingsErrorLabelText.set("Succesfully connected to playASoundServer!")
            
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
                                ["Off-script", 998, 5, 1],
                                ["1. Start", 1, 5, 0],
                                ["2. P says name", 2, 6, 0],
                                ["3. P says 'I'm alright'", 3, 7, 0],
                                ["4. P says 'outside a lot'", 4, 8, 0],
                                ["5. P says 'new years resolution?'", 5, 9, 0],
                                ["6. P says 'game on Sunday'", 6, 10, 0],
                                ["7. P says 'theater more often'", 7, 11, 0],
                                ["8. P says 'make me laugh'", 8, 12, 0],
                                ["9. P says 'coming back'", 9, 13, 0],
                                ["10. P says 'could be actor'", 10, 14, 0],
                                ["11. P says 'wins an Oscar then'", 11, 15, 0],
                                ["12. P says 'drink or eat sometimes?'", 12, 16, 0],
                                ["13. P says 'they are hungry'", 13, 17, 0],
                                ["14. P says 'also need a break'", 14, 18, 0],
                                ["15. P says 'go shopping'", 15, 19, 0],
                                ["16. End", 16, 20, 0]]

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
            self.experiment.close(self.isPhysical.get())
        elif trial == 998:
            self.experiment.offScript(self.isPhysical.get())
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
