from ultralytics import YOLO
import os
import cv2

class Detect:
    def __init__(self,tello):
        self.path=os.path.dirname(__file__)
        self.path=self.path+''
        os.chdir(self.path)
        self.model = YOLO("train8.onnx",task='detect')
        self.cap=tello.video
        
    def detect(self,c_pipe):
        while 1:
            #total_frame=int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
            #self.cap.set(cv2.CAP_PROP_POS_FRAMES, total_frame-1)
            success, frame = self.cap.read()
            if success:
                arr_re=[[],[],[],[]]
                result = self.model.track(frame,persist=True,iou=0.5,imgsz=800,agnostic_nms=True,verbose=False)
                plot=result[0].plot()
                for box in result[0].boxes:
                    if result[0].boxes.id!=None:
                        ids=box.id.int().cpu().tolist()
                        num=box.cls[0].cpu().detach().numpy().tolist()
                        box=box.xywh
                        x=box[0][0].cpu().detach().numpy().tolist()
                        y=box[0][1].cpu().detach().numpy().tolist()
                        h=box[0][3].cpu().detach().numpy().tolist()
                        line = [x,y,h,ids]
                        if num==0:
                            arr_re[0].append(line)
                        elif num==1:
                            arr_re[1].append(line)
                        elif num==2:
                            arr_re[2].append(line)
                        elif num==3:
                            arr_re[3].append(line)
                c_pipe.send(arr_re)
                frame=cv2.resize(plot,(0,0),fx=0.7,fy=0.7,interpolation=cv2.INTER_LINEAR)
                cv2.imshow("Video", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            