import cv2


class VideoWriter(cv2.VideoWriter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __enter__(self) -> "HandyVideoWriter":
        return self
    
    def __exit__(self, type, value, traceback):
        self.release()
