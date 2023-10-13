from ultralytics import YOLO
import os
import cv2
import time


class Detect:
    def __init__(self):
        self.path=os.path.dirname(__file__)
        self.path=self.path+''
        os.chdir(self.path)
        self.arr=[[],[],[],[]]
        self.model = YOLO("train8.onnx")
        self.cap=None
        
    def video_stream(self,video):
        self.cap=video
        
    def detect(self):
        while self.cap==None:
            time.sleep(0.1)
        num=0
        while 1:
            success, frame = self.cap.read()
            num=(num+1)%4
            if success and num==0:
                arr_re=[[],[],[],[]]
                result = self.model.track(frame,persist=True,iou=0.5,imgsz=800,agnostic_nms=True)
                plot=result[0].plot()
                
                for box in result[0].boxes:
                    if result[0].boxes.id!=None:
                        ids=box.id.int().cpu().tolist()
                        num=box.cls[0].cpu().detach().numpy().tolist()
                        box=box.xywh
                        x=box[0][0].cpu().detach().numpy().tolist()
                        y=box[0][1].cpu().detach().numpy().tolist()
                        w=box[0][2].cpu().detach().numpy().tolist()
                        line = [x,y,w,ids]
                        if num==0:
                            arr_re[0].append(line)
                        elif num==1:
                            arr_re[1].append(line)
                        elif num==2:
                            arr_re[2].append(line)
                        elif num==3:
                            arr_re[3].append(line)
                
                self.arr=arr_re
                frame=cv2.resize(plot,(0,0),fx=0.7,fy=0.7,interpolation=cv2.INTER_LINEAR)
                cv2.imshow("Video", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
                
                
                
    def get_arr(self):
        
        return self.arr