
import webbrowser as wb
import random as r
import time as t

messages = ['Connecting to Servers',
  'Downloading Content',
  'Generating token',
  'Synching Clock',
  'Soldering Circuit Board',
  'Building Virtual Enviroment',
  'Preheating to 325°F',
  'Fetching Data',
  'Programming Cake',
  'Scanning for Bugs',
  'Unbaking Cake',
  'Applying For Harvard',
  'Rejecting Rejection',
  'Doing Lakitu Skip',
  'Generating UUID',
  ]
# roblox.open
done = 0
percent = 0
while done < 15:
    print(f'{messages[done]}... ({percent}%)')
    percent = percent + r.randint(20,30)
    if percent >= 100:
        print(f'{messages[done]}... (100%)')
        done = done + 1
        percent = 0
        t.sleep(1.5)
    t.sleep(1.5)

print('''To verify that you are human,
a test will open in a new window in
your browser in 5 seconds.''')
print(5)
t.sleep(1)
print(4)
t.sleep(1)
print(3)
t.sleep(1)
print(2)
t.sleep(1)
print(1)
t.sleep(1)
print(0)

for joey in range(10):
    wb.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ',1,True) 
