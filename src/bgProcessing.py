'''
@Description: 
@Author: Senkita
@Date: 2020-06-10 13:53:22
@LastEditors: Senkita
@LastEditTime: 2020-06-10 15:30:17
'''
import subprocess
from pathlib import Path, PurePosixPath
from src.utils import resource_path


class BackgroundProcessing:
    def __init__(self, filePath):
        self.filePath = filePath
        self.qpdfPath = resource_path(Path('bin').joinpath('qpdf.exe'))

    def pdfDecrypt(self):
        fileName = PurePosixPath(self.filePath).name
        subprocess.call([self.qpdfPath, '--decrypt',
                         self.filePath, fileName], shell=True)
