# -*- coding: UTF-8 -*-


from Tkinter import *
import ttk

class main:
    def __init__(self,master):

#-----------------------------------------Cores e Configurações---------------------------------------

        #self.cor_do_fundo = 'blanched almond'#cor do blackground
        #self.cor_do_fundo = '#808000'
        #self.cor_do_fundo = '#D3BC5F'
        
        self.cor_do_entrada = 'PaleTurquoise'
        self.cor_do_fundo = 'LightSteelBlue'  #homem
        
        #self.cor_do_fundo = '#FFD1FF'  #Mulher

    	self.abas = ttk.Notebook(master)
        ttk.Style().configure("TNotebook", background=self.cor_do_fundo)
        #self.abas.configure(width=1024) Ainda não descobri pra que serve isso

#======================================= -:Aba Cleinte:- ========================================        

        self.abas.place(relx = 0.0, rely = 0.0, relheight = 1.0, relwidth = 1.0)
        self.abas.configure(takefocus="")
        self.abas_pg0 = ttk.Frame(self.abas)
        self.abas.add(self.abas_pg0, padding = 3)
        self.abas.tab(0, text = "Cliente cadastro", underline = "-1")
        
#======================================= Aba Serviços ===========================================

        self.abas.configure(takefocus = "")
        self.abas_pg1 = ttk.Frame(self.abas)
        self.abas.add(self.abas_pg1, padding = 3)
        self.abas.tab(1, text = u"Check-List Entrada/Saida", underline = "-1")
        

#========================================== -:Frames:- ===========================================

     
        self.frame_cadastro = Frame(self.abas_pg0, relief = RIDGE, borderwidth = '8', bg = self.cor_do_fundo)
        self.frame_cadastro.place(relx = 0.0, rely = 0.0, relheight = 1.0, relwidth = 0.50)

        self.frame_pequisar = Frame(self.abas_pg0, relief = RIDGE, borderwidth = '8', bg = self.cor_do_fundo)
        self.frame_pequisar.place(relx = 0.50, rely = 0.0, relheight = 1.0, relwidth = 0.50)

        self.frame_renome = Frame(self.abas_pg1, relief = RIDGE, borderwidth = '8', bg = self.cor_do_fundo)
        self.frame_renome.place(relx = 0.0, rely = 0.0, relheight = 1.0, relwidth = 0.50)

        self.frame_renom = Frame(self.abas_pg1, relief = RIDGE, borderwidth = '8', bg = self.cor_do_fundo)
        self.frame_renom.place(relx = 0.50, rely = 0.0, relheight = 1.0, relwidth = 0.50)
        
#========================================= -:fim dos Frames:- =========================================

        self.label_cadas = Label(self.abas_pg0, text = 'CADASTRO', font = ('Ariel', '25'), bg = self.cor_do_fundo)
        self.label_cadas.place(relx = 0.12, rely = 0.03)        
      
        self.label_placa = Label(self.abas_pg0, text = 'Placa', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_placa.place(relx = 0.02, rely = 0.15) 
        self.entrada_placa = Entry(self.abas_pg0, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        self.entrada_placa.place(relx = 0.02,rely = 0.20)

        self.label_cliente = Label(self.abas_pg0, text = 'Cliente', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_cliente.place(relx = 0.02, rely = 0.25) 
        self.entrada_placa = Entry(self.abas_pg0, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        self.entrada_placa.place(relx = 0.02, rely = 0.30)


        self.label_ender = Label(self.abas_pg0, text = u'Endereço', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_ender.place(relx = 0.02, rely = 0.35) 


        
        self.entrada_ender = Entry(self.abas_pg0, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        self.entrada_ender.place(relx = 0.02, rely = 0.40)

        self.label_cid = Label(self.abas_pg0, text = u'Cidade', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_cid.place(relx = 0.02, rely = 0.45) 
        self.entrada_cid = Entry(self.abas_pg0, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        self.entrada_cid.place(relx = 0.02, rely = 0.50)

        self.label_cep = Label(self.abas_pg0, text = u'CEP', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_cep.place(relx = 0.02, rely = 0.55) 
        self.entrada_cep = Entry(self.abas_pg0, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        self.entrada_cep.place(relx = 0.02, rely = 0.60)

        self.label_cpf = Label(self.abas_pg0, text = u'CPF/CNPJ', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_cpf.place(relx = 0.02, rely = 0.65) 
        self.entrada_cpf = Entry(self.abas_pg0, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        self.entrada_cpf.place(relx = 0.02, rely = 0.70)

        self.label_tel = Label(self.abas_pg0, text = u'Telefone', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_tel.place(relx = 0.02, rely = 0.75) 
        self.entrada_tel = Entry(self.abas_pg0, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        self.entrada_tel.place(relx = 0.02, rely = 0.80)


        self.label_email = Label(self.abas_pg0, text = u'E-mail', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_email.place(relx = 0.02, rely = 0.85) 
        self.entrada_email = Entry(self.abas_pg0, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        self.entrada_email.place(relx = 0.02, rely = 0.90)

#====================================== -:Aba Check-List:- ================================== 

        self.label_age = Label(self.abas_pg1, text = 'Agenda entrada',  bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_age.place(relx = 0.02, rely = 0.05 ) 
        self.entrada_age = Entry(self.abas_pg1, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        self.entrada_age.place(relx = 0.09,rely = 0.10, relheight = 0.04, relwidth = 0.1)

        self.label_age = Label(self.abas_pg1, text = u'Previsão',  bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_age.place(relx = 0.23, rely = 0.05 )
        self.entrada_age = Entry(self.abas_pg1, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        self.entrada_age.place(relx = 0.22,rely = 0.10, relheight = 0.042, relwidth = 0.1)

        self.label_age = Label(self.abas_pg1, text = u'saida',  bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_age.place(relx = 0.38, rely = 0.05 )
        self.entrada_age = Entry(self.abas_pg1, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        self.entrada_age.place(relx = 0.37,rely = 0.10, relheight = 0.042, relwidth = 0.1)

        self.label_vmar = Label(self.abas_pg1, text = 'Veiculo Marca', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_vmar.place(relx = 0.04, rely = 0.15) 
        self.entrada_vmar = Entry(self.abas_pg1, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        self.entrada_vmar.place(relx = 0.02, rely = 0.20, relheight = 0.042, relwidth=0.20)

        self.label_model = Label(self.abas_pg1, text = 'Modelo', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_model.place(relx = 0.275, rely = 0.15)
        self.entrada_model = Entry(self.abas_pg1, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        self.entrada_model.place(relx = 0.26,rely = 0.20, relheight = 0.040, relwidth = 0.1)

        self.label_ano = Label(self.abas_pg1, text = 'Ano', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_ano.place(relx = 0.41, rely = 0.15)
        self.entrada_ano = Entry(self.abas_pg1, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        self.entrada_ano.place(relx = 0.408,rely = 0.20,relheight = 0.042,relwidth = 0.06)

        self.label_combust = Label(self.abas_pg1, text = u'Nivel de Combustivel', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_combust.place(relx = 0.02, rely = 0.275) 
        self.entrada_combust = Entry(self.abas_pg1, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        self.entrada_combust.place(relx = 0.02, rely = 0.325, relheight = 0.042, relwidth = 0.20)

        
        self.label_klm = Label(self.abas_pg1, text = u'Kilometragem ', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_klm.place(relx = 0.02, rely = 0.45) 
        self.entrada_klm = Entry(self.abas_pg1, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        self.entrada_klm.place(relx = 0.02,rely = 0.5, relheight = 0.042, relwidth = 0.20)

        self.label_kfer = Label(self.abas_pg1, text = u'Kit de ferramentas', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_kfer.place(relx = 0.02, rely = 0.6) 

        self.label_mac = Label(self.abas_pg1, text = u'Macaco', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_mac.place(relx = 0.02, rely = 0.67)
 
        self.label_ext = Label(self.abas_pg1, text = u'Extintor', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_ext.place(relx = 0.02, rely = 0.74) 
 
        self.label_estep = Label(self.abas_pg1, text = u'Estepe', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_estep.place(relx = 0.02, rely = 0.81) 
         
        self.label_sint = Label(self.abas_pg1, text = u'Sintomas apresentados:', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_sint.place(relx = 0.62, rely = 0.06) 
        self.entrada_sint = Text(self.abas_pg1, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        self.entrada_sint.place(relx = 0.52,rely = 0.10,relheight = 0.2,relwidth = 0.45)

        self.label_diag = Label(self.abas_pg1, text = u'Diagnóstico:', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_diag.place(relx = 0.68, rely = 0.32) 
        self.entrada_diag = Text(self.abas_pg1, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        self.entrada_diag.place(relx = 0.52,rely = 0.38,relheight = 0.2, relwidth = 0.45)

        self.label_diag = Label(self.abas_pg1, text = u'Serviço executado:', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_diag.place(relx = 0.68, rely = 0.6)
        self.entrada_diag = Text(self.abas_pg1, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        self.entrada_diag.place(relx = 0.52,rely = 0.65, relheight = 0.2, relwidth = 0.45)

        
        #========================== -:off-set do place:- =========================================================================

        
        self.label_pesq = Label(self.abas_pg0, text = 'PESQUISAR', bg = self.cor_do_fundo, font = ('Ariel', '25'))
        self.label_pesq.place(relx = 0.65, rely = 0.03) 


        self.label_cons = Label(self.abas_pg0, text = u'consultar', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_cons.place(relx = 0.52, rely = 0.18) 
        self.entrada_cons = Entry(self.abas_pg0, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        self.entrada_cons.place(relx = 0.52, rely = 0.23)


        self.label_com = Label(self.abas_pg0, text = 'Complemento', bg = self.cor_do_fundo, font = ('Ariel', '15'))
        self.label_com.place(relx = 0.52, rely = 0.35) 

        self.entrada_com = Text(self.abas_pg0, bg = self.cor_do_entrada, font = ('Ariel', '15')) 
        
        
        self.entrada_com.place(relx = 0.52,rely = 0.40, relheight = 0.52, relwidth = 0.45) 



        


#==================================================== -:Botoes:- ==========================================================================================


        #Botão Cadastra
        self.botao_cadastra = Button(self.abas_pg0, bg = self.cor_do_fundo, text="Cadastrar", font=('Ariel','15'), fg='green')
        self.botao_cadastra.place(relx = 0.325, rely = 0.3, height = 100, width = 160)

        #Botão Cancelar
        self.botaocancela = Button(self.abas_pg0, bg = self.cor_do_fundo,text = 'Limpar\nCancelar', font = ('Ariel','15'), fg = 'blue')
        self.botaocancela.place(relx = 0.325,rely = 0.64, height = 100, width = 160)

        self.escolha = BooleanVar()
        self.rb1Comb = Radiobutton(self.abas_pg1, text = 'entrada', font = ('Ariel','20'), variable = self.escolha, bg = self.cor_do_fundo, value = True)
        self.rb1Comb.place(relx = 0.312, rely = 0.3)

        self.rb1Comb = Radiobutton(self.abas_pg1, text = '    saída', font = ('Ariel','20'), variable = self.escolha, bg = self.cor_do_fundo, value = True)
        self.rb1Comb.place(relx = 0.312, rely = 0.35)

        self.rb2kilo = Radiobutton(self.abas_pg1, text = 'entrada',font = ('Ariel','20'), variable = self.escolha, bg = self.cor_do_fundo, value = True)
        self.rb2kilo.place(relx = 0.312, rely = 0.475)

        self.rb2kilo = Radiobutton(self.abas_pg1, text = '    saída', font = ('Ariel','20'), variable = self.escolha, bg = self.cor_do_fundo, value = True)
        self.rb2kilo.place(relx = 0.312, rely = 0.525)

        self.rb3kitfer = Radiobutton(self.abas_pg1, text = 'sim',font = ('Ariel','20'), variable = self.escolha, bg = self.cor_do_fundo, value = True)
        self.rb3kitfer.place(relx = 0.25, rely = 0.6)

        self.rb3kitfer = Radiobutton(self.abas_pg1, text = u'não', font = ('Ariel','20'), variable = self.escolha, bg = self.cor_do_fundo, value = True)
        self.rb3kitfer.place(relx = 0.365, rely = 0.6)

        self.rb4mac = Radiobutton(self.abas_pg1, text = 'sim',font = ('Ariel','20'), variable = self.escolha, bg = self.cor_do_fundo, value = True)
        self.rb4mac.place(relx = 0.25, rely = 0.67)

        self.rb4mac = Radiobutton(self.abas_pg1, text = u'não', font = ('Ariel','20'), variable = self.escolha, bg = self.cor_do_fundo, value = True)
        self.rb4mac.place(relx = 0.365, rely = 0.67)

        self.rb5ext = Radiobutton(self.abas_pg1, text = 'sim',font = ('Ariel','20'), variable = self.escolha, bg = self.cor_do_fundo, value = True)
        self.rb5ext.place(relx = 0.25, rely = 0.74)

        self.rb5ext = Radiobutton(self.abas_pg1, text = u'não', font = ('Ariel','20'), variable = self.escolha, bg = self.cor_do_fundo, value = True)
        self.rb5ext.place(relx = 0.365, rely = 0.74)

        self.rb6estep = Radiobutton(self.abas_pg1, text = u'não', font = ('Ariel','20'), variable = self.escolha, bg = self.cor_do_fundo,value = True)
        self.rb6estep.place(relx = 0.365, rely = 0.81)
        self.rb6estep = Radiobutton(self.abas_pg1, text = u'sim', font = ('Ariel','20'), variable = self.escolha, bg = self.cor_do_fundo, value = True)
        self.rb6estep.place(relx = 0.25, rely = 0.81)

        self.botao_cadastra = Button(self.abas_pg1, bg = self.cor_do_fundo, text = "Cadastrar", font = ('Ariel','15'), fg = 'green')
        self.botao_cadastra.place(relx = 0.02, rely = 0.90, height = 60, width = 160)

        self.botaocancela = Button(self.abas_pg1, bg = self.cor_do_fundo, text = 'Limpar\nCancelar', font = ('Ariel','15'), fg = 'blue')
        self.botaocancela.place(relx = 0.314, rely = 0.90, height = 60, width = 160)



                        
                        
root = Tk()
root.title("Manutencao Preventiva Temporal")
root.geometry("1024x768")
main(root)
root.mainloop()
