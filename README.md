# ROS audio\_common Package

This repository contains the ROS audio\_common package.

For user documentation, please refer to the [ROS Wiki page for audio\_common](http://wiki.ros.org/audio_common)

# Enabling Monitor

To be able to record sounds coming from the computer:  
1. Move the `.asoundrc` file to the user directory (`~/`)
2. Edit the file: replace both instances of `#NAME` with the name of the **Monitor Source**. To find the name of the **Monitor Source**, type `pactl list` into terminal and use the Search function. See example (the name is in the red rectangle):
![monitor](/monitor.png)
3. Log out the user and log back in for the change to take effect.

# Recording Audio

- `roslaunch audio_capture capture_all.launch` starts publishing audio from built-in microphone to */audio_mic/audio* and onboard sounds to */audio_onboard/audio* topics
- `roslaunch audio_capture capture_all_bag.launch` same as above + launches an *audio_bagger* node, which starts and stops rosbagging audio based on a Bool from the *record_audio* topic

# Playing audio

- `roslaunch audio_play play_all.launch` plays audio published to */audio_mic/audio* and */audio_onboard/audio* topics. Use `rosbag play` to supply the audio.

NOTE: The mic and onboard audio is out of sync by a few seconds.
