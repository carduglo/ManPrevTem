from Tkinter import *

class main:
    def __init__(self,master):
        self.frame = Frame(master)
        self.frame.place()

                        
root = Tk()
root.title("Aqui vai o titulo da Janela")
root.geometry("800x600")
main(root)
root.mainloop()