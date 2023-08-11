#! /usr/bin/env python

import rospy #main python library
from sensor_msgs.msg import LaserScan ##ros msg that gets the laser scans

def callback_laser(msg):
  # 120 degrees into 3 regions
  # receive a value of range between 0 and 10.
  regions = [ 
    min(min(msg.ranges[0:2]), 10),
    min(min(msg.ranges[3:5]), 10),
    min( min(msg.ranges[6:9]), 10),
    ]

  rospy.loginfo(regions)

def main():
  rospy.init_node('reading_laser')
  sub= rospy.Subscriber("/robot/laser/scan", LaserScan, callback_laser)

  rospy.spin()   #keep running while the ros-master isn't shutdown

if __name__ == '__main__':
  main()
