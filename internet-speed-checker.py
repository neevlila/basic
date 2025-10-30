# pip install speedtest-cli

import speedtest

def bytes_to_mb(bytes):
    KB = 1024
    MB = KB * 1024
    return int(bytes / MB)

st = speedtest.Speedtest()

start = input('Press enter to Start')
down_speed = str(bytes_to_mb(st.download()))
up_speed = str(bytes_to_mb(st.upload()))
ping = st.results.ping

print(down_speed + 'mb/s')
print(up_speed + 'mb/s')
print(ping)
