def adicionar_funcionario(vetor,nome,salario):
    vetor.append({"nome":nome, "salario":salario})
    print("Nome adicionado: ", nome)
    print("Salário adicionado: ", salario)
def remover_funcionario(vetor,nome):
    for funcionario in vetor:
        if funcionario["Nome"] == nome:
            vetor.remove(funcionario)
            print("Funcionario removido ", nome)
        else:
            print("Funcionario não encontrado")
    else:
        print("Nome não encontrado ")

def listar_funcionarios(vetor):
    if vetor:
     for funcionario in vetor:
         print("Nome: ", funcionario["nome"])
         print("Salário: ", funcionario["salario"])
       
    else:
        print("Nenhum funcionário cadastrado")

def main():
    vetor_funcionarios = []
    
    while True:
        print("Manipulando Vetores: ")
        menu = """
        [1] Adicionar funcionário
        [2] Remover funcionário
        [3] listar funcionarios
        [4] sair

        => """
        print(menu)

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            nome = input("Digite o nome a ser adicionado: ")
            salario = float (input("Informe o salário: "))
            adicionar_funcionario(vetor_funcionarios, nome, salario)
        elif opcao == '2':
            nome = input("Digite o nome a ser removido: ")
            remover_funcionario (vetor_funcionarios,nome)

        elif opcao == '3':
            listar_funcionarios(vetor_funcionarios)

        elif opcao == '4':
            print("Saindo ...")
            break

        else:
            print("Opção invalida. Tente novamente ")
if __name__ == "__main__" :
    main()
