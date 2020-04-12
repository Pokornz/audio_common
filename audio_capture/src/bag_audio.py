#!/usr/bin/env python
import os

import rospy

import time

bag_name = ""
bag_path = ""

from std_msgs.msg import Bool

recording = False

def callback(data):
	global bag_name
	global recording

	#start and stop recording
	if data.data == True and recording == False:

		bag_name = str(time.gmtime().tm_year) + "_" + str(time.gmtime().tm_mday) + "_" + str(time.gmtime().tm_mon) + "_" + str(time.gmtime().tm_hour) + "_" + str(time.gmtime().tm_min) + "_" + str(time.gmtime().tm_sec)

		recording = True

		#OBS! change path name
		os.system("rosbag record -O " + bag_path + "/" + bag_name + " /audio_mic/audio /audio_onboard/audio __name:=audiorecord_bag")

	elif data.data == False and recording == True:

		recording = False

		os.system("rosnode kill audiorecord_bag")


def listener(test):
	global bag_path

	#init the node as 'audio_bagger'
	rospy.init_node('audio_bagger', anonymous=True)
	bag_path = rospy.get_param('/audio_bagger/bag_path')
	rospy.loginfo("Bags will be saved to " + bag_path)

	rospy.Subscriber("record_audio", Bool, callback)

	rospy.loginfo("waiting for topic 'record_audio' = 1")

	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()


if __name__ == '__main__':
	listener(0)

#Following command can be used to start/stop bagging: 
#rostopic pub record_audio std_msgs/Bool 1
#rostopic pub record_audio std_msgs/Bool 0
