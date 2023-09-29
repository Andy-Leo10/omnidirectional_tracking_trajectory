from robot_omni_class import *
import time

def seguimiento_de_trayectoria(xd,xdp,yd,ydp,phid,phidp,robot):
    
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
    p3 = K3*phie-phidp

    av = np.array([p1, p2, p3])
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

if __name__ == '__main__':
    try:
        robot = RobotOmni()
        #hacemos una trayectoria que se actualiza cada 0.5 segundos
        tiempo=0.0
        v=0.5
        dt=0.005
        while tiempo<2.0:
            xd=1
            xdp=0
            yd=-1
            ydp=0
            phi=-1*pi/3
            phid=0
            #obtenemos las velocidades respecto del robot para seguir la trayectoria
            u,v,w=seguimiento_de_trayectoria(xd,xdp,yd,ydp,phi,phid,robot)
            robot.move(u,v,w)
            print(tiempo)
            tiempo+=dt
            time.sleep(dt)
        robot.stop()
        while tiempo<6.0:
            xd=1
            xdp=0
            yd=-1
            ydp=0
            phi=0
            phid=0
            #obtenemos las velocidades respecto del robot para seguir la trayectoria
            u,v,w=seguimiento_de_trayectoria(xd,xdp,yd,ydp,phi,phid,robot)
            robot.move(u,v,w)
            print(tiempo)
            tiempo+=dt
            time.sleep(dt)
        robot.stop()
        print("---FIN---")
    except rospy.ROSInterruptException:
        pass


#roslaunch neo_description mpo_500_controller.launch
#python control_seguimiento_trayectoria.py