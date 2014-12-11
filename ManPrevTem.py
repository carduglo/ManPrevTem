# -*- coding: UTF-8 -*-


from Tkinter import *
import ttk

class main:
    def __init__(self,master):

    	self.abas = ttk.Notebook(master)
        #self.abas.configure(width=1024) Ainda não descobri pra que serve isso
        self.abas.configure(takefocus="")
        self.abas_pg0 = ttk.Frame(self.abas)
        self.abas.add(self.abas_pg0, padding=3)
        self.abas.tab(0, text="Cliente",underline="-1")
         

        self.abas.place(relx=0.0,rely=0.0,relheight=1.0,relwidth=1.0)
#========================================Placa=================================================
        self.label_placa = Label(self.abas_pg0, text = 'Placa', font = ('Ariel', '15'))# criei o label=escrita
        self.label_placa.place(relx=0.02, rely=0.05) # off-set do texto (posicionamento)
        self.entrada_placa = Entry(self.abas_pg0, font = ('Ariel', '15')) 
        self.entrada_placa.place(relx=0.02,rely=0.10)

        self.label_cliente = Label(self.abas_pg0, text = 'Cliente', font = ('Ariel', '15'))# criei o label=escrita
        self.label_cliente.place(relx=0.02, rely=0.15) # off-set do texto (posicionamento)
        self.entrada_placa = Entry(self.abas_pg0, font = ('Ariel', '15')) 
        self.entrada_placa.place(relx=0.02, rely=0.20)

        self.label_ender = Label(self.abas_pg0, text = u'Endereço', font = ('Ariel', '15'))# criei o label=escrita
        self.label_ender.place(relx=0.02, rely=0.25) # off-set do texto (posicionamento)
        self.entrada_ender = Entry(self.abas_pg0, font = ('Ariel', '15')) 
        self.entrada_ender.place(relx=0.02, rely=0.30)

        self.label_cid = Label(self.abas_pg0, text = u'Cidade', font = ('Ariel', '15'))# criei o label=escrita
        self.label_cid.place(relx=0.02, rely=0.35) # off-set do texto (posicionamento)
        self.entrada_cid = Entry(self.abas_pg0, font = ('Ariel', '15')) 
        self.entrada_cid.place(relx=0.02, rely=0.40)

        self.label_cep = Label(self.abas_pg0, text = u'CEP', font = ('Ariel', '15'))# criei o label=escrita
        self.label_cep.place(relx=0.02, rely=0.45) # off-set do texto (posicionamento)
        self.entrada_cep = Entry(self.abas_pg0, font = ('Ariel', '15')) 
        self.entrada_cep.place(relx=0.02, rely=0.50)

        self.label_cpf = Label(self.abas_pg0, text = u'CPF/CNPJ', font = ('Ariel', '15'))# criei o label=escrita
        self.label_cpf.place(relx=0.02, rely=0.55) # off-set do texto (posicionamento)
        self.entrada_cpf = Entry(self.abas_pg0, font = ('Ariel', '15')) 
        self.entrada_cpf.place(relx=0.02, rely=0.60)

        self.label_tel = Label(self.abas_pg0, text = u'Telefone', font = ('Ariel', '15'))# criei o label=escrita
        self.label_tel.place(relx=0.02, rely=0.65) # off-set do texto (posicionamento)
        self.entrada_tel = Entry(self.abas_pg0, font = ('Ariel', '15')) 
        self.entrada_tel.place(relx=0.02, rely=0.70)


        self.label_email = Label(self.abas_pg0, text = u'E-mail', font = ('Ariel', '15'))# criei o label=escrita
        self.label_email.place(relx=0.02, rely=0.75) # off-set do texto (posicionamento)
        self.entrada_email = Entry(self.abas_pg0, font = ('Ariel', '15')) 
        self.entrada_email.place(relx=0.02, rely=0.80)

        self.label_cons = Label(self.abas_pg0, text = u'consulta', font = ('Ariel', '15'))# criei o label=escrita
        self.label_cons.place(relx=0.52, rely=0.08) # off-set do texto (posicionamento)
        self.entrada_cons = Entry(self.abas_pg0, font = ('Ariel', '15')) 
        self.entrada_cons.place(relx=0.52, rely=0.13)



        self.label_com = Label(self.abas_pg0, text = u'Complemento', font = ('Ariel', '15'))# criei o label=escrita
        self.label_com.place(relx=0.52, rely=0.25) # off-set do texto (posicionamento)
        self.entrada_com = Entry(self.abas_pg0, font = ('Ariel', '15')) 
        #self.entrada_com.place(relx=0.52, rely=0.40)
        self.entrada_com.place(relx=0.52,rely=0.30,relheight=0.65,relwidth=0.45)







#========================================Cliente=======================================================
		
                        
root = Tk()
root.title("Manutencao Preventiva Temporal")
root.geometry("1024x768")
main(root)
root.mainloop()