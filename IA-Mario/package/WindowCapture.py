# Library: pywin32
import win32ui
import win32gui
import win32con
import numpy as np

class WindowCapture:

    # Properties
    width = 0
    height = 0
    screen = None
    offset_x = 0
    offset_y = 0

    # Constructor
    def __init__(self, window_name=None, border_pixels=8, titlebar_pixels=30, downbar_pixels=0):
        # find the handle for the window we want to capture.
        # if no window name is given, capture the entire screen
        if window_name is None:
            self.screen = win32gui.GetDesktopWindow()
        else:
            self.screen = win32gui.FindWindow(None, window_name)
            if not self.screen:
                raise Exception('Window not found {}'.format(window_name))

        # get the window size
        window_rect = win32gui.GetWindowRect(self.screen)
        self.width = window_rect[2] - window_rect[0] # 1920
        self.height = window_rect[3] - window_rect[1] # 1080

        # account for the window border and titlebar and cut them off
        self.width = self.width - (border_pixels * 2)
        self.height = self.height - titlebar_pixels - downbar_pixels
        self.offset_x = border_pixels
        self.offset_y = titlebar_pixels

    def get_screenshot(self):

        #get the window image data
        wdc = win32gui.GetWindowDC(self.screen)
        dcobj = win32ui.CreateDCFromHandle(wdc)
        cdc = dcobj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcobj, self.width, self.height)
        cdc.SelectObject(dataBitMap)
        cdc.BitBlt((0, 0), (self.width, self.height), dcobj, (self.offset_x, self.offset_y), win32con.SRCCOPY)

        # convert the raw data into a format opencv can read
        # dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
        signedIntArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntArray, dtype='uint8')
        img.shape = (self.height, self.width, 4)

        # Free Resources
        dcobj.DeleteDC()
        cdc.DeleteDC()
        win32gui.ReleaseDC(self.screen, wdc)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        # drop the alpha channel, or cv.matchTemplate() will throw an error like:
        #   error: (-215:Assertion failed) (depth == CV_8U || depth == CV_32F) && type == _templ.type()
        #   && _img.dims() <= 2 in function 'cv::matchTemplate'
        img = img[..., :3]

        # make image C_CONTIGUOUS to avoid errors that look like:
        #   File ... in draw_rectangles
        #   TypeError: an integer is required (got type tuple)
        # see the discussion here:
        # https://github.com/opencv/opencv/issues/14866#issuecomment-580207109
        img = np.ascontiguousarray(img)

        return img

    # find the name of the window you're interested in.
    # once you have it, update window_capture()
    # https://stackoverflow.com/questions/55547940/how-to-get-a-list-of-the-name-of-every-open-window
    @staticmethod
    def list_window_names():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)

    @staticmethod
    def getHwnd(window_name):
        thelist = []
        def findit(hwnd, ctx):
            if win32gui.GetWindowText(hwnd) == window_name:  # check the title
                thelist.append(hwnd)

        win32gui.EnumWindows(findit, None)
        return thelist
