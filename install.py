import os
import sys
import requests

os.system("""
apt update && apt upgrade
pkg update
pkg upgrade
pkg install git
pkg install wget
pkg install pip
pkg install pip2
pkg install python
pkg install python2
pkg install python3
pkg install unzip

pip install V7xStyle
pip install pafy
pip install nexmo
pip install twilio
pip install smtplib
pip install requests
pip install datetime
pip install re
pip install pathlib
pip install youtube_dl
""")

os.system("""
cd
cd RV-TOOL_v4.0
cd .RVFISHING
bash setup
bash tmux_setup
cd
clear
""")
