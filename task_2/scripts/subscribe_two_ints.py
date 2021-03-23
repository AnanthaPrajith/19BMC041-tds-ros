#!/usr/bin/env python  
import rospy

from task_2.msg import two_number

def callback(data):
    global c,d
    c = data.a
    d = data.b
    rospy.loginfo("a=1;b=2;     (1+2)*5= %d"% d)
   # publisher()



def listener():
    rospy.init_node("task_subscriber", anonymous=True)
    rospy.Subscriber("final_output", two_number, callback)


    rospy.spin()



if __name__ == '__main__':
    listener()
