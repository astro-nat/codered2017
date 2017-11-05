from flask import Flask, render_template

import serial
import numpy as np
import matplotlib.pyplot as plt

import socket
import sys

app = Flask(__name__)

@app.route("/")
def main():

    # HOST = '172.25.29.21'   # Symbolic name, meaning all available interfaces
#     PORT = 8888 # Arbitrary non-privileged port
#  
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print 'Socket created'
#  
#     #Bind socket to local host and port
#     try:
#         s.bind((HOST, PORT))
#     except socket.error as msg:
#         print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
#         sys.exit()
#      
#     print 'Socket bind complete'
#  
#     #Start listening on socket
#     s.listen(10)
#     print 'Socket now listening'
#  
#     #now keep talking with the client
#     while 1:
#         #wait to accept a connection - blocking call
#         conn, addr = s.accept()
#         print 'Connected with ' + addr[0] + ':' + str(addr[1])
#         
#         (data,addr) = mySocket.recvfrom(SIZE)
#     	print data
#      
#     s.close()
            
    return render_template('index.html')
    
#    ser = serial.Serial('/dev/cu.usbmodem1451', baudrate = 115200)
#
#    y1 = [1,2,3,4]
#    x1 = [1,2,3,4];
#    x2 = [5,3,6,7];
#    x3 = [2,6,10,11];
#    x4 = [5,6,7,8];
#    x5 = [1,2,3,4];
#
#    plt.ion()
#
#    ydata = [0] * 50
#    ax1=plt.axes()
#
#    # make plot
#    line, = plt.plot(ydata)
#    plt.ylim([10,40]) # set the y-range to 10 to 40
#
#    # start data collection
#    while True:
#        data = ser.readline().rstrip() # read data from serial
#        # port and strip line endings
#        if len(data.split(".")) == 2:
#            ymin = float(min(ydata))-10
#            ymax = float(max(ydata))+10
#            plt.ylim([ymin,ymax])
#            ydata.append(data)
#            del ydata[0]
#            line.set_xdata(np.arange(len(ydata)))
#            line.set_ydata(ydata)  # update the data
#            plt.draw() # update the plot
#
#    #    plt.plot(x1,y1,'ro',x2,y1,x3,y1,x4,y1,x5,y1);
#    #    plt.ylabel('Graph 1')
#    #    plt.show()

if __name__ == "__main__":
    app.run()

@app.route('/templates/')
def tutorial():
    return render_template('tutorial_a.html')
	
			

  
