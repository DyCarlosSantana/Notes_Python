"""
Exercício 89: Boletim com Listas Compostas
O que fazer: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo numa lista composta. No final, mostre um boletim contendo a média de cada um e permita que o utilizador possa consultar as notas de cada aluno individualmente.
"""
cadastros = [["Edy Carlos", 8, 9], ["Bruna Karla", 9, 10], ["Elisabeth", 8, 7], ["Carlos Brito", 5, 4]]
aluno = [] 
while True:
    try:
        print("====="*8)
        print("Digite [999] para Sair... ")
        option = int(input("[1] Buscar por ID \n[2] Lista Completa \n[3] Cadastrar Notas \n--> "))

        if option == 1:
            print("-----"*8)
            print("Digite [999] para voltar ao Inicio... ")
            while True:
                try:
                    print("-----"*8)
                    id_aluno = int(input("🔍 Buscar por Aluno (ID): "))
                    if id_aluno == 999:
                        print("↩️ Voltando ao Inicio...")
                        break

                    print(f"ID Aluno: {id_aluno}")
                    print(f"Nome: {cadastros[id_aluno][0]}") 
                    print(f"1° Nota: {cadastros[id_aluno][1]:.1f}")
                    print(f"2° Nota: {cadastros[id_aluno][2]:.1f}")
                    # Pega da lista cadastros a sublista com o 'id_aluno'(inddice), acessando os elementos da sublista.

                except:
                    print(f"ID: {id_aluno} não encontrado!")
        elif option == 2:
            while True:
                print("====="*8)
                print( "| id | Aluno                 |  Média  |")
                print("====="*8)
                for id, aluno in enumerate(cadastros):
                    media = (aluno[1] + aluno[2]) / 2
                    print(f"| {id}  |", end=' ')
                    print(f"{aluno[0]: <18}", end=' ')
                    print(f"{media:>10.1f}")
                print(" ")
                resp = int(input("Digite [999] para coltar ao Inicio... "))
                if resp == 999:
                    print("↩️ Voltando ao Inicio...")
                    break

        elif option == 3:
            while True:
                print("-----"*6)
                nome = str(input("Nome do Aluno: ")).strip()
                aluno.append(nome)
                n1 = int(input("1° Nota: "))
                aluno.append(n1)
                n2 = int(input("2° Nota: "))
                aluno.append(n2)
                cadastros.append(aluno[:])
                aluno.clear()
                print("-----"*6)

                resp = int(input("Digite [999] para voltar ao Inicio... \n[1] Continuar Cadastro \n--> "))
                if resp == 999:
                    print("↩️ Voltando ao Inicio...")
                    break
        elif option == 999:
            break
    except:
        print("Erro ao processar!")

print("Programa encerrado!")

# Nota: Execução Funciona, mas retorna um erros caso um novo cadastro seja feito e depois tente acessar a lista completa