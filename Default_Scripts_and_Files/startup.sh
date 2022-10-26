

mosquitto -c mosquitto.conf &
python3 radio_mqtt_bridge.py -p /dev/ttyUSB0 -v True -c radio_devices_list.json -ip 127.0.0.1 &
python3 command_runner.py &
#python3 sunset_sunrise_mqtt_publisher.py &
#python3 meteo.py &
cd /home/dietpi/display/OrangePi-OLED/examples/
python3 sys_info.py &

