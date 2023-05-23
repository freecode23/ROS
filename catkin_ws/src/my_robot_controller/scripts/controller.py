#!/usr/bin/env python3


import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

def publish_cmd(pose: Pose):
    cmd = Twist()
    
    # 1. if out of bound move
    if pose.x < 2.0 or pose.x > 9.0 or pose.y < 2.0 or pose.x > 9.0:
        # turn around:
        cmd.linear.x = 1.0
        cmd.angular.z = 1.4

    # 2. if not out of bound run fast
    else:
        cmd.linear.x = 5.0
        cmd.angular.z = 0.0

    # 3. send command to cmd_vel topic
    pub.publish(cmd)

if __name__ == "__main__":
    rospy.init_node("controller_node")

    # 1. init publisher and subscriber
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    subser = rospy.Subscriber("/turtle1/pose", Pose, callback=publish_cmd)
    rospy.loginfo("Node has been started")

    # 2. listen and send callback if msg received
    rospy.spin()
