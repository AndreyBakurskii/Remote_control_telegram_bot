import pyautogui as pag


def right(n=1):
    """
    press right n times
    :param n: amount times
    :return: None
    """
    for i in range(n):
        pag.press('right')


def left(n=1):
    """
    press left n times
    :param n: amount times
    :return: None
    """
    for i in range(n):
        pag.press('left')


def space():
    """
    press space
    :return: None
    """
    pag.press('space')


def volume_up(n=1):
    """
    increase the sound n times
    :param n: amount times
    :return: None
    """
    for i in range(n):
        pag.press('volumeup')


def volume_mute():
    """
    mute sound
    :return: None
    """
    pag.press('volumemute')


def volume_down(n=1):
    """
    drop the sound n times
    :param n: amount time
    :return: None
    """
    for i in range(n):
        pag.press('volumedown')

# command to turn off your computer
# def turn_off():
#     os.system("shutdown /s /t 60")
