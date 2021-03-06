# Imports
import psutil
import platform
from flask import Flask, render_template, url_for, send_from_directory
import threading

# Operating System
os = platform.system()
release = platform.release()

# Hostname
hostname = platform.node()

# Memory Variables
virtual = psutil.virtual_memory()
memory = str(float(virtual.percent)) + '%'
memoryp = str(float(virtual.percent))

# CPU Variables
cpu = psutil
percent = cpu.cpu_percent()
processor = str(round(percent)) + '%'

# Flask
app = Flask(__name__)

@app.route('/')
def site():
  return render_template('return.html', os=os, release=release, memoryp=memoryp, memory=memory, host=hostname, processor=processor)

if __name__ == '__main__':
  app.run(port=9111)
