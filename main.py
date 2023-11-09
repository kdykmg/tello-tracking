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
data=yolo_data.Move()
Track=track.tracking(Tello)

def thread_yolo_data(p_pipe):
    data.move_scooter(p_pipe)
def process_yolo_predict(c_pipe):
    predict.detect(c_pipe)

if __name__ == '__main__':
    p_pipe,c_pipe=Pipe() 
    predict_process=multiprocessing.Process(target=process_yolo_predict,args=(c_pipe,),daemon=True)
    predict_process.start()
    data_thread=threading.Thread(target=thread_yolo_data,args=(p_pipe,))
    data_thread.daemon=True
    data_thread.start()
    while 1:
        Track.tracking(data.get_tracking_scooter())
        time.sleep(0.1)
    