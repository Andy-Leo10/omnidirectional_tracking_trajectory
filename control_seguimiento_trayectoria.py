from robot_omni_class import *
import time

def seguimiento_de_trayectoria(xd, xdp, yd, ydp, phid, phidp, robot):
    position = robot.get_position()
    x_c = position.x
    y_c = position.y
    phidesf = robot.get_yaw()

    # x_c: es x del centro entre ruedas
    # y_c: es y del centro entre ruedas

    d2 = 0.500 / 2
    K1 = 2
    K2 = 2
    K3 = 2

    # xdesf: es x desplazado
    # ydesf: es y desplazado

    xdesf = x_c + d2 * np.cos(phidesf)
    ydesf = y_c + d2 * np.sin(phidesf)

    # xd: es x deseado
    # yd: es y deseado

    xe = xd - xdesf
    ye = yd - ydesf
    phie = phid - phidesf

    p1 = K1 * xe + xdp
    p2 = K2 * ye + ydp
    p3 = K3 * phie + phidp

    av = np.array([p1, p2, p3])
    av.shape = (3, 1)

    # Matriz inversa:
    # [cos(phi)     sin(phi)    0
    #  -sin(phi)    cos(phi)    -d2
    #  0            0           1]

    M = np.array([
        [np.cos(phidesf), -np.sin(phidesf), -d2 * np.sin(phidesf)],
        [np.sin(phidesf), np.cos(phidesf), d2 * np.cos(phidesf)],
        [0, 0, 1]
    ])

    results = np.dot(np.linalg.inv(M), av)

    u = results[0, 0]
    v = results[1, 0]
    w = results[2, 0]
    return u, v, w

def seguir_trayectoria(robot, trayectoria):
    tiempo = 0.0
    dt = 0.005

    for punto in trayectoria:
        xd, xdp, yd, ydp, phi, phid, duracion = punto
        while tiempo < duracion:  # Controla el tiempo en cada segmento de la trayectoria
            # Obtener velocidades para seguir el punto actual
            u, v, w = seguimiento_de_trayectoria(xd, xdp, yd, ydp, phi, phid, robot)
            # Mover el robot y actualizar el tiempo
            robot.move(u, v, w)
            tiempo += dt
            time.sleep(dt)
        tiempo=0
        # Detener el robot al final de cada segmento
        robot.stop()
        print("---FIN DEL SEGMENTO---")

    print("---FIN DE LA TRAYECTORIA---")

if __name__ == '__main__':
    try:
        robot = RobotOmni()

        # Definir los puntos de la trayectoria (llegar a la escalera)
        trayectoria = [
            #(1.0, 0.0, 1.0, 0.0, 0.0, 0.0, t),  # Ejemplo: Avanzar 1 metro en diagonal
            # (xd, xdp, yd, ydp, phi, phid,t)
            # Define los puntos de la trayectoria aqui
            (0.0, 0.0, 7.0, 0.0, pi/2, 0.0,6),
            (-0.7, 0.0, 7.2, 0.0, 3*pi/2, 0.0,1),
            (-1.2, 0.0, 7.7, 0.0, pi, 0.0,2)
        ]

        seguir_trayectoria(robot, trayectoria)
        print("---FIN---")

    except rospy.ROSInterruptException:
        pass


#cd /home/user/catkin_ws/src/omni_pkg/src
#roslaunch neo_description mpo_500_controller.launch
#python control_seguimiento_trayectoria.py
#roslaunch neo_description mpo_500_controller.launch world_name_global:=/home/user/catkin_ws/src/omni_pkg/src/miDepaWorld.world