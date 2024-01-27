import time

import win32api
import win32con
import win32gui
import win32ui
from PIL import Image


def screenshot(file_path='screenshot.png'):
    # grab a handle to the main desktop window
    hdesktop = win32gui.GetDesktopWindow()

    # determine the size of all monitors in pixels
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    # create a device context
    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)

    # create a memory based device context
    mem_dc = img_dc.CreateCompatibleDC()

    # create a bitmap object
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)

    # copy the screen into our memory device context
    mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)

    # convert the raw data into a format that PIL can use
    bmpinfo = screenshot.GetInfo()
    bmpstr = screenshot.GetBitmapBits(True)

    # create an image object
    img = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    # save the image
    img.save(file_path)

    # free resources
    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())


if __name__ == '__main__':
    screenshot('screenshot.png')
    print("Screenshot saved as 'screenshot.png'")
    time.sleep(2)
