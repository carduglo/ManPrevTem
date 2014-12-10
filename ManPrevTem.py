from Tkinter import *

class main:
    def __init__(self,master):
        self.frame = Frame(master)
        self.frame.place()

                        
root = Tk()
root.title("Manutencao Preventiva Temporal")
root.geometry("1024x768")
main(root)
root.mainloop()