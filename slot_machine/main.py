import random

MAX_LINHAS = 3
MAX_APOSTA = 100
MIN_APOSTA = 1

FILEIRAS = 3
COLUNAS = 3

qtda_simbolos = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

valor_simbolos = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def checar_ganhos(colunas, fileiras, aposta, valores):
    ganhos = 0
    fileiras_ganhas = []
    for fileira in range(fileiras):
        simbolo = colunas[0][fileira]
        for coluna in colunas:
            simbolo_a_checar = coluna[fileira]
            if simbolo != simbolo_a_checar:
                break
        else:
            ganhos += valores[simbolo] * aposta
            fileiras_ganhas.append(fileira + 1)

    return ganhos, fileiras_ganhas

def get_slot_machine_spin(fileiras, colunas, simbolos):
    todos_os_simbolos = []
    for simbolo, qtda_simbolos in simbolos.items():
        for _ in range(qtda_simbolos):
            todos_os_simbolos.append(simbolo)

    coluna = []
    for _ in range(colunas):
        col = []
        simbolos_atuais = todos_os_simbolos[:]
        for _ in range(fileiras):
            valor = random.choice(simbolos_atuais)
            simbolos_atuais.remove(valor)
            col.append(valor)

        coluna.append(col)

    return coluna

def print_slot_machine(coluna):
    for fileira in range(len(coluna[0])):
        for i, col in enumerate(coluna):
            if i != len(coluna) - 1:
                print(col[fileira], end=" | ")
            else:
                print(col[fileira], end="")
        print()



def deposito():
     while True:
         quantia = input("Quanto você gostaria de depositar? $")
         if quantia.isdigit():
             quantia = int(quantia)
             if quantia > 0:
                 break
             else:
                 print("A quantia deve ser maior que 0.")
         else:
             print("Por favor, insira um número.")

     return quantia

def get_num_de_linhas():
    while True:
         linhas = input("Entre com o número de linhas em que gostaria de apostar (1 - " + str(MAX_LINHAS) +")? ")
         if linhas.isdigit():
             linhas = int(linhas)
             if 1 <= linhas <= MAX_LINHAS:
                 break
             else:
                 print("Insira um número válido de linhas.")
         else:
             print("Por favor, insira um número.")

    return linhas

def get_aposta():
    while True:
         aposta = input("Quanto você gostaria de apostar em cada linha? $")
         if aposta.isdigit():
             aposta = int(aposta)
             if MIN_APOSTA <= aposta <= MAX_APOSTA:
                 break
             else:
                 print(f"O valor da aposta deve estar entre ${MIN_APOSTA} - ${MAX_APOSTA} ")
         else:
             print("Por favor, insira um número.")

    return aposta

def giro(saldo):
    linhas = get_num_de_linhas()

    while True:
        aposta = get_aposta()
        total_aposta = aposta * linhas
        if total_aposta > saldo:
            print(f"Você não possui saldo suficiente para realizar essa aposta, seu saldo atual é de ${saldo}.")
        else:
            break

    print(f"Você está apostando ${aposta} em {linhas} linhas. A aposta total é: ${total_aposta}.")

    slots = get_slot_machine_spin(FILEIRAS, COLUNAS, qtda_simbolos)
    print_slot_machine(slots)
    ganhos, fileiras_ganhas = checar_ganhos(slots, linhas, aposta, valor_simbolos)
    print(f"Você ganhou ${ganhos}.")
    print(f"Você ganhou na(s) fileira(s): ", *fileiras_ganhas)
    return ganhos - total_aposta


def main():
    saldo = deposito()
    while True:
        print(f"Saldo Atual: ${saldo}")
        resposta = input("Pressione enter para jogar (s para sair).")
        if resposta == "s":
            break
        saldo += giro(saldo)

    print(f"Você terminou com: ${saldo}")
    
    
main()