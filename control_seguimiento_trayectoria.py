from robot_omni_class import *

def seguimiento_de_trayectoria(xd,xdp,yd,ydp,phi,phid,x_c,y_c):
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
    phie=0

    p1 = K1*xe - xdp
    p2 = K2*ye - ydp
    p3 = K3*phie-phid

    av = np.array([xd+p1, yd+p1, phid+p3])
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
        # Example usage:
        robot.move(vx=1, vy=0, wz=1.5)  # Move the robot
        rospy.sleep(2)
        robot.stop()  # Stop the robot
        position = robot.get_position()
        print(position)
        yaw = robot.get_yaw()
        print(yaw)
        orientacion = robot.get_orientation()
        print(orientacion)
        velocidad_angular = robot.get_angular_velocity()
        print(velocidad_angular)
        robot.run()
    except rospy.ROSInterruptException:
        pass