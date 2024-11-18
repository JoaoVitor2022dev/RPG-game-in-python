print("BEM-VINDO AO GAME RPG EM PYTHON")

Inventario = []

# Usar um loop for com um numero  grande de interações para simular um jogo continuo 

while True: # 100 é um numero arbitrário grande para simunar a repetição
    print(" ")
    print("1. Ir para a cabana")
    print("2. Ir para a floresta")
    print("3. Sair do jogo")
    print("4. Ver inventario")
    print(" ")

    escolha = int(input("DIGITE SUA ESCOLHA:  "))

    if escolha == 1:
            print(" ")
            print("A cabana tem uma espada")
            print(" ")
            print("1. Pegar a espada")
            print("2. Ignorar a espada")
            print("3. Voltar para a floresta")
            print(" ")
            espada = int(input("O QUE VOCE FAZ? "))

            if espada == 1:
                 Inventario.append("espada")
                 print(" ")
                 print("O jogador conseguiu uma espada")
            elif espada == 2:
                 print(" ")
                 print("Seu inventário está vazio")
            elif espada == 3:
                 print(" ")
                 print("Voltar para a floresta")      
            else:
                 print(" ") 
                 print("Número inválido")   
                      
    elif escolha == 2:
            print(" ")    
            print(" 'Você está na floresta escura'")

    elif escolha == 3:
            print(" ")
            print(" 'Você saiu do jogo'")     
            break # fim do jogo
    elif escolha == 4:
          print(" ") 
          print("'Seu inventario'")
          for item in Inventario:
                print(f"Item - {item}")
              
    else:
          print("Número inválido")          