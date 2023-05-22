lista_fruta = []

#def sao como divs em html vc usa para criar funçoes separadas das demais.
#def para criar uma fruta
def adicionar_fruta():
    fruta = input('Digite o nome da sua fruta: ')
    lista_fruta.append(fruta)
    print('Fruta adicionada com sucesso!')
 
#segundo def irei usar para mostrar as frutas
def exibir_frutas():
    print('Aqui está a sua lista de fruta:')
    for frutas in lista_fruta:
        print(frutas)
 #Terceiro para remover as frutas
def remover_fruta():
    fruta = input('Digite o nome da fruta que deseja remover: ')
    if fruta in lista_fruta:
        lista_fruta.remove(fruta)
        print('Fruta removida!!')
    else:
            print('Essa fruta não esta na lista!')
 
 # Esse while true é para escolher entre as opçoes
 # e tambem dar os comandos de resposta para o pc do usuario :)
 
while True:
    
    print('Adicionar fruta: 1')
    print('Ver sua lista de fruta: 2')
    print('remover sua alguma fruta: 3')
    print('Sair da lista de fruta.')
    
    opcao = input('Digite sua opção entre 1-4: ')
    
    if opcao == '1':
        adicionar_fruta()
    elif opcao == '2':
        exibir_frutas()
    elif opcao == '3':
        remover_fruta()
    elif opcao == '4':
        break
    else:
        print('Opção invalida tente novamente!!')
            
    
    #gabrielleiteoliveiradasilva