#!/usr/bin/env python3.7



import rospy, math, numpy as np

from std_msgs.msg import Float32MultiArray


rospy.init_node('basic_motion', anonymous=True)

pub = rospy.Publisher('/wheel_speed', Float32MultiArray, queue_size=10)

rospy.sleep(1)


forward = [1, 1, 1, 1]

msg = Float32MultiArray(data=forward)

pub.publish(msg)

rospy.sleep(1)

backward = [-1, -1, -1, -1]

msg = Float32MultiArray(data=backward)

pub.publish(msg)


rospy.sleep(1)


left = [-1, 1, -1, 1]

msg = Float32MultiArray(data=left)

pub.publish(msg)


rospy.sleep(1)


right = [1, -1, 1, -1]

msg = Float32MultiArray(data=right)

pub.publish(msg)


rospy.sleep(1)


counterclockwise = [-1, 1, 1, -1]

msg = Float32MultiArray(data=counterclockwise)

pub.publish(msg)


rospy.sleep(1)


clockwise = [1, -1, -1, 1]

msg = Float32MultiArray(data=clockwise)

pub.publish(msg)


rospy.sleep(1)


stop = [0,0,0,0]

msg = Float32MultiArray(data=stop)

pub.publish(msg)