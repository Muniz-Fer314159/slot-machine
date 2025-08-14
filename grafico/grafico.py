import random
import matplotlib.pyplot as plt

# Função para simular uma única jogada no caça-níqueis
def jogar():
  # Gerar um número aleatório entre 0 e 1
  resultado = random.random()
  # Se o resultado for menor que 0.49, o jogador ganha
  if resultado < 0.49:
    return 1  # Retorna 1 para indicar que o jogador ganhou
  # Caso contrário, o jogador perde
  else:
    return -1  # Retorna -1 para indicar que o jogador perdeu

# Número de jogadas a serem simuladas
num_jogadas = 10000

# Listas para armazenar os resultados acumulados
resultados_jogador = []
resultados_maquina = []

# Simular as jogadas e armazenar os resultados acumulados
saldo_jogador = 0
saldo_maquina = 0
for i in range(num_jogadas):
    resultado_jogada = jogar()
    saldo_jogador += resultado_jogada
    saldo_maquina -= resultado_jogada  # Saldo da máquina é o inverso do jogador
    resultados_jogador.append(saldo_jogador)
    resultados_maquina.append(saldo_maquina)

# Plotar o gráfico de linhas
plt.plot(resultados_jogador, label='Saldo do Jogador')
plt.plot(resultados_maquina, label='Saldo da Máquina')
plt.title('Lei dos Grandes Números em um Caça-Níqueis')
plt.xlabel('Número de Jogadas')
plt.ylabel('Saldo Acumulado')
plt.legend()
plt.show()