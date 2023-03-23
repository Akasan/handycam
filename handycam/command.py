import os
import cv2
import click
from capture import VideoCapture
from writer import VideoWriter


@click.group()
def main():
    pass


FOURCC = {
    "mp4": "mp4v"
}


def get_ext(filename) -> str:
    return os.path.basename(filename).split(".")[-1]


@main.command()
@click.argument("src")
@click.option("-v", "--is_video", "is_video", is_flag=True)
@click.option("-s", "--step_size", "step_size", type=int, default=1)
@click.option("-w", "--write", "is_write", is_flag=True)
@click.option("-o", "--out_filename", "out_filename", default="out.mp4")
@click.option("-f", "--fps", "fps", type=int, default=30)
@click.option("-W", "--width", "width", type=int, default=-1)
@click.option("-H", "--height", "height", type=int, default=-1)
def imshow(src, is_video, step_size, is_write, out_filename, fps, width, height):
    if not is_video:
        try:
            src = int(src)
        except:
            print("Invalid web camera's source number")
            return

    with VideoCapture(src, is_video=is_video, step_size=step_size) as cap:
        is_resize = False
        out_size = [cap.WIDTH, cap.HEIGHT]

        if not width == -1:
            out_size[0] = width
            is_resize = True
        if not height == -1:
            out_size[1] = height
            is_resize = True

        out_size = tuple(out_size)

        if is_write:
            fourcc = FOURCC[get_ext(out_filename)]
            writer = VideoWriter(
                out_filename, 
                cv2.VideoWriter_fourcc(*fourcc), 
                fps, 
                out_size
            )
        else:
            writer = None

        if not cap.isOpened():
            print(f"Capture was not opened (src: {src})")
            return

        print("Please press q when you want to quit showing frames")
        while True:
            ret, frame = cap.read()
            if not ret:
                cv2.destroyWindow(window_name)
                break

            cv2.imshow(window_name, frame)

            if not writer is None:
                if is_resize:
                    frame = cv2.resize(frame, out_size)
                    
                writer.write(frame)

            if cv2.waitKey(20) == ord("q"):
                cv2.destroyWindow("frame")
                break

        if not writer is None:
            writer.release()


if __name__ == "__main__":
    main()
