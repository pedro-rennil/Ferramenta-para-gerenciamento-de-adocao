from veterinario.operations import os
def menu_vet():
    print("===== Clinica veterinaria =====")
    print("1. Consulta")
    print("2. Exames")
    print("3. Cirurgia")
    print("4. Vacinas")
    print("5. Voltar ao Menu Principal")

def menu_consulta():
    print("1. Clinico geral - R$100")
    print("2. Cardiologia - R$450")
    print("3. Dermatologia - R$300")
    print("4. Animais Oftalmologista - R$230")
    print("5. Voltar ao Menu Principal")


def menu_exame():
    print("1. Ultrassom - R$120")
    print("2. Raio-x - R$180")
    print("3. Hemograma - R$35")
    print("4. Eletrocardiograma - R$120")
    print("5. Voltar ao Menu Principal")

def menu_cirurgia():
    print("1. Castração - R$700")
    print("2. Catarata - R$2000")
    print("3. Neoplasia - R$4000")
    print("4. Pata quebrada - 1500")
    print("5. Voltar ao Menu Principal")

def menu_vacina():
    print("1. V8 (óctupla) - R$60")
    print("2. V10 (déctupla) - R$65")
    print("3. Raiva - R$70 ")
    print("4. Gripe - R$90")
    print("5. Voltar ao Menu Principal")

def invalido():
    print("digite uma opção valida")

def main():
    while True:
        try:
          menu_vet()
          op = input("Escolha a opção: ")

          if op == '1':
              os.system("cls")
              menu_consulta()
              espec = int(print("Digite o numero da especialidade desejada"))
            
          elif op == '2':
              os.system("cls")
              menu_exame()
              exame = int(print("Digite o numero do Exame desejado"))

          elif op == '3':
            os.system("cls")
            menu_cirurgia()
            cirurgia = int(print("Digite o numero da cirurgia desejada"))

          elif op == '4':
              os.system("cls")
              menu_vacina()
              vacina = int(print("Digite o numero da vacina desejada"))
  
          elif op == '5':
              os.system("cls")
              print("Voltando ao menu principal...")
              break

          else:
              os.system("cls")
              print("Opção inválida! Tente novamente.")
        except:
            invalido()
              