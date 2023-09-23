from robot_omni_class import *
import time
import math

def seguimiento_de_trayectoria(xd,xdp,yd,ydp,phi,phid,robot):
    
    position=robot.get_position()
    x_c=position.x
    y_c=position.y
    phidesf=robot.get_yaw()
    
    # x_c: es x del centro entre ruedas
    # y_c: es y del centro entre ruedas

    d2 = 0.500 / 2
    K1 = 2
    K2 = 2
    K3 = 2

    # xdes: es x desplazado
    # ydes: es y desplazado

    xdesf = x_c + d2*np.cos(phi)
    ydesf = y_c + d2*np.sin(phi)

    # xd: es x deseado
    # yd: es y deseado

    xe = xd - xdesf
    ye = yd - ydesf
    phie=phid-phidesf

    p1 = K1*xe - xdp
    p2 = K2*ye - ydp
    p3 = K3*phie-phid

    av = np.array([xd+p1, yd+p2, phid+p3])
    av.shape = (3,1)

    # Matriz inversa:
    # [cos(phi)     sin(phi)    0
    #  -sin(phi)    cos(phi)    -d2
    #  0            0           1]

    M= np.array([
                [np.cos(phi), -np.sin(phi), -d2*np.sin(phi)],
                [-np.sin(phi), np.cos(phi), d2*np.cos(phi)],
                [0,             0,              1]
                ])

    results=np.dot(np.linalg.inv(M),av)
    
    u = results[0, 0]
    v = results[1, 0]
    w = results[2, 0]
    return u,v,w

def seguir_trayectoria(robot, trayectoria):
    tiempo = 0.0
    v = 0.5
    dt = 0.005

    for punto in trayectoria:
        xd, xdp, yd, ydp, phi, phid = punto
        while tiempo < 1.0:  # Controla el tiempo en cada segmento de la trayectoria
            # Obtener velocidades para seguir el punto actual
            u, v, w = seguimiento_de_trayectoria(xd, xdp, yd, ydp, phi, phid, robot)
            print("Velocidades:", u, v, w)

            # Mover el robot y actualizar el tiempo
            robot.move(u, v, w)
            tiempo += dt
            time.sleep(dt)
        tiempo=0
        # Detener el robot al final de cada segmento
        robot.stop()
        print("---FIN DEL SEGMENTO---")

    print("---FIN DE LA TRAYECTORIA---")

def generar_trayectoria_circular(radio, num_puntos):
    trayectoria = []
    angulo_entre_puntos = 2 * math.pi / num_puntos
    
    for i in range(num_puntos):
        angulo = i * angulo_entre_puntos
        x = radio * math.cos(angulo)
        y = radio * math.sin(angulo)
        xd = 0.0  # Velocidad en x (opcional)
        yd = 0.0  # Velocidad en y (opcional)
        phi = 0.0  # Orientacion (opcional)
        phid = 0.0  # Velocidad angular (opcional)
        
        trayectoria.append((x, xd, y, yd, phi, phid))
    
    return trayectoria

if __name__ == '__main__':
    try:
        robot = RobotOmni()
        
        radio = 4.0  # Radio de la trayectoria circular
        num_puntos = 36  # Numero de puntos en la trayectoria circular
        # Definir los puntos de la trayectoria 
        trayectoria = generar_trayectoria_circular(radio, num_puntos)
        # (xd, xdp, yd, ydp, phi, phid)
        seguir_trayectoria(robot, trayectoria)
        print("---FIN---")
    except rospy.ROSInterruptException:
        pass



#roslaunch neo_description mpo_500_controller.launch
#python control_seguimiento_trayectoria.py