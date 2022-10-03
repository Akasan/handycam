from typing import Iterator
import numpy as np
import cv2


class VideoCapture(cv2.VideoCapture):
    """HandyVideoCapture is a wrapper for cv2.VideoCapture.
    This class was made to make cv2.VideoCapture more handy.

    Examples:
        >>> with HandyVideoCapture(0) as cap:
        ...     for frame in cap.reads():
        ...         pass
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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

    def __enter__(self) -> "HandyVideoCapture":
        return self

    def __exit__(self, type, value, traceback):
        self.release()

    def reads(self, step_size: int = 1) -> Iterator[np.ndarray]:
        i = 0

        while True:
            ret, frame = self.read()

            i += 1
            if not (i-1) % step_size == 0:
                continue

            if not ret:
                break

            yield frame

    def __del__(self):
        self.release()
