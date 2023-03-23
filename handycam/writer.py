import numpy as np
import cv2


class VideoWriter:
    def __init__(self, *args, **kwargs):
        self.writer = cv2.VideoWriter(*args, **kwargs)
    
    def __enter__(self) -> "VideoWriter":
        return self
    
    def __exit__(self, type, value, traceback):
        self.writer.release()

    def __del__(self):
        if self.writer.isOpened():
            self.release()

    def release(self):
        self.writer.release()

    def write(self, frame: np.ndarray):
        self.writer.write(frame)
