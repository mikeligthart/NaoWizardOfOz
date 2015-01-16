import Tkinter
from embodimentExperiment import *

class WizardOfOzRemote(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        self.experiment = EmbodimentExperiment("10.0.1.2")
        self.experiment.initialization(False)

    def initialize(self):
        self.grid()

        button = Tkinter.Button(self, text=u"Hi, how are you?", command=self.OnButtonClick)
        button.grid(column=0, row=0)

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,True)

    def OnButtonClick(self):
        self.experiment.neutral_1(False)

if __name__ == "__main__":
    remote = WizardOfOzRemote(None)
    remote.title('Wizard Remote')
    remote.mainloop()
