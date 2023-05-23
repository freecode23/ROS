#!/usr/bin/env python3

# to run:
# sherly@sherly-Inspiron-15-3510:~/Desktop/ROS/catkin_ws/src$ rosrun my_robot_controller my_first_node.py 

import rospy
from geometry_msgs.msg import Twist

if __name__ == "__main__":
    rospy.init_node("draw_circle_node")
    rospy.loginfo("Node has been started")
    
    # 1. create publisher object
    # a)give it name of the topic"
    # from turtlesim rostopic list
    # get the velocity command topic

    # b) get the data type:
    # rostopic info /turtle1/cmd_vel
    # rostopic show geometry_msgs/Twist
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10 )
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 2.0

        pub.publish(msg)
        rate.sleep()

