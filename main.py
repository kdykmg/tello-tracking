import time
import threading
import yolo_data
import yolo_predict
import tello

data=yolo_data.Move()
predict=yolo_predict.Detect()
Tello=tello.tello()
data_arr=[]

def thread_video_stream():
    tello.vid(predict)
def thread_yolo_data():
    data.move_scooter()
def thread_yolo_predict():
    predict.detect()
def thread_data():
    data_arr=predict.get_arr()
    data.set_af_arr(data_arr)
    time.sleep(0.2)
    
data_thread=threading.Thread(target=thread_yolo_data)
data_thread.daemon=True
data_thread.start()

predict_thread=threading.Thread(target=thread_yolo_predict)
predict_thread.daemon=True
predict_thread.start()

while 1:
    tracking,scooter=data.get_tracking_scooter()
    if tracking!=None:
        print(scooter)
        
    