from typing import Tuple
from typing import Iterator
import numpy as np
import cv2


class VideoCapture:
    def __init__(self, src, *args, **kwargs):
        self.cap = cv2.VideoCapture(src)
        self.current_position = 0
        self.skip_size = kwargs.get("skip_size", 1)
        self.is_video = kwargs.get("is_video", False)

    def get(self, *args, **kwargs):
        return self.cap.get(*args, **kwargs)

    def set(self, *args, **kwargs):
        self.cap.set(*args, **kwargs)

    def _increment_position(self):
        if self.is_video:
            self.current_position += self.skip_size
            self.set(cv2.CAP_PROP_POS_FRAMES, self.current_position)

    def read(self) -> Tuple[bool, np.ndarray]:
        self._increment_position()
        return self.cap.read()

    def __enter__(self) -> "VideoCapture":
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cap.release()

    @property
    def FRAME_COUNT(self) -> int:
        return int(self.get(cv2.CAP_PROP_FRAME_COUNT))

    @property
    def FPS(self) -> int:
        return int(self.get(cv2.CAP_PROP_FPS))

    @property
    def WIDTH(self) -> int:
        return int(self.get(cv2.CAP_PROP_FRAME_WIDTH))

    @property
    def HEIGHT(self) -> int:
        return int(self.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def __len__(self) -> int:
        return self.FRAME_COUNT

    def isOpened(self) -> bool:
        return self.cap.isOpened()
