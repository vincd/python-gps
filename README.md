Python-GPS
----------

# Installation
## macos
Download and install the driver on Prolific [website](http://www.prolific.com.tw/US/ShowProduct.aspx?p_id=229&pcid=41)
After the reboot, the USB stick should be listed as `/dev/tty.usbserial`
To install the deamon, run the following command line:
```
brew install gpsd
```
The gps folder is provided as a standalone library if the daemon is on an other machine.

## ubuntu
The USB stick should be listed as `/dev/ttyUSB0`, then install the deamon:
```
sudo apt-get update
sudo apt-get install gpsd gpsd-clients python-gps
```

# Acknowledgments
Global Positioning System - daemon
