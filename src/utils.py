'''
@Description: 
@Author: Senkita
@Date: 2020-06-10 14:01:12
@LastEditors: Senkita
@LastEditTime: 2020-06-10 14:42:30
'''
from pathlib import Path
import sys


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = Path(".").resolve()
    return Path(base_path).joinpath(relative_path)
