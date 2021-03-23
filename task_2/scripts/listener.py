#!/usr/bin/env python
import rospy
from task_2.msg import two_number
c=None
d=None
def callback(data):
    global c,d
    c = data.a
    d = data.b
   # rospy.loginfo("%d is number 1 is :  the number 2 is%d" % (data.a,data.b))
    publisher()

def listener():
    rospy.init_node("task2_listner", anonymous=True)
    rospy.Subscriber("two_number", two_number, callback)
    rospy.spin()


def print_final():
    e = d+c
    f = e*5
    return e, f

def publisher():
    pub = rospy.Publisher("final_output", two_number, queue_size=1)
    x,y = print_final()
    r=rospy.Rate(1)
    msg = two_number()
    while not rospy.is_shutdown():
      msg.a = x
      msg.b = y
      pub.publish(msg)
      #rospy.loginfo("The output obtained by multiplication of 4 with the sum of 2 and 3 is %d"% y)
      r.sleep()
     
 
if __name__ == '__main__':
    listener()
