#!/bin/sh
#/etc/init.d/ipacquire
### BEGIN INIT INFO
# Provides:          start_tool
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: start_tool
# Description: this service is used to start my application
### END INIT INFO

case "$1" in
	start)
		echo "Starting app"
		#python /home/pi/py/fft/puship.py
		python /home/pi/py/writetotext.py
		;;
	stop)
		echo "Stop"
		#kill $( ps aux | grep -m 1 'python /home/pi/py/fft/puship.py' | awk '{ print $2 }')
		kill $( ps aux | grep -m 1 'python /home/pi/py/writetotext.py' | awk '{ print $2 }')
		;;
	*)
		echo "Usage:service ipacquire start|stop"
		exit 1
		;;
esac
exit 0


