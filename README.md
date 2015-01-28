# NaoWizardOfOz
Wizard of Oz set-up in python for embodiment experiment with Nao

# Requirements
* pynaoqi-python-2.7-naoqi-1.14.5.X.Y (select X.Y = win32.exe, mac64.tar or linux64.tar for your OS)
* pyaudio (http://people.csail.mit.edu/hubert/pyaudio/)
* tkNotebook by Patrick T. Cossette (http://code.activestate.com/recipes/541092-tknotebook/)

# Use with physical Nao
* Run wizardOfOzRemote.py
* Have a Nao running and get its IP-address (pushing the chest button once)
* Enter the Nao's IP-address and port (default = 9559) under the 'Settings' tab
* Press the 'Connect to Nao' button
* If it says: "Succesfully connected to Nao!" you're good to go. If it says "An error occured!" see troubleshooting below.
* Go to the 'Behaviors' tab
* Select the right experimental settings.
* Select the behaviors you want to run (always start with initialization and end with close).

# Use with virtual Nao
* Run wizardOfOzRemote.py
* Start a virtual Nao in webots and get the IP-address of the computer that is simulating your Nao.
* Run playASoundServer.py on the same computer as the virtual Nao
* Enter the virtual Nao's IP-address and port (default = 9559) under the 'Settings' tab
* Enter the port of the playASoundServer (default = 50007)
* Press the 'Connect to Nao' button
* If should say: "Succesfully connected to Nao!" If it says "An error occured!" see troubleshooting below.
* Press the 'Connect to playASoundServer'
* If it says: "Succesfully connected to playASoundServer!" you're good to go. If it says "An error occured!" see troubleshooting below.
* Go to the 'Behaviors' tab
* Select the right experimental settings.
* Select the behaviors you want to run (always start with initialization and end with close).

# Troubleshooting
* Are you connected to the same network? This only works when you are.
* Does your firewall blocks the connections? Try to add webots and/or the ports you are using as an exception to your firewall. I do not recommend turning your firewall off completely.
* Have your tried turning it off and on again? No seriously, this fixes most of my problems. Don't forget to close python programms running in the background via your taskmanager.
