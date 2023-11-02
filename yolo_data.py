import math
import time

class Move:
    def __init__(self,Yolo):
        self.before_arr=[]
        self.after_arr=[]
        self.tracking=None
        self.tracking_scooter=[]
        self.yolo=Yolo
        
    def move_scooter(self):
        while 1:
            self.set_af_arr(self.yolo.get_arr())
          
            af_arr=self.after_arr
            if self.tracking!=None:
                for kb_ax,kb_ay,kb_ah,ids in af_arr[1]: 
                    if self.tracking==ids:
                        self.tracking_scooter=[kb_ax,kb_ay,kb_aids,kb_ah]
                        continue
            for kb_ax,kb_ay,kb_ah,kb_aids in af_arr[1]:
                for kb_bx, kb_by,kb_bh,kb_bids in self.be_arr[1]:
                    if kb_aids==kb_bids:
                        dis_kb=math.sqrt((kb_ax-kb_bx)**2+(kb_ay-kb_by)**2) 
                        if dis_kb>kb_ah/100:
                            if self.move_person(af_arr,dis_kb):
                                self.tracking=kb_aids 
                                self.tracking_scooter=[kb_ax,kb_ay,kb_aids,kb_ah]
                                
            self.before_arr=af_arr
    
    def move_person(self,af_arr,dis_kb):
    
        for pe_ax,pe_ay,pe_ah,pe_aids in af_arr[3]:
            for pe_bx,pe_by,pe_bh,pe_bids in self.be_arr[3]:
                if pe_aids==pe_bids:
                    dis_pe=math.sqrt((pe_ax-pe_bx)**2+(pe_ay-pe_by)**2)
                    if dis_kb*0.7<dis_pe and dis_pe<dis_kb*1.3:
                        for he_ax,he_ay,he_ah,he_aids in af_arr[2]:
                            for he_bx,he_by,he_bh,he_bids in self.be_arr[2]:
                                if he_aids==he_bids:
                                    dis_he=math.sqrt((he_ax-he_bx)**2+(he_ay-he_by)**2)
                                    if dis_kb*0.7<dis_he and dis_he<dis_kb*1.3:
                                        return True   
        return False         
                
    def set_af_arr(self,data):
        self.after_arr=data

    def get_tracking_scooter(self):
        return self.tracking_scooter