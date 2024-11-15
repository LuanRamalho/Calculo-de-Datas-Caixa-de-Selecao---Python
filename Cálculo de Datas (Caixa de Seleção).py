import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

def calcular_diferenca():
    # Obtendo as datas das caixas de seleção
    data1_str = combo_data1.get()
    data2_str = combo_data2.get()

    # Convertendo as strings para objetos de data
    try:
        data1 = datetime.strptime(data1_str, "%Y-%m-%d")
        data2 = datetime.strptime(data2_str, "%Y-%m-%d")
        
        # Calculando a diferença
        diferenca = abs(data2 - data1)
        anos = diferenca.days // 365
        meses = (diferenca.days % 365) // 30
        dias = (diferenca.days % 365) % 30

        # Atualizando o rótulo de resultado
        resultado_var.set(f"Diferença: {anos} anos, {meses} meses e {dias} dias")
    except ValueError:
        resultado_var.set("Erro ao calcular a diferença.")

# Gerar uma lista de datas
def gerar_datas(inicio, fim):
    delta = timedelta(days=1)
    datas = []
    while inicio <= fim:
        datas.append(inicio.strftime("%Y-%m-%d"))
        inicio += delta
    return datas

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora de Diferença entre Datas")
root.geometry("400x300")  # Tamanho da janela
root.configure(bg="#F0F8FF")  # Cor de fundo suave

# Definindo a faixa de datas
data_inicio = datetime(1950, 1, 1)
data_fim = datetime(2030, 12, 31)

# Gerando a lista de datas
lista_datas = gerar_datas(data_inicio, data_fim)

# Criando os widgets com cores e estilos aprimorados
label_data1 = ttk.Label(root, text="Selecione Data 1:", background="#F0F8FF", font=("Arial", 12))
label_data1.pack(pady=5)

combo_data1 = ttk.Combobox(root, values=lista_datas, font=("Arial", 12), width=20)
combo_data1.pack(pady=5)
combo_data1.set(lista_datas[0])  # Definindo um valor padrão

label_data2 = ttk.Label(root, text="Selecione Data 2:", background="#F0F8FF", font=("Arial", 12))
label_data2.pack(pady=5)

combo_data2 = ttk.Combobox(root, values=lista_datas, font=("Arial", 12), width=20)
combo_data2.pack(pady=5)
combo_data2.set(lista_datas[1])  # Definindo um valor padrão

botao_calcular = tk.Button(root, text="Calcular Diferença", command=calcular_diferenca, font=("Arial", 12, "bold"), bg="darkgreen", fg="snow")
botao_calcular.pack(pady=15)

resultado_var = tk.StringVar()
label_resultado = ttk.Label(root, textvariable=resultado_var, background="#F0F8FF", font=("Arial", 12, "bold"), foreground="#333333")
label_resultado.pack(pady=10)

# Iniciando o loop da interface gráfica
root.mainloop()
