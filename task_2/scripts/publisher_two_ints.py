#!/usr/bin/env python  
import rospy

from task_2.msg import two_number

def main():
   rospy.init_node("two_ints_publisher")
   pub = rospy.Publisher("two_number", two_number, queue_size=1)
   r=rospy.Rate(1)
   
   msg = two_number()
   while not rospy.is_shutdown():
      msg.a = 1
      msg.b = 2
      pub.publish(msg)
      r.sleep()

if __name__ =="__main__":
   try:
      main()
   except rospy.ROSInterruptException:
      pass  

