import os
from datetime import datetime

ARQUIVO_TAREFAS = 'tarefas.txt'

    
"""Carrega as tarefas do arquivo de texto"""
def carregar_tarefas():
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []
    with open(ARQUIVO_TAREFAS, 'r') as file:
        tarefas = file.readlines()
    return [tarefa.strip() for tarefa in tarefas]

"""Salva as tarefas no arquivo de texto"""
def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, 'w') as file:
        for tarefa in tarefas:
            file.write(f"{tarefa}\n")

"""Adiciona uma nova tarefa à lista com a data e horário"""
def adicionar_tarefa(tarefa, data_hora):
    tarefas = carregar_tarefas()
    tarefas.append(f"{tarefa} (Data e Hora: {data_hora})")
    salvar_tarefas(tarefas)
    print(f"Tarefa '{tarefa}' adicionada com sucesso para a data e hora {data_hora}!")

"""Remove uma tarefa da lista"""
def remover_tarefa(tarefa):
    tarefas = carregar_tarefas()
    tarefa_encontrada = False
    for tarefa_existente in tarefas:
        if tarefa in tarefa_existente:
            tarefas.remove(tarefa_existente)
            tarefa_encontrada = True
            break
    if tarefa_encontrada:
        salvar_tarefas(tarefas)
        print(f"Tarefa '{tarefa}' removida com sucesso!")
    else:
        print(f"Tarefa '{tarefa}' não encontrada.")

"""Extrai a data e hora da string da tarefa"""
def extrair_data_hora(tarefa):
    try:
        data_hora_str = tarefa.split("(Data e Hora: ")[1].strip(")")
        return datetime.strptime(data_hora_str, "%d/%m/%Y %H:%M")
    except (IndexError, ValueError):
        return None


"""Exibe as tarefas, ordenadas por data mais próxima até a mais distante"""
def visualizar_tarefas():
    tarefas = carregar_tarefas()
    tarefas.sort(key=extrair_data_hora)
    if tarefas:
        print("Tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")
    else:
        print("Nenhuma tarefa encontrada.")

"""Exibe o menu"""
def mostrar_menu():
    print("\nAgenda de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Visualizar Tarefas")
    print("4. Sair")

"""Verifica se data e horário estão no formato correto (DD/MM/YYYY HH:MM)"""
def validar_data_hora(data_hora_str):
    try:
        datetime.strptime(data_hora_str, "%d/%m/%Y %H:%M")
        return True
    except ValueError:
        return False

"""Função principal, regras que permitem interagir com o código corretamente"""
def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            tarefa = input("Digite a tarefa a ser adicionada: ")
            data_hora = input("Digite a data e horário da tarefa (DD/MM/YYYY HH:MM): ")
            if validar_data_hora(data_hora):
                adicionar_tarefa(tarefa, data_hora)
            else:
                print("Data e horário inválidos. Por favor, use o formato DD/MM/YYYY HH:MM.")
        elif escolha == '2':
            tarefa = input("Digite a tarefa a ser removida: ")
            remover_tarefa(tarefa)
        elif escolha == '3':
            visualizar_tarefas()
        elif escolha == '4':
            print("Saindo da agenda de tarefas.")
            break
        else:
            print("Opção inválida, por favor tente novamente.")

if __name__ == "__main__":
    main()
