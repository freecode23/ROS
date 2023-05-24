#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from turtlesim.srv import SetPen
from geometry_msgs.msg import Twist

# make sure to run master
# roserun turtlesim_node 
# roserun controller.py
prevx = 0

def call_set_pen_service(r, g, b, width, off):
    try:
        # create client that will call the service
        setpen = rospy.ServiceProxy("/turtle1/set_pen", SetPen)
        setpen(r, g, b, width, off)

    except rospy.ServiceException as e:
        rospy.logwarn(e)


def publish_cmd(pose: Pose):
    cmd = Twist()
    # PART 1. Send command to topic (publish)
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

    # PART 2. send request to service
    global prevx 
    # caseA. turtle on right hand side
    if pose.x >= 5.5 and prevx < 5.5:
        call_set_pen_service(255, 0, 0, 3, 0)
    elif pose.x < 5.5 and prevx >= 5.5:
        call_set_pen_service(0, 255, 0, 3, 0)
    
    prevx = pose.x


if __name__ == "__main__":
    # 0. init node
    rospy.init_node("controller_node")

    # 1. wait for service (make sure it exist before we call it when we do callback
    rospy.wait_for_service("/turtle1/set_pen")

    # 2. init publisher and subscriber
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    subser = rospy.Subscriber("/turtle1/pose", Pose, callback=publish_cmd)
    rospy.loginfo("Node has been started")

    # 3. listen and send callback if msg received
    rospy.spin()
