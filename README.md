# ROS audio\_common Package

To get started, clone the repository into your ROS workspace, build with `catkin build` and source `devel/setup.bash`.

When compiling on Ubuntu 16.04, there can be a missing package issue - make sure **GStreamer** is installed.  
Here is an installation command for Ubuntu or Debian:  
```
sudo apt-get install libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio libgstreamer-plugins-base1.0-dev
```

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
