import cv2
import click
from capture import VideoCapture
from writer import VideoWriter


@click.group()
def main():
    pass


@main.command()
@click.argument("src")
@click.option("-v", "--is_video", "is_video", is_flag=True)
@click.option("-n", "--window_name", "window_name", default="frame")
@click.option("-s", "--skip_size", "skip_size", type=int, default=1)
def imshow(src, is_video, window_name, skip_size):
    if not is_video:
        try:
            src = int(src)
        except:
            print("Invalid web camera's source number")
            return

    with VideoCapture(src, is_video=is_video, skip_size=skip_size) as cap, \
         VideoWriter("out.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (1280, 720)) as writer:
        if not cap.isOpened():
            print(f"Capture was not opened (src: {src})")
            return

        print("Please press q when you want to quit showing frames")
        while True:
            ret, frame = cap.read()
            if not ret:
                cv2.destroyWindow(window_name)
                break

            writer.write(frame)

            cv2.imshow(window_name, frame)

            if cv2.waitKey(20) == ord("q"):
                cv2.destroyWindow(window_name)
                break


if __name__ == "__main__":
    main()
