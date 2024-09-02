def adicionar_name(vetor,nome):
    vetor.append(nome)
    print("Update vetor: ", nome)
def removerNome(vetor,nome):
    if nome in vetor:
        vetor.remove(nome)
    else:
        print("Nome não encontrado ")

def listarNomes(vetor):
    if vetor:
     for nome in vetor:
         print("Nomes na lista")
         print("\n",nome)
       
    else:
        print("A lista está vazia")

def main():
    vetor_nomes = []
    
    while True:
        print("Manipulando Vetores: ")
        menu = """
        [1] Adicionar Nome
        [2] Remover Nome
        [3] listar nomes
        [4] sair

        => """
        print(menu)

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            nome = input("Digite o nome a ser adicionado: ")
            adicionar_name(vetor_nomes, nome)
        elif opcao == '2':
            nome = input("Digite o nome a ser removido: ")
            removerNome (vetor_nomes,nome)

        elif opcao == '3':
            listarNomes(vetor_nomes)

        elif opcao == '4':
            print("Saindo ...")
            break

        else:
            print("Opção invalida. Tente novamente ")
if __name__ == "__main__" :
    main()
