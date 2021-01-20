import os
import time

def download():
    print("Installing libfontconfig1-dev")
    os.system("sudo apt install libfontconfig1-dev -y")
    time.sleep(1)

    print("Installing libfreetype6-dev")
    os.system("sudo apt install libfreetype6-dev -y")
    time.sleep(1)

    print("Installing libx11-dev")
    os.system("sudo apt install libx11-dev -y")
    time.sleep(1)

    print("Installing libx11-xcb-dev")
    os.system("sudo apt install libx11-xcb-dev -y")
    time.sleep(1)

    print("Installing libxext-dev")
    os.system("sudo apt install libxext-dev -y")
    time.sleep(1)

    print("Installing libxfixes-dev")
    os.system("sudo apt install libxfixes-dev -y")
    time.sleep(1)

    print("Installing libxi-dev")
    os.system("sudo apt install libxi-dev -y")
    time.sleep(1)

    print("Installing libxrender-dev")
    os.system("sudo apt install libxrender-dev -y")
    time.sleep(1)

    print("Installing libxcb1-dev")
    os.system("sudo apt install libxcb1-dev -y")
    time.sleep(1)
    
    print("Installing libxcb-glx0-dev")
    os.system("sudo apt install libxcb-glx0-dev -y")
    time.sleep(1)

    print("Installing libxcb-keysyms1-dev")
    os.system("sudo apt install libxcb-keysyms1-dev -y")
    time.sleep(1)

    print("Installing libxcb-image0-dev")
    os.system("sudo apt install libxcb-image0-dev -y")
    time.sleep(1)

    print("Installing libxcb-shm0-dev")
    os.system("sudo apt install libxcb-shm0-dev -y")
    time.sleep(1)

    print("Installing libxcb-icccm4-dev")
    os.system("sudo apt install libxcb-icccm4-dev -y")
    time.sleep(1)

    print("Installing libxcb-sync0-dev")
    os.system("sudo apt install libxcb-sync0-dev -y")
    time.sleep(1)

    print("Installing libxcb-xfixes0-dev")
    os.system("sudo apt install libxcb-xfixes0-dev -y")
    time.sleep(1)

    print("Installing libxcb-shape0-dev")
    os.system("sudo apt install libxcb-shape0-dev -y")
    time.sleep(1)

    print("Installing libxcb-randr0-dev")
    os.system("sudo install libxcb-randr0-dev -y")
    time.sleep(1)

    print("Installing libxcb-render-util0-dev")
    os.system("sudo apt install libxcb-render-util0-dev -y")
    time.sleep(1)

    print("Installing libxcd-xinerama-dev -y")
    os.system("sudo apt install libxcd-xinerama-dev-y ")
    time.sleep(1)

    print("Installing libxkbcommon-dev")
    os.system("sudo apt install libxkbcommon-dev -y")
    time.sleep(1)

    print("Installing libxkbcommon-x11-dev -y")
    os.system("sudo apt install libxkbcommon-x11-dev -y")
    time.sleep(1)

    print("Installing libatspi2.0-dev")
    os.system("sudo apt install libatspi2.0-dev -y")
    time.sleep(1)

    print("Installing libgstreamer1.0-0")
    os.system("sudo apt install libgstreamer1.0-0 -y")
    time.sleep(1)

    print("Installing gstreamer1.0-plugins-base")
    os.system("sudo apt install gstreamer1.0-plugins-base -y")
    time.sleep(1)

    print("Installing gstreamer1.0-plugins-good")
    os.system("sudo apt install gstreamer1.0-plugins-good -y")
    time.sleep(1)
 
    print("Installing gstreamer1.0-plugins-bad")
    os.system("sudo apt install gstreamer1.0-plugins-bad -y")
    time.sleep(1)

    print("Installing gstreamer1.0-plugins-ugly")
    os.system("sudo apt install gstreamer1.0-plugins-ugly -y")
    time.sleep(1)

    print("Installing gstreamer1.0-libav")
    os.system("sudo apt install gstreamer1.0-libav -y")
    time.sleep(1)

    print("Installing gstreamer1.0-doc")
    os.system("sudo apt install gstreamer1.0-doc -y")
    time.sleep(1)

    print("Installing gstreamer1.0-tools")
    os.system("sudo apt install gstreamer1.0-tools -y")
    time.sleep(1)

    print("Installing gstreamer1.0-x")
    os.system("sudo apt install gstreamer1.0-x -y")
    time.sleep(1)

    print("Installing gstreamer1.0-alsa")
    os.system("sudo apt install gstreamer1.0-alsa -y")
    time.sleep(1)

    print("Installing gstreamer1.0-gl")
    os.system("sudo apt install gstreamer1.0-gl -y")
    time.sleep(1)

    print("Installing gstreamer1.0-gtk3")
    os.system("sudo apt install gstreamer1.0-gtk3 -y")
    time.sleep(1)

    print("Installing gstreamer1.0-qt5")
    os.system("sudo apt install gstreamer1.0-qt5 -y")
    time.sleep(1)

    print("Installing gstreamer1.0-pulseaudio")
    os.system("sudo apt install gstreamer1.0-pulseaudio -y")
    time.sleep(1)

    print("Installing flite1-dev")
    os.system("sudo apt instal flite1-dev -y")
    time.sleep(1)

    print("Installing libspeechd-dev")
    os.system("sudo apt install libspeechd-dev -y")
    time.sleep(1)

    print("Installing speech-dispatcher")
    os.system("sudo apt install speech-dispatcher -y")
    time.sleep(1)

    print("Installing flex")
    os.system("sudo apt install flex -y")
    time.sleep(1)

    print("Installing Gperf")
    os.system("sudo apt install gperf -y")
    time.sleep(1)

    print("Installing npm and nodejs")
    os.system("sudo apt install nodejs -y")
    os.system("sudo apt install npm -y")
    time.sleep(1)

    print("Installing FontConfig")
    os.system("sudo apt install fontconfig -y")
    time.sleep(1)

    print("Installing x11-xserver-utils")
    os.system("sudo apt install x11-xserver-utils -y")
    time.sleep(1)

while True:
    print("Do you wish to update system? or start download files")
    ans = input("Yes or No: ")

    if ans == 'yes' or ans == 'Yes':
        print("Begin Updates")
        time.sleep(1)
        while True:
            print("May Need authorization! Enter password if promted.")
            os.system("sudo apt update")
            time.sleep(2)
            option = input("Check for Upgrades? - ")
            if option == 'yes' or option == 'Yes':
                os.system("sudo apt full-upgrade -y")
                time.sleep(2)
                break

            elif option == 'no' or option == 'No':
                print("Continue without checking for upgrades..")
        break    
        download()
        

    elif ans == 'no' or ans == 'No':
        while True:
            print("Begin Direct Install")
            download()
            break

    else:
        print("Restarting script. Choose option from below.")
        time.sleep(3)

