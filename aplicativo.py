from modulos import *
from funcoes import *

main = Tk()

class Aplicativo(Funcs):
  def __init__(self):
    self.main = main
    self.imagens()
    self.tela()
    self.criarTabelas()
    self.menus()
    main.mainloop()
    
  def tela(self):
    self.main.title("Central de Ferramentaria") 
    self.main.geometry("900x600")
    self.main.resizable(False, False)
    self.imgFundo = PhotoImage(data=base64.b64decode(self.fundo))
    self.imgBtT = PhotoImage(data=base64.b64decode(self.btT))
    self.imgBtF = PhotoImage(data=base64.b64decode(self.btF))
    self.imgBtR = PhotoImage(data=base64.b64decode(self.btR))
    self.lbFundo= Label(main,image=self.imgFundo)
    self.lbFundo.pack()

    self.btTecnico=Button(main, bd=0,image=self.imgBtT,command=self.janelaTecnico)
    self.btTecnico.place(relx=0.068,rely=0.62)

    self.btFerramentas=Button(main, bd=0,image=self.imgBtF,command=self.janelaFerramenta)
    self.btFerramentas.place(relx=0.40,rely=0.62)

    self.btReservas=Button(main, bd=0,image=self.imgBtR,command=self.janelaReserva)
    self.btReservas.place(relx=0.731,rely=0.62)
  
  def menus(self):
    menuBar= Menu(self.main)
    self.main.config(menu=menuBar)
    menu1 = Menu(menuBar)
    menu2 = Menu(menuBar)
    menu3 = Menu(menuBar)
    
    def sairMenu(): self.main.destroy()

    menuBar.add_cascade(label= "Opções", menu=menu1)
    menuBar.add_cascade(label= "Tecnico", menu=menu2)
    menuBar.add_cascade(label= "Ferramenta", menu=menu3)
    
    ####################################Opções############################################
    menu1.add_command(label="Sair", command=sairMenu)
    
    
    ####################################Tecnico###########################################
    menu2.add_command(label="ExportarTecnico", command=self.exportarTecnico)
    
    
    ####################################Ferramenta########################################
    menu3.add_command(label="ExportarFerramenta", command=self.exportarFerramentas)
  
  
  
  def janelaTecnico(self):
    self.tecnico = tk.Toplevel()
    self.tecnico.title("Tecnicos") 
    self.tecnico.configure(background="#1C1C1C")
    self.tecnico.geometry("900x600")
    self.tecnico.resizable(False, False)
    self.tecnico.transient(self.main)
    self.tecnico.focus_force()
    self.tecnico.grab_set()
    self.tecnicoFrames()
    self.selecionarListaT()
    
  def janelaFerramenta(self):
    self.ferramenta = tk.Toplevel()
    self.ferramenta.title("Ferramentas")
    self.ferramenta.configure(background="#1C1C1C")
    self.ferramenta.geometry("900x600")
    self.ferramenta.resizable(False, False)
    self.ferramenta.transient(self.main)
    self.ferramenta.focus_force()
    self.ferramenta.grab_set()
    self.ferramentaFrames()
    self.selecionarListaF()
  
  def janelaReserva(self):
    self.reserva = tk.Toplevel()
    self.reserva.title("Reserva") 
    self.reserva.configure(background="#1C1C1C")
    self.reserva.geometry("900x600")
    self.reserva.resizable(False, False)
    self.reserva.transient(self.main)
    self.reserva.grab_set()
    self.imgReserva = PhotoImage(data=base64.b64decode(self.imgR))
    self.lbReserva= Label(self.reserva, image=self.imgReserva)
    self.lbReserva.pack()
    msg.showerror("Página Indisponível", "Página Indisponível")
  
  def ferramentaFrames(self):
    self.frame3 = atk.Frame3d(self.ferramenta, bg= '#dfe3ee')
    self.frame3.place(relx= 0.01, rely=0.02, relwidth=0.98, relheight=0.56)
        
    self.frame4 = atk.Frame3d(self.ferramenta, bg= '#dfe3ee')
    self.frame4.place(relx= 0.01, rely=0.6, relwidth=0.98, relheight=0.36)  
    
    self.ferramentaFrame3()
    self.ferramentaFrame4()
      
  def tecnicoFrames(self):
    self.frame1 = atk.Frame3d(self.tecnico, bg= '#dfe3ee')
    self.frame1.place(relx= 0.01, rely=0.02, relwidth=0.98, relheight=0.56)
      
    self.frame2 = atk.Frame3d(self.tecnico, bg= '#dfe3ee')
    self.frame2.place(relx= 0.01, rely=0.6, relwidth=0.98, relheight=0.36)
    
    self.tecnicoFrame1()
    self.tecnicoFrame2()
  
  def tecnicoFrame1(self):
    self.listaTecnico = ttk.Treeview(self.frame1, height=10, columns=("col0","col1","col2","col3","col4","col5","col6"))
    self.listaTecnico.heading("#0")
    self.listaTecnico.heading("#1", text="Nome")
    self.listaTecnico.heading("#2", text="Email")
    self.listaTecnico.heading("#3", text="Cpf")
    self.listaTecnico.heading("#4", text="Telefone")
    self.listaTecnico.heading("#5", text="Turno")
    self.listaTecnico.heading("#6", text="Equipe")
    
    self.listaTecnico.column("#0", width=0  )
    self.listaTecnico.column("#1", width=135)
    self.listaTecnico.column("#2", width=135)
    self.listaTecnico.column("#3", width=135)
    self.listaTecnico.column("#4", width=135)
    self.listaTecnico.column("#5", width=135)
    self.listaTecnico.column("#6", width=135)
    
    self.listaTecnico.place(relx=0.01, rely=0.02, relwidth=0.94, relheight=0.94)
    
    self.barraRolagem = Scrollbar(self.frame1, orient="vertical")
    self.listaTecnico.configure(yscroll=self.barraRolagem.set)
    self.barraRolagem.place(relx=0.956, rely=0.02, relwidth=0.03, relheight=0.94)
    
    self.listaTecnico.bind("<Button-1>", self.clickTecnico)
      
  def tecnicoFrame2(self):
    #########################################Botao########################################
    self.btBuscar = atk.Button3d(self.frame2, text="Buscar", command = self.buscaTecnico)
    self.btBuscar.place(relx=0.001, rely=0.8, relwidth=0.2,relheight=0.2)
      
    self.btlimpaTela = atk.Button3d(self.frame2, text="Limpar", command = self.limpaTecnico)
    self.btlimpaTela.place(relx=0.2, rely=0.8, relwidth=0.2,relheight=0.2)
      
    self.btCadastrar = atk.Button3d(self.frame2, text="Cadastrar", command = self.cadastrarTecnico)
    self.btCadastrar.place(relx=0.4, rely=0.8, relwidth=0.2,relheight=0.2)
      
    self.btDeletar = atk.Button3d(self.frame2, text="Deletar", command = self.deletarTecnico)
    self.btDeletar.place(relx=0.6, rely=0.8, relwidth=0.2,relheight=0.2)
    
    self.btModificar = atk.Button3d(self.frame2, text="Modificar", command = self.modificarTecnico)
    self.btModificar.place(relx=0.8, rely=0.8, relwidth=0.2,relheight=0.2)
    
    ########################################Label#########################################
    
    self.lbNome = Label(self.frame2, text= "Nome", background="#dfe3ee", foreground="#1C1C1C", font="1")
    self.lbNome.place(relx=0.02 ,rely=0.1)
    
    self.lbEmail = Label(self.frame2, text= "E-Mail", background="#dfe3ee", foreground="#1C1C1C", font="1")
    self.lbEmail.place(relx=0.02 ,rely=0.3)
    
    self.lbCpf = Label(self.frame2, text= "Cpf", background="#dfe3ee", foreground="#1C1C1C", font="1")
    self.lbCpf.place(relx=0.02 ,rely=0.5)
    
    self.lbTelefone = Label(self.frame2, text= "Telefone", background="#dfe3ee", foreground="#1C1C1C", font="1")
    self.lbTelefone.place(relx=0.5 ,rely=0.1)
    
    self.lbTurno = Label(self.frame2, text= "Turno", background="#dfe3ee", foreground="#1C1C1C", font="1")
    self.lbTurno.place(relx=0.5 ,rely=0.3)
    
    self.lbEquipe = Label(self.frame2, text= "Equipe", background="#dfe3ee", foreground="#1C1C1C", font="1")
    self.lbEquipe.place(relx=0.5 ,rely=0.5)
    
    ########################################Entry#########################################
    
    turno = ["Manhã","Tarde","Noite"]
    
    self.entryNome = Entry(self.frame2)
    self.entryNome.place(relx=0.12,rely=0.1, relwidth=0.32)
    
    self.entryEmail = Entry(self.frame2)
    self.entryEmail.place(relx=0.12,rely=0.3, relwidth=0.32)
    
    self.entryCpf = Entry(self.frame2)
    self.entryCpf.place(relx=0.12,rely=0.5, relwidth=0.32)
    
    self.entryTelefone = Entry(self.frame2)
    self.entryTelefone.place(relx=0.6,rely=0.1, relwidth=0.37)
    
    self.entryTurno = ttk.Combobox(self.frame2,values=turno)
    self.entryTurno.place(relx=0.6,rely=0.3, relwidth=0.37)
    
    self.entryEquipe = Entry(self.frame2)
    self.entryEquipe.place(relx=0.6,rely=0.5, relwidth=0.37)

#################################Ferramentas##############################################
    
  def ferramentaFrame3(self):
    self.listaFerramenta = ttk.Treeview(self.frame3, height=10, columns=("col0","col1",
      "col2","col3","col4","col5","col6", "col7","col8","col9","col10"))
    self.listaFerramenta.heading("#0")
    self.listaFerramenta.heading("#1", text="IdFerramenta")
    self.listaFerramenta.heading("#2", text="Descricao")
    self.listaFerramenta.heading("#3", text="Fabricante")
    self.listaFerramenta.heading("#4", text="Voltagem")
    self.listaFerramenta.heading("#5", text="PartNumber")
    self.listaFerramenta.heading("#6", text="Tamanho")
    self.listaFerramenta.heading("#7", text="Medida")
    self.listaFerramenta.heading("#8", text="Tipo")
    self.listaFerramenta.heading("#9", text="Material")
    self.listaFerramenta.heading("#10", text="ReservaMax")

    self.listaFerramenta.column("#0", width=0  )
    self.listaFerramenta.column("#1", width=80)
    self.listaFerramenta.column("#2", width=80)
    self.listaFerramenta.column("#3", width=80)
    self.listaFerramenta.column("#4", width=80)
    self.listaFerramenta.column("#5", width=80)
    self.listaFerramenta.column("#6", width=80)
    self.listaFerramenta.column("#7", width=80)
    self.listaFerramenta.column("#8", width=80)
    self.listaFerramenta.column("#9", width=80)
    self.listaFerramenta.column("#10", width=80)
    
    
    self.listaFerramenta.place(relx=0.01, rely=0.02, relwidth=0.94, relheight=0.94)
    
    self.barraRolagem = Scrollbar(self.frame3, orient="vertical")
    self.listaFerramenta.configure(yscroll=self.barraRolagem.set)
    self.barraRolagem.place(relx=0.956, rely=0.02, relwidth=0.03, relheight=0.94)
    
    self.listaFerramenta.bind("<Button-1>", self.clickFerramenta)
      
  def ferramentaFrame4(self):
    #########################################Botao########################################
    self.btBuscar = atk.Button3d(self.frame4, text="Buscar", command = self.buscaFerramenta)
    self.btBuscar.place(relx=0.001, rely=0.8, relwidth=0.2,relheight=0.2)
      
    self.btlimpaTela = atk.Button3d(self.frame4, text="Limpar", command=self.limpaFerramenta)
    self.btlimpaTela.place(relx=0.2, rely=0.8, relwidth=0.2,relheight=0.2)
      
    self.btCadastrar = atk.Button3d(self.frame4, text="Cadastrar", command=self.cadastrarFerramenta)
    self.btCadastrar.place(relx=0.4, rely=0.8, relwidth=0.2,relheight=0.2)
      
    self.btDeletar = atk.Button3d(self.frame4, text="Deletar", command=self.deletarFerramenta)
    self.btDeletar.place(relx=0.6, rely=0.8, relwidth=0.2,relheight=0.2)
    
    self.btModificar = atk.Button3d(self.frame4, text="Modificar", command=self.modificarFerramenta)
    self.btModificar.place(relx=0.8, rely=0.8, relwidth=0.2,relheight=0.2)
    
    ########################################Label#########################################
    
    self.lbDescricao = Label(self.frame4, text= "Descricao", background="#dfe3ee", foreground="#1C1C1C", font="1")
    self.lbDescricao.place(relx=0.02 ,rely=0.1)
    
    self.lbFabricante = Label(self.frame4, text= "Fabricante", background="#dfe3ee", foreground="#1C1C1C", font="1")
    self.lbFabricante.place(relx=0.02 ,rely=0.3)
    
    self.lbVoltagem = Label(self.frame4, text= "Voltagem", background="#dfe3ee", foreground="#1C1C1C", font="1")
    self.lbVoltagem.place(relx=0.02 ,rely=0.5)
    
    self.lbPartNumber = Label(self.frame4, text= "PartNumber", background="#dfe3ee", foreground="#1C1C1C", font="1")
    self.lbPartNumber.place(relx=0.3 ,rely=0.1)
    
    self.lbTamanho = Label(self.frame4, text= "Tamanho", background="#dfe3ee", foreground="#1C1C1C", font="1")
    self.lbTamanho.place(relx=0.3 ,rely=0.3)

    self.lbMedida = Label(self.frame4, text= "Medida", background="#dfe3ee", foreground="#1C1C1C", font="1")
    self.lbMedida.place(relx=0.3 ,rely=0.5) 

    self.lbTipo = Label(self.frame4, text= "Tipo", background="#dfe3ee", foreground="#1C1C1C", font="1")
    self.lbTipo.place(relx=0.6 ,rely=0.1)

    self.lbMaterial = Label(self.frame4, text= "Material", background="#dfe3ee", foreground="#1C1C1C", font="1")
    self.lbMaterial.place(relx=0.6 ,rely=0.3)

    self.lbReservaMax = Label(self.frame4, text= "ReservaMax", background="#dfe3ee", foreground="#1C1C1C", font="1")
    self.lbReservaMax.place(relx=0.6 ,rely=0.5)
    
    ########################################Entry#########################################

    voltagem = ["50v","127v","110v","220v","110v,220v","Outros"]
    medida = ["mm","cm","Polegadas","Metros","Outros"]
    tipo = ["Elétrica","Mecânica","Segurança","Outros"]
    material = ["Ferro", "Madeira", "Borracha", "Plástico", "Outros"]

    self.entryIdFerramenta = Entry(self.frame4)
     
    self.entryDescricao = Entry(self.frame4)
    self.entryDescricao.place(relx=0.12,rely=0.1, relwidth=0.17)
    
    self.entryFabricante = Entry(self.frame4)
    self.entryFabricante.place(relx=0.12,rely=0.3, relwidth=0.17)
    
    self.entryVoltagem = ttk.Combobox(self.frame4,values=voltagem)
    self.entryVoltagem.place(relx=0.12,rely=0.5, relwidth=0.17)
    
    self.entryPartNumber = Entry(self.frame4)
    self.entryPartNumber.place(relx=0.42,rely=0.1, relwidth=0.17)
    
    self.entryTamanho = Entry(self.frame4)
    self.entryTamanho.place(relx=0.42,rely=0.3, relwidth=0.17)

    self.entryMedida = ttk.Combobox(self.frame4,values=medida)
    self.entryMedida.place(relx=0.42,rely=0.5, relwidth=0.17)

    self.entryTipo = ttk.Combobox(self.frame4,values=tipo)
    self.entryTipo.place(relx=0.75,rely=0.1, relwidth=0.17)

    self.entryMaterial = ttk.Combobox(self.frame4,values=material)
    self.entryMaterial.place(relx=0.75,rely=0.3, relwidth=0.17)

    self.entryReservaMax = Entry(self.frame4)
    self.entryReservaMax.place(relx=0.75,rely=0.5, relwidth=0.17)
    


    
Aplicativo()