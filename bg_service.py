import time
import utils


def bg_loop():
    utils.screenshot('screenshot.png')
    time.sleep(10)


if __name__ == '__main__':
    bg_loop()
