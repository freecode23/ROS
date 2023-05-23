#!/usr/bin/env python3


import rospy
from turtlesim.msg import Pose

def print_pose(msg: Pose):

    rospy.loginfo("("+ str(msg.x)+ "," + str(msg.y) +")")

if __name__ == "__main__":
    rospy.init_node("pose_subscriber_node")

    subser = rospy.Subscriber("/turtle1/pose", Pose, callback=print_pose)

    rospy.loginfo("Node has been started")

    rospy.spin()



    
    
    
