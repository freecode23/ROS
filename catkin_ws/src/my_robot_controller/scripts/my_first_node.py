#!/usr/bin/env python3

# to run:
# sherly@sherly-Inspiron-15-3510:~/Desktop/ROS/catkin_ws/src$ rosrun my_robot_controller my_first_node.py 

import rospy

if __name__ == "__main__":
    rospy.init_node("test_node")
    rospy.loginfo("hello from test node")
    rate = rospy.Rate(10) # 10 ms

    # inf loop
    while not rospy.is_shutdown():
        rospy.loginfo("hello")
        rate.sleep()
