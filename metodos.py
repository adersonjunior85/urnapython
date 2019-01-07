from tkinter import *
from pygame import mixer
from reportlab.pdfgen import canvas
import pyautogui
import sys
import time



class Metodos():
    def __init__(self):
        pass

    def verifica_senha(self):
        Login = self.nome.get()
        Senha = self.senha.get()
        try:
            if Login == '' and Senha == '':
                messagebox.showinfo("Informação", "O seu usuário foi validado com sucesso!")
                self.master.withdraw()
                self.janelaProsseguir()
            else:
                messagebox.showerror("Erro", "Um erro foi encontrado!\nSeu usuário não foi encontrado!")
        finally:
            self.nome.delete(0,'end')
            self.senha.delete(0,'end')


    def validar(self):
        CPF = self.cpf.get()
        if len(CPF)!= 11:
            messagebox.showerror("Erro", "Tente digitar de acordo com o exemplo!")
            self.cpf.delete(0,'end')
        else:
            CPF = CPF[:3]+'.'+CPF[3:6]+'.'+CPF[6:9]+'-'+CPF[9:11]
            Banco = "votos/alunoVoto.txt"
            try:
                Abrir = open(Banco, "r")
                linha = Abrir.readlines()
                global cpfRelativo
                for a in linha:
                    separar = a.split("|")
                    if separar[0] == CPF and separar[1].strip('\n') == 'F':
                        messagebox.showinfo("Validado", "O CPF foi validado com sucesso!")
                        cpfRelativo = CPF
                        pyautogui.press('numlock')
                        self.votoJanela()
                        break
                        #self..withdraw()
                        #self.prosseguir()
                    elif separar[0] == CPF and separar[1].strip('\n') == 'V':
                        messagebox.showwarning("Alerta", "O CPF indicado já registrou voto!")
                        break
                else:
                    Banco = "votos/alunoVoto1.txt"
                    try:
                        Abrir = open(Banco, "r")
                        linha = Abrir.readlines()
                        for a in linha:
                            separar = a.split("|")
                            if separar[0] == CPF and separar[1].strip('\n') == 'F':
                                messagebox.showinfo("Validado", "O CPF foi validado com sucesso!")
                                cpfRelativo = CPF
                                pyautogui.press('numlock')
                                self.votoJanela()
                                break
                            elif separar[0] == CPF and separar[1].strip('\n') == 'V':
                                messagebox.showwarning("Alerta", "O CPF indicado já registrou voto!")
                                break
                        else:
                            messagebox.showerror("Erro", "O CPF não foi encontrado!")
                    finally:
                        pass
                        
            finally:
                self.cpf.delete(0,'end')
    

    def encerrar(self):
        global NomePdf
        global j
        branco = 0
        naovotou = 0
        ########
        partido = ["PDF", "PEDF", "PEDT", "PJL"]
        candidatos = [0,0,0,0]
        ########
        j += 1
        NomePdf = NomePdf + str(j)
        try:
            Banco = "votos/alunoVoto.txt"
            Abrir = open(Banco, "r")
            linha = Abrir.readlines()
            pdf = canvas.Canvas('{}.pdf'.format(NomePdf))
            for v in linha:
                separar = v.strip("\n")
                separar = separar.split("|")
                
                if separar[1] == "V":
                    voto = separar[2]
                    if voto == "01":
                        candidatos[0]+=1
                    elif voto == "07":
                        candidatos[1]+=1
                    elif voto == "42":
                        candidatos[2]+=1
                    elif voto == "99":
                        candidatos[3]+=1
                    else:
                        branco += 1
                else:
                    naovotou += 1
            else:
                try:
                    Banco = "votos/alunoVoto1.txt"
                    Abrir = open(Banco, "r")
                    linha = Abrir.readlines()
                    for v in linha:
                        separar = v.strip("\n")
                        separar = separar.split("|")
                        if separar[1] == "V":
                            voto = separar[2]
                            if voto == "01":
                                candidatos[0]+=1
                            elif voto == "07":
                                candidatos[1]+=1
                            elif voto == "42":
                                candidatos[2]+=1
                            elif voto == "99":
                                candidatos[3]+=1
                            else:
                                branco += 1
                        else:
                            naovotou += 1
                    
                except:
                    print("Error")

                finally:
                    Abrir.close()
                        
                    
        except:
            print('Erro ao gerar {}.pdf'.format(NomePdf))

        finally:
            pass
            
        self.prosseguir.destroy()
        x = 680
        n = 0
        for a in candidatos:
            x -= 20
            pdf.drawString(247,x, ("Partido "+str(partido[n])+": "+str(a)))
            n+=1
        pdf.drawString(247,680, "Não votaram: "+str(naovotou))
        pdf.drawString(247,700, "Branco ou nulo: "+str(branco))
        pdf.setTitle(NomePdf)
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(245,750, 'Dado da Eleição')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(245,724, 'Extraido do Banco de Dados')
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(NomePdf))
        

   
    def sair(self):
        self.prosseguir.withdraw()
        self.master.deiconify()
        
    def fechar(self):
        self.fim.destroy()

    def voltar(self):
        self.prosseguir.deiconify()
        self.janelaDados.withdraw()

    def pesqCandidato(self):
        global cont
        global cpfRelativo
        num = self.et1.get()
        
        if num == '':
            messagebox.showerror("Campo vazio!", 'Candidato não informado!')

        elif cont == num or num == '00':
            Banco = "votos/alunoVoto.txt"
            escrever = ''
            try:
                Abrir = open(Banco, "r")
                linhas = Abrir.readlines()
                for x in linhas:
                    separador = x.split('|')
                    if separador[0] == cpfRelativo:
                        separador[1] = '|V' 
                        separador.append('|' + self.et1.get()+'\n')
                        x = separador[0]+separador[1]+separador[2]
                    escrever += x
                
                    
                Abrir2 = open(Banco, "w")
                Abrir2.writelines(escrever)
                        
                        
                
            except IOError:
                pass
            
            except Exception as erro:
                messagebox.showerror("Erro Inesperado", erro)

            else:
                messagebox.showinfo("Sucesso", "Voto efetuado com sucesso!")
                cont = ''
                self.janela_voto.destroy()
                self.janelaDados.destroy()
                self.prosseguir.deiconify()
            
        elif cont != num and num != '00' and num != '':
            arq = "candidatos/" + num + "/info.txt"
            try:
                abre = open(arq, "r")
                linhas = abre.readlines()
            except IOError:
                messagebox.showerror("Erro", "Candidato não identificado!\n Porfavor digite um número válido.")
                self.et1.delete(0, 'end')

            except Exception as erro:
                messagebox.showerror("Erro Inesperado", erro)

            else:
                self.lb3["text"] = linhas[0].strip("\n")
                self.lb5["text"] = linhas[1].strip("\n")
                self.lb7["text"] = linhas[2].strip("\n")
                self.imagem["file"] = "candidatos/" + num + "/" + num + ".png"
                #self.imagem = self.imagem.zoom(20)
                #self.imagem = self.imagem.subsample(50)
                abre.close()
                cont = self.et1.get()

    def key1(self, event):
        global cont1
        global cpfRelativo
        num = self.et1.get()
        cont1 = cont1+1
        
        if cont1 == 2:    
            if num == '':
                messagebox.showerror("Campo vazio!", 'Candidato não informado!')

            elif cont1 == num or num == '00' or len(num) == 2:
                mixer.music.load('fim.mp3')
                mixer.music.play()
                try:
                    Banco = "votos/alunoVoto.txt"
                    escrever = ''
                    Abrir = open(Banco, "r")
                    linhas = Abrir.readlines()
                    for x in linhas:
                        separador = x.split('|')
                        if separador[0] == cpfRelativo:
                            separador[1] = '|V' 
                            separador.append('|' + self.et1.get()+'\n')
                            x = separador[0]+separador[1]+separador[2]
                        escrever += x    
                    Abrir2 = open(Banco, "w")
                    Abrir2.writelines(escrever)
                    Abrir2.close()
                            
                    
                except IOError:
                    messagebox.showerror("Erro Inesperado", erro)
                
                except Exception as erro:
                    messagebox.showerror("Erro Inesperado", erro)

                else:
                    try:
                        Banco = "votos/alunoVoto1.txt"
                        escrever = ''
                        Abrir = open(Banco, "r")
                        linhas = Abrir.readlines()
                        for x in linhas:
                            separador = x.split('|')
                            if separador[0] == cpfRelativo:
                                separador[1] = '|V' 
                                separador.append('|' + self.et1.get()+'\n')
                                x = separador[0]+separador[1]+separador[2]
                            escrever += x    
                        Abrir2 = open(Banco, "w")
                        Abrir2.writelines(escrever)
                        Abrir2.close()
                                
                        
                    except IOError:
                        messagebox.showerror("Erro Inesperado", erro)
                    
                    except Exception as erro:
                        messagebox.showerror("Erro Inesperado", erro)

                    else:
                        cont1 = 0
                        pyautogui.press('numlock')
                        self.telafim()
                        self.janela_voto.destroy()
                        self.janelaDados.destroy()
                        self.prosseguir.deiconify()
                        self.prosseguir.after(4000, self.fechar)

                        messagebox.showinfo("Sucesso", "Voto efetuado com sucesso!")
            cont1 = 0
        
    
    def key2(self, event):
        self.et1.delete(0, 'end')

    def key3(self, event):
        Banco = "votos/alunoVoto.txt"
        escrever = ''
        try:
            Abrir = open(Banco, "r")
            linhas = Abrir.readlines()
            for x in linhas:
                separador = x.split('|')
                if separador[0] == cpfRelativo:
                    separador[1] = '|V' 
                    separador.append('|' + '00' + '\n')
                    x = separador[0]+separador[1]+separador[2]
                escrever += x       
            Abrir2 = open(Banco, "w")
            Abrir2.writelines(escrever)
                            
        except IOError:
            pass
        
        except Exception as erro:
            messagebox.showerror("Erro Inesperado", erro)

        else:
            messagebox.showinfo("Sucesso", "Voto efetuado com sucesso!")
            self.janela_voto.destroy()
            self.janelaDados.destroy()
            self.prosseguir.deiconify()
            
    def validate(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        if(action=='1'):
            if text in '0123456789.-+':
                try:
                    float(value_if_allowed)
                    return True
                except ValueError:
                    return False
            else:
                return False
        else:
            return True

    def atualizarTela(self):
        global cont
        global cpfRelativo
        num = self.et1.get()
                
        if num == '':
            messagebox.showerror("Campo vazio!", 'Candidato não informado!')

        elif cont == num or num == '00':
            Banco = "votos/alunoVoto.txt"
            escrever = ''
            try:
                Abrir = open(Banco, "r")
                linhas = Abrir.readlines()
                for x in linhas:
                    separador = x.split('|')
                    if separador[0] == cpfRelativo:
                        separador[1] = '|V' 
                        separador.append('|' + self.et1.get()+'\n')
                        x = separador[0]+separador[1]+separador[2]
                    escrever += x
                    
                            
                Abrir2 = open(Banco, "w")
                Abrir2.writelines(escrever)
            except IOError:
                pass
                    
            except Exception as erro:
                messagebox.showerror("Erro Inesperado", erro)
                
            else:
                messagebox.showinfo("Sucesso", "Voto efetuado com sucesso!")
                cont = ''
                self.janela_voto.destroy()
                self.janelaDados.destroy()
                self.prosseguir.deiconify()
                    
        elif cont != num and num != '00' and num != '':
            arq = "candidatos/" + num + "/info.txt"
            try:
                abre = open(arq, "r")
                linhas = abre.readlines()
            except IOError:
                messagebox.showerror("Erro", "Candidato não identificado!\n Porfavor digite um número válido.")
                self.et1.delete(0, 'end')

            except Exception as erro:
                messagebox.showerror("Erro Inesperado", erro)

            else:
                self.lb3["text"] = linhas[0].strip("\n")
                self.lb5["text"] = linhas[1].strip("\n")
                self.lb7["text"] = linhas[2].strip("\n")
                self.imagem["file"] = "candidatos/" + num + "/" + num + ".png"
                #self.imagem = self.imagem.zoom(20)
                #self.imagem = self.imagem.subsample(50)
                abre.close()
                cont = self.et1.get()
        


cont = ''
NomePdf = 'Resultados'
j = 1
cont1 = 0
cpfRelativo = ''
caminho='padrao.png'

