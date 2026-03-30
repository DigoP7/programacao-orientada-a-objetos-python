# Exercício: Controle de lâmpada
# Objetivo: Simular o funcionamento de uma lâmpada (ligar, desligar e verificar estado).

class Lampada:
    def __init__(self):
        self.estado = False  # True = lâmpada ligada

    def liga_desliga(self):
        self.estado = not self.estado

    def ligar(self):
        self.estado = True

    def desligar(self):
        self.estado = False

    def visual(self):
        return "LIGADO" if self.estado else "DESLIGADO"

    def status(self):
        return f"Lâmpada\nStatus: {self.visual()}"

    def __str__(self):
        return f"Lâmpada\nStatus: {self.estado}"


def mostrar_status_lampadas(lampadas):
    print("\nEstado atual das lâmpadas:")
    for i, lampada in enumerate(lampadas, start=1):
        print(f"Lâmpada {i}: {lampada.visual()}")
    print()


def menu():
    # lampadas = [Lampada(), Lampada(), Lampada(), Lampada() ]
    lampadas = [Lampada() for _ in range(4)]

    while True:
        mostrar_status_lampadas(lampadas)
        try:
            escolha = int(input("Escolha uma lâmpada (1 a 4) ou 0 para sair: "))
            if escolha == 0:
                print("Encerrando o programa.")
                break
            if escolha < 1 or escolha > 4:
                print("Escolha inválida. Tente novamente.")
                continue

            acao = input("Digite 'ligar' ou 'desligar': ").strip().lower()
            if acao == "ligar":
                lampadas[escolha - 1].ligar()
            elif acao == "desligar":
                lampadas[escolha - 1].desligar()
            else:
                print("Ação inválida. Use 'ligar' ou 'desligar'.")
        except ValueError:
            print("Entrada inválida. Use números para escolher a lâmpada.")
        print("-" * 40)

menu()
