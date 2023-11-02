import math

class tracking:
    def __init__(self,tello):
        self.land=True
        self.tello=tello
        self.vid_size=tello.get_cv2_size()
        self.weight=self.vid_size[0]
        self.height=self.vid_size[1]
        self.middle=self.weight/2
        self.stand_tello_height=2
        self.stand_scooter_height=1
        self.stand_scooter_weight=1
        self.stand_distance=3
        self.real_distance=0.879*self.stand_distance/self.middle
        self.cross_scooter=math.sqrt(self.stand_scooter_height**2+self.stand_scooter_weight**2)
        self.croos_distance=math.sqrt((self.stand_tello_height-self.stand_scooter_height)**2+self.stand_distance**2)
        
        self.distsnce=self.cross_scooter/(((self.stand_tello_height-self.stand_scooter_height)/self.croos_distance)*self.stand_scooter_height/self.cross_scooter+self.stand_distance/self.croos_distance*self.stand_scooter_weight/self.cross_scooter)/self.stand_distance
        
        
    def tracking(self,scooter):
        
        if scooter==[]:
            return
        print(scooter[0])
        """
        x=scooter[0]
        y=scooter[1]
        h=scooter[3]
        
        h=h*self.real_distance
        dis=h*self.distsnce-self.stand_scooter_weight/2  
        if dis<self.stand_distance:
             self.tello.send_data("stop")
             return
        set_speed=int(100-100*self.stand_distance/dis)
        if self.land:
            self.tello.send_data("takeoff")
        if x/self.middle>1.1:
            self.tello.send_data("ccw 10")
        elif x/self.middle<0.9:
            self.tello.send_data("cw 10")
            
        self.tello.send_data("speed %f" %set_speed)
    
    
    def set_scooter(self,Scooter):
        self.scooter=Scooter
        """