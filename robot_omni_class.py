#!/usr/bin/env python

import rospy
import numpy as np
from std_msgs.msg import Float32MultiArray
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped, Twist
import tf.transformations as tf
import math
from math import pi

class RobotOmni:
    def __init__(self):
        rospy.init_node('robot_omni_controller', anonymous=True)

        self.length = 0.500 / 2
        self.radius = 0.254 / 2
        self.width = 0.548 / 2
        self.wheel_radius = self.radius

        self.H = np.array([[-self.length - self.width, 1, -1],
                           [self.length + self.width, 1, 1],
                           [self.length + self.width, 1, -1],
                           [-self.length - self.width, 1, 1]]) / self.radius

        self.velocity_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self.wheel_speed_publisher = rospy.Publisher('wheel_speed', Float32MultiArray, queue_size=10)
        self.odom_subscriber = rospy.Subscriber('odom', Odometry, self.odom_callback)
        self.pose = PoseStamped()
        self.twist=Twist()
        self.yaw = 0.0
        self.maxVel = 1.0
        self.maxAngVel = 1.0

        rospy.sleep(1)

    def twist_to_wheels(self, wz, vx, vy):
        twist = np.array([wz, vx, vy])
        twist.shape = (3, 1)
        wheel_speeds = np.dot(self.H, twist)
        return wheel_speeds.flatten().tolist()

    def move(self, vx, vy, wz):
        #colocamos un saturador para que no se exceda la velocidad lineal
        if vx>self.maxVel:
            vx=self.maxVel
        elif vx<-self.maxVel:
            vx=-self.maxVel
        if vy>self.maxVel:
            vy=self.maxVel
        elif vy<-self.maxVel:
            vy=-self.maxVel
        #colocamos un saturador para que no se exceda la velocidad angular
        if wz>self.maxAngVel:
            wz=self.maxAngVel
        elif wz<-self.maxAngVel:
            wz=-self.maxAngVel
        #realizamos la publicacion de la velocidad lineal y angular SEGURA
        wheel_speeds = self.twist_to_wheels(wz, vx, vy)
        print("Velocidades:", round(vx, 3), round(vy, 3), round(wz, 3))
        msg = Float32MultiArray(data=wheel_speeds)
        self.wheel_speed_publisher.publish(msg)

    def stop(self):
        stop = [0, 0, 0, 0]
        msg = Float32MultiArray(data=stop)
        self.wheel_speed_publisher.publish(msg)

    def odom_callback(self, data):
        self.pose = data.pose.pose
        quaternion = (data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w)
        euler = tf.euler_from_quaternion(quaternion)
        self.yaw = euler[2]

    def get_position(self):
        return self.pose.position

    def get_linear_velocity(self):
        return self.twist.linear

    #obtenemos la velocidad angular en el eje z
    def get_angular_velocity(self):
        return self.twist.angular.z

    def get_yaw(self):
        #return self.yaw
        #se agrego lo de abajo
        res = self.yaw
        while res > pi:
            res -= 2.0 * pi
        while res < -pi:
            res += 2.0 * pi
        return res

    def get_orientation(self):
        res = self.yaw
        while res > pi:
            res -= 2.0 * pi
        while res < -pi:
            res += 2.0 * pi
        #return res
        return math.degrees(res)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    try:
        robot = RobotOmni()
        # Example usage:
        robot.move(vx=0, vy=0, wz=1.5)  # Move the robot
        rospy.sleep(1)
        robot.stop()  # Stop the robot
        position = robot.get_position()
        print(position)
        yaw = robot.get_yaw()
        print(yaw)
        velocidad_angular = robot.get_angular_velocity()
        print(velocidad_angular)
        robot.stop()
        robot.run()
    except rospy.ROSInterruptException:
        pass
