#!/usr/bin/env python3
#coding=utf-8

import rospy
from std_msgs.msg import String

def talker():
    publisher = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker')
    rate = rospy.Rate(10)

    count = 0
    while not rospy.is_shutdown():
        hello_str = "Meteu essa " + str(count) + " ?"
        rospy.loginfo("Enviando mensagem " + str(count) + ".")
        count += 1
        publisher.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass