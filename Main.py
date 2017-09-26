import Robot as rb
from Simulator import Simulator
import WallFollower as WF

#
# O objetivo deste programa e movimentar o robô p3dx de um ponto de partida até
# o ponto de chegada sem colidir com as paredes.
#
# O algoritmo usado é um wall follow usando a diferença entre os sensores de ID
# 7 e 8, usando também o sensor 4 para evitar colisões frontais.
#
# Tendo em vista que este programa serve como avaliação para selecionar membros
# de uma equipe a documentação do código foi priorizada, focando no
# entendimento do algoritmo mesmo para alguém que não tenha tido contato
# previo com o mesmo.
#
# O vídeo contendo o resultado do algoritmo se encontra no link:
# https://youtu.be/1zQgLIONleU
#
# Definir a variável VREP_LIB_PATH para o funcionamento do programa
#

def main():
    # Inicia a simulação
    sim = Simulator()

    # Conecta com o servidor
    sim.connect()

    # Pega o handler do pioneer dentro do Vrep
    robot = rb.newPioonerRobot(sim)

    # Variavel de controle para objetivo
    goal = False

    # Enquanto não realizar objetivo
    while not goal:

        # Roda algoritmo segue parede
        WF.execute(robot)

        # Posição do objetivo
        position = robot.sim.getObjectPosition(robot.sonarHandle[4])
        # Se estiver em cima ou depois do objetivo, pare o robô
        if position[0] > 1.47 and position[1] < -1.34:
            goal = True

    # Para o robo
    robot.drive(0, 0)

    # Desconecta do servidor
    # sim.disconnect()

# Roda o programa
main()
