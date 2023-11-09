import socket
import cv2

class tello:
    def __init__(self):
        """
        self.land=False
        self.socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(("0.0.0.0",8889))
        self.tello_address = ("192.168.10.1", 8889)
        self.local_video_port = 11111
        self.socket.sendto('command'.encode('utf-8'),self.tello_address)
        self.socket.sendto('streamon'.encode('utf-8'),self.tello_address)
        """
        self.video=cv2.VideoCapture("test2.mp4")
        #self.video=cv2.VideoCapture("udp://@0.0.0.0:11111")

    def send_data(self,msg):
        self.abort_flag = False
        self.socket.sendto(msg.encode('utf-8'), self.tello_address)       
        
    def get_cv2_size(self):
        cv2_size=[self.video.get(cv2.CAP_PROP_FRAME_WIDTH),self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)]
        return cv2_size
    