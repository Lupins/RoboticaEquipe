# Segue parede que usa o princípio básico para explorar labirintos: siga a parede à direita
def execute(robot):
    # Atualiza a informação dos sensores
    robot.updateSensors()

    # Pega a informações dos sensores que são relevantes ao algoritmo
    side1 = robot.sonarReading[7]
    side2 = robot.sonarReading[8]
    front = robot.sonarReading[4]

    # Variavel para verificar se robo está paralelo à parede
    # Diferença entre dois sensores paralelos no robô
    diff = side1 - side2
    
    # Excessão caso sensor esteja longe demais
    if side1 == -1 or side2 == -1:
        diff = 0.0

    # Caso robô esteja indo em direção a uma parede: pare de andar e vire a esquerda
    if front < 0.5 and front > -1:
        headingToWall(robot)

    # Caso robô perca visão da parede a direita: pare de andar e vire a direita
    elif side1 == -1:
        lostRightWall(robot)
    
    # Casos com menor prioridade
    else:
        # Caso robô esteja se distânciando da parede
        if diff > 0.001 and side1 > 0.3:
            turnRight(robot)

        # Caso robô esteja se aproximando da parede
        elif diff < -0.001:
            turnLeft(robot)

        # Caso robô esteja paralelo a parede mas muito distânte
        elif side1 > 0.3:
            turnRight(robot)

        # Andar em linha reta
        else:
            goStraight(robot)

def goStraight(robot):
    robot.drive(0.07, 0)

def turnLeft(robot):
    robot.drive(0.07, 0.1)

def turnRight(robot):
    robot.drive(0.07, -0.1)

def headingToWall(robot):
    robot.drive(0.0, 0.1)

def lostRightWall(robot):
    robot.drive(0.0, -0.1)
