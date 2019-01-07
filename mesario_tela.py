from tkinter import *
import tkinter as tk
from tkinter import messagebox
from metodos import *

class MyApp(Frame,Metodos):
    def __init__(self, master=None):
        Metodos.__init__(self)
        Frame.__init__(self, master)

        #CONTAINER TITULO
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["padx"] = 20
        self.primeiroContainer["pady"] = 80
        self.primeiroContainer.pack()
        self.titulo = Label(self.primeiroContainer, text="Acesso do Mesário")
        self.titulo["font"] = ("Times New Roman Baltic", "26", "bold")
        self.titulo.pack()
        self.fontePadrao = ("Times New Roman", "15")

        #CONTAINER PRA COLOCAR O LOGIN
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 50
        self.segundoContainer["pady"] = 10
        self.segundoContainer.pack()
        self.nomeLabel = Label(self.segundoContainer,
        text="Login", font=self.fontePadrao)
        self.nomeLabel["padx"]=30
        self.nomeLabel.pack(side=LEFT)
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        #CONTAINER PRA COLOCAR SENHA
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer["pady"] = 10
        self.terceiroContainer.pack()
        self.senhaLabel = Label(self.terceiroContainer,
        text="Senha", font=self.fontePadrao)
        self.senhaLabel["padx"]=30
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        #CONTAINER BOTÃO DE ENTRAR
        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 80
        self.quartoContainer["pady"] = 60
        self.quartoContainer.pack()
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Entrar"
        self.autenticar["font"] = ("Verdana", "13")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verifica_senha
        self.autenticar.pack(side=LEFT)

        
    def janelaProsseguir(self):
        self.prosseguir = Toplevel()
        self.prosseguir.geometry("%dx%d+0+0" % (w-16, h))
        self.prosseguir.title('Prosseguir')
        self.prosseguir.focus_force()#Quando abrir foco nela
        self.prosseguir.resizable(width=False, height=False)

        

        #CONTAINER COM A PERGUNTA
        self.primeiroContainer = Frame(self.prosseguir)
        self.primeiroContainer["padx"] = 20
        self.primeiroContainer["pady"] = 80
        self.primeiroContainer.pack()
        self.titulo = Label(self.primeiroContainer, text="O que deseja fazer?")
        self.titulo["font"] = ("Times New Roman Baltic", "26", "bold")
        self.titulo.pack()

        #CONTAINER COM DOIS BOTOES
        self.segundoContainer = Frame(self.prosseguir)
        self.segundoContainer.pack()
        self.bt = Button(self.segundoContainer)
        self.bt["text"] = "Votar"
        self.bt["font"] = ("Verdana", "13")
        self.bt["width"] = 20
        self.bt["command"] = self.dadosJanela
        self.bt.pack(side=LEFT)
        self.bt2 = Button(self.segundoContainer)
        self.bt2["text"] = "Encerrar Eleição"
        self.bt2["font"] = ("Verdana", "13")
        self.bt2["width"] = 20
        self.bt2["command"] = self.encerrar
        self.bt2.pack()
        self.prosseguir.deiconify()

        self.terceiroContainer = Frame(self.prosseguir)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer["pady"] = 50
        self.terceiroContainer.pack()
        self.bt = Button(self.terceiroContainer)
        self.bt["text"] = "Sair"
        self.bt["font"] = ("Verdana", "13")
        self.bt["width"] = 20
        self.bt["command"] = self.sair
        self.bt.pack()
        

    def dadosJanela(self):
        self.prosseguir.withdraw()
        self.janelaDados= Toplevel()        

        self.janelaDados.update()
        self.janelaDados.geometry("%dx%d+0+0" % (w-16, h))
        self.janelaDados.title('Confirmação de Dados')
        self.janelaDados.resizable(width=False, height=False)
        self.janelaDados.focus_force()

        self.primeiroContainer = Frame(self.janelaDados)
        self.primeiroContainer["padx"] = 20
        self.primeiroContainer["pady"] = 80
        self.primeiroContainer.pack()
        self.nomeLabel = Label(self.primeiroContainer,
        text="Confirmação", font=("Times New Roman Baltic", "27", "bold"))
        self.nomeLabel["padx"]=30
        self.nomeLabel.pack(side=LEFT)

        self.segundoContainer = Frame(self.janelaDados)
        self.segundoContainer["padx"] = 60
        self.segundoContainer["pady"] = 60
        self.segundoContainer.pack()
        self.cpfLabel = Label(self.segundoContainer,
        text="CPF: ", font=self.fontePadrao)
        self.cpfLabel["padx"]=30
        self.cpfLabel.pack(side=LEFT)
        self.cpf = Entry(self.segundoContainer)
        self.cpf["width"] = 30
        self.cpf["font"] = ("Arial", "13")
        self.cpf.focus()
        self.cpf.pack(side=LEFT)

        self.terceiroContainer = Frame(self.janelaDados)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer["pady"] = 20
        self.terceiroContainer.pack()
        self.bt = Button(self.terceiroContainer)
        self.bt["text"] = "Validar"
        self.bt["font"] = ("Verdana", "13")
        self.bt["width"] = 20
        self.bt["command"] = self.validar
        self.bt.pack()

        self.quartoContainer = Frame(self.janelaDados)
        self.quartoContainer["padx"] = 20
        self.quartoContainer["pady"] = 0
        self.quartoContainer.pack()
        self.bt3 = Button(self.quartoContainer)
        self.bt3["text"] = "Voltar"
        self.bt3["font"] = ("Verdana", "13")
        self.bt3["width"] = 20
        self.bt3["command"] = self.voltar
        self.bt3.pack()

    def votoJanela(self):
        global w,h, caminho
        self.janela_voto = Toplevel()
        #self.janela_voto.geometry("600x500+1500+50")#########
        self.janela_voto.geometry("1275x985+%d+0" % (w))
        #self.janela_voto.geometry("%dx%d+%d+0" % (w, h, w))
        mixer.init()
        self.janela_voto.title("Voto")
        self.janela_voto.grab_set()
        self.janela_voto.transient()
        #self.janela_voto.attributes('-fullscreen',True)
        self.janela_voto.resizable(width=False, height=False)

        var = tk.StringVar()
        max_len = 2

        vcmd = (self.master.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.janela_voto.bind("<Return>", self.key1)
        self.janela_voto.bind("<,>", self.key2)
        #self.janela_voto.bind("<*>", self.key3)

        Numero  = tk.StringVar()
        Nome    = tk.StringVar()
        Partido = tk.StringVar()
        caminho = "padrao.png"
        Numero.set("?")
        Nome.set("?")
        Partido.set("?")

        self.imagem = PhotoImage(file = caminho)
        
        #CONTAINER FOTO DO CANDIDATO
        self.container1 = Frame(self.janela_voto)
        self.container1["width"] = 200
        self.container1.pack()
        self.foto = Label(self.container1, image=self.imagem)
        self.foto.imagem = self.imagem
        self.foto.imagem["width"] = 200
        self.foto.imagem["height"] = 200
        self.foto.pack()


        
    
        #CONTAINER INFORMAÇÃO DO CANDIDATO
        self.container2 = Frame(self.janela_voto)
        self.container2["pady"] = 20
        self.container2.pack()
        self.lb1 = Label(self.container2)
        self.lb1["text"] = "SEU VOTO PARA GOVERNADOR"
        self.lb1["font"] = ("Verdana", "30")
        self.lb1.pack()

        self.container3 = Frame(self.janela_voto)
        self.container3["pady"] = 15
        self.container3.pack()
        self.lb2 = Label(self.container3)
        self.lb2["text"] = "Número:"
        self.lb2["font"] = ("Verdana", "20")
        self.lb2.pack(side=LEFT)
        self.lb3 = Label(self.container3, textvariable = Numero)
        self.lb3["font"] = ("Verdana", "20")
        self.lb3.pack(side=BOTTOM)

        self.container4 = Frame(self.janela_voto)
        self.container4["pady"] = 15
        self.container4.pack()
        self.lb4 = Label(self.container4)
        self.lb4["text"] = "Nome:"
        self.lb4["font"] = ("Verdana", "20")
        self.lb4.pack(side=LEFT)
        self.lb5 = Label(self.container4, textvariable = Nome)
        self.lb5["font"] = ("Verdana", "20")
        self.lb5.pack(side = BOTTOM)

        self.container5 = Frame(self.janela_voto)
        self.container5["pady"] = 15
        self.container5.pack()
        self.lb6 = Label(self.container5)
        self.lb6["text"] = "Partido:"
        self.lb6["font"] = ("Verdana", "20")
        self.lb6.pack(side=LEFT)
        self.lb7 = Label(self.container5, textvariable = Partido)
        self.lb7["font"] = ("Verdana", "20")
        self.lb7.pack(side = BOTTOM)

        #CONTAINER ENTRY DO NUMERO DE VOTO
        self.container6 = Frame(self.janela_voto)
        self.container6["pady"] = 25
        self.container6.pack()
        self.et1 = Entry(self.container6, validate = 'key', validatecommand = vcmd, textvariable = var)
        self.et1["width"] = 5
        self.et1["font"] = ("Verdana", "28")
        self.et1["justify"] = "center"
        self.et1.focus()
        self.et1.pack()

        #CONTAINER CONFIRMA E BRANCO
        self.container4 = Frame(self.janela_voto)
        self.container4["width"] = 25
        self.container4.pack()
        self.lb8 = Label(self.container4)
        self.lb8["text"] = "Aperte Enter duas vezes para votar"
        self.lb8["font"] = ("Verdana", "11")
        self.lb8.pack()
        
            
                  
        def on_write(self, *args):
            global cont
            global cont1
            s = var.get()
            cont1 = 0
            if len(s) > max_len:
                var.set(s[:max_len])
            
            elif len(s) == 0 or len(s) > 0:
                global cont
                global cpfRelativo
                global caminho
                global app
                num = s
                        
                if s == '':
                    Numero.set("?")
                    Nome.set("?")
                    Partido.set("?")
                    app.imagem["file"]="padrao.png"
                    cont=num

                elif len(s)==1:
                    Numero.set("?")
                    Nome.set("?")
                    Partido.set("?")
                    app.imagem["file"]="padrao.png"
                    cont=num

                elif s == '00':
                    Numero.set("Branco")
                    Nome.set("Branco")
                    Partido.set("Branco")
                    caminho="candidatos/" + num + "/" + num + ".png"           
                    cont = num
                    
                            
                elif len(s)==2:
                    arq = "candidatos/" + num + "/info.txt"
                    try:
                        abre = open(arq, "r")
                        linhas = abre.readlines()
                    except IOError:
                        Numero.set("Nulo")
                        Nome.set("Nulo")
                        Partido.set("Nulo")
                        app.imagem["file"]="padrao.png"
                        cont=num
                            

                    except Exception as erro:

                        messagebox.showerror("Erro Inesperado", erro)

                    else:
                        Numero.set(linhas[0].strip("\n"))
                        Nome.set(linhas[1].strip("\n"))
                        Partido.set(linhas[2].strip("\n"))
                        caminho="candidatos/" + num + "/" + num + ".png"
                        app.imagem["file"]="candidatos/" + num + "/" + num + ".png"
                        #self.imagem = self.imagem.zoom(20)
                        #self.imagem = self.imagem.subsample(50)
                        abre.close()
                        cont = s
                
                    
            
                

        var.trace_variable("w",on_write)

    def telafim(self):
        self.fim = Toplevel()
        self.fim.geometry("1275x985+%d+0" % (w))
        self.fim.title("Fim")
        self.fim.grab_set()
        self.fim.transient()
        self.fim.resizable(width=False, height=False)

        self.container1 = Frame(self.fim)
        self.container1["pady"] = 300
        self.container1.pack()
        self.lb1 = Label(self.container1)
        self.lb1["text"] = "FIM!"
        self.lb1["font"] = ("Verdana", "80")
        self.lb1.pack()

        self.lb2 = Label(self.container1)
        self.lb2["text"] = "\n\n\n\n\n\n\n\nDesenvolvido por:\nAderson Januario\nPedro Vicente\nAlessandra Medeiros"
        self.lb2["font"] = ("Verdana", "12")
        self.lb2.pack()

        

        
        

        

app = MyApp()
app.master.title("Tela de Login do Mesário")
w, h = app.master.winfo_screenwidth(), app.master.winfo_screenheight()
app.master.geometry("%dx%d+0+0" % (w-16, h))
mainloop()


#self.jan.transient(root)#Sempre aberta
#self.jan.focus_force()#Quando abrir foco nela
#self.jan.grab_set()#Não usar botoes da outra
#messagebox.showinfo("Informação", "Dados do "+ Clube +":" +"\n\nNome do clube: "+ Lista[0]+"\nAno de fundação: "+Lista[1]+"\nSérie Atual: Série "+Lista[2]+"\nQuantidade de títulos: "+Lista[3])
#messagebox.showerror("Erro", "Um erro foi encontrado!\nO clube "+Clube+" não foi encontrado!")

