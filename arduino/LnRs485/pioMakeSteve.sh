#!/bin/bash
action=$1
device=$2
VERBOSE=-v
VERBOSE=

function SYNTAX {
    echo
    echo "immettere l'azione ed il device da programmare:"
    echo "azione: (anche più di uno senza spazi intermedi)"
    echo "      b - build"
    echo "      c - clean"
    echo "      m - monitor serial"
    echo "      u - upload"
    echo
    echo "device:"
    echo "      Es. /dev/ttyUSB0"
    echo
    exit
}

# device=/dev/ttyUSB0
    [[ "$action" = "" ]] && SYNTAX


function creaLink() {
    ln -s /home/pi/485d_Loreto/Arduino/LnLibraries/LnFunctions      /home/pi/485d_Loreto/Arduino/rs485-Full/lib/LnFunctions
    ln -s /home/pi/485d_Loreto/Arduino/LnLibraries/RS485_protocol   /home/pi/485d_Loreto/Arduino/rs485-Full/lib/RS485_protocol
}

function deleteLink() {
    rm -f /home/pi/485d_Loreto/Arduino/rs485-Full/lib/LnFunctions
    rm -f /home/pi/485d_Loreto/Arduino/rs485-Full/lib/RS485_protocol
}


#cleam
if [[ "$action" =~ "c" ]]; then
    echo "------"
    echo "CLEAN"
    echo "------"
    echo
    platformio run --target clean
fi

#build
# creaLink
if [[ "$action" =~ "b" ]]; then
    echo "------"
    echo "BUILD"
    echo "------"
    echo
    platformio run  --environment nano
fi

#upload
if [[ "$action" =~ "u" ]]; then
    [[ "$device" = "" ]] && SYNTAX
    echo "------"
    echo "UPLOAD"
    echo "------"
    echo
    echo platformio run --target upload --upload-port $device
    platformio run --target upload --upload-port $device
fi
# deleteLink


#monitor
if [[ "$action" =~ "m" ]]; then
    [[ "$device" = "" ]] && SYNTAX
    echo "------"
    echo "MONITOR"
    echo "------"
    echo
    echo platformio device monitor -p $device
    platformio device monitor -p $device
fi

  CLEAN='platformio run --target clean'
  BUILD='platformio run --environment nano'
 UPLOAD='platformio run --target upload --upload-port /dev/ttyUSB0'
MONITOR='platformio device monitor -p /dev/ttyUSB0'