import time
import threading
import yolo_data
import yolo_predict
import tello
import track
import multiprocessing
from multiprocessing import Pipe

Tello=tello.tello()
predict=yolo_predict.Detect(Tello)
data=yolo_data.Move(predict)
Track=track.tracking(Tello)

def thread_yolo_data():
    data.move_scooter()
def process_yolo_predict():
    predict.detect()

if __name__ == '__main__':
    
    pipe=Pipe()
    
    data_thread=threading.Thread(target=thread_yolo_data)
    data_thread.daemon=True
    data_thread.start()

    predict_process=multiprocessing.Process(target=process_yolo_predict,daemon=True)
    predict_process.start()

   
    while 1:
        Track.tracking(data.get_tracking_scooter())
        time.sleep(0.3)
    
    