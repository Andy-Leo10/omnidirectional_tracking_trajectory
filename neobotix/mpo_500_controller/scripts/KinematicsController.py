#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Twist

from HolonomicRobots import FourMechModel

def callback(msg):
    global pub
    global mpo_500
    
    u = msg.data
    wz, vx, vy = mpo_500.forwardKin(u)
    vel_msg = Twist()
    vel_msg.linear.x = vx
    vel_msg.linear.y = vy
    vel_msg.angular.z = wz
    pub.publish(vel_msg)
    
def kinematics_controller():
    global pub
    global mpo_500
    
    rospy.init_node('kinematics_controller', anonymous=True)

    rospy.Subscriber("wheel_speed", Float32MultiArray, callback)
    
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
    
    mpo_500 = FourMechModel(l=0.500/2, r=0.254/2, w=0.548/2)
    
    rospy.spin()

if __name__ == '__main__':
    kinematics_controller()
