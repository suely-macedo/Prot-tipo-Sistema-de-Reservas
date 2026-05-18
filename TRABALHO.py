import sqlite3
 
import tkinter as tk
lista_matriculas = open("Matriculas.txt", "r").read()
 
connection = sqlite3.connect("teste.bd")
cursor = connection.cursor()
 
cursor.execute("CREATE TABLE IF NOT EXISTS reservas (Id INTEGER, Nome TEXT, Matricula TEXT, Dtinicio TEXT, Periodo INTEGER)")

cursor.execute("DELETE FROM reservas")
 
#O if not exists é para se a tabela não tiver sido criada, se já estiver ela pula linha.
cursor.execute("INSERT INTO reservas VALUES('001', 'Ana', '202572272', '06/05', '5h')")
 
cursor.execute("INSERT INTO reservas VALUES('002', 'Paulo', '20257772', '07/05', '8h')")
 
connection.commit()
connection.close()

def reservas():
    matricula_digitada = matr_var.get()
    if matricula_digitada in lista_matriculas:
 
        print("Acesso garantido! Aluno matriculado.")
 
 
        nome = name_var.get()
    else:
 
        print("Acesso negado! Matrícula não encontrada.")
 
def PegaValores():
    connection = sqlite3.connect("teste.bd")
 
    cursor = connection.cursor()
 
    rows = cursor.execute("SELECT * FROM reservas").fetchall()
 
    for linha in rows:
 
        texto_linha = f"ID: {linha[0]} | Nome: {linha[1]} | Matrícula: {linha[2]} | Início: {linha[3]} | Período: {linha[4]}"
        print(texto_linha)
        
    connection.close()
    return rows

def Ex():
    Results = PegaValores()
    print(Results[0][0])


    root = tk.Tk()

    for aluno in Results:
        texto=str(aluno[0])
        tk.Label(root, text=aluno[0]).pack()

        tk.Button(root, text="Presença").pack()
 
        root.title("Sistema de Reserva de Quartos")

root=tk.Tk()
root.geometry("500x200")
name_var=tk.StringVar()
 
matr_var=tk.StringVar()
 
hora_var=tk.StringVar()
 
period_var=tk.StringVar()
 
 
tk.Label(root, text="Nome ").pack()
 
entry_nome = tk.Entry(root, textvariable  = name_var, font=('arial',12))
 
entry_nome.pack()
tk.Label(root, text="Matrícula").pack()
 
entry_matricula = tk.Entry(root, textvariable  = matr_var, font=('arial',12))
 
entry_matricula.pack()
tk.Label(root, text="Dt de Início").pack()
 
entry_hora = tk.Entry(root, textvariable  = hora_var, font=('arial',12))
 
entry_hora.pack()
tk.Label(root, text="Periodo").pack()
 
entry_tempo = tk.Entry(root, textvariable  = period_var, font=('arial',12))
 
entry_tempo.pack()

tipo_quarto = tk.StringVar(value="")
 
tk.Label(root, text="Escolha o tipo de quarto: ").pack()

tk.Radiobutton(root, text="Quarto premium", variable = tipo_quarto, value = "premium"). pack()

tk.Radiobutton(root, text="Quarto comum", variable = tipo_quarto, value= "comum" ).pack()

 
b1= tk.Button(root, text= "confirma")
 
b1['command']= reservas
 
b1.pack()

btn_sair = tk.Button(root, text="Sair", command=root.destroy)

btn_sair.pack()
 
PegaValores()

 
root.mainloop()
