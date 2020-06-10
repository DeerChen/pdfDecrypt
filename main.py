'''
@Description: 
@Author: Senkita
@Date: 2020-06-08 19:16:06
@LastEditors: Senkita
@LastEditTime: 2020-06-10 15:31:47
'''
from src.ui import UserInterface
from src.bgProcessing import BackgroundProcessing
import sys


def main():
    '''
    @description:
    # * 读取待解锁pdf文件位置
    # * 读取qpdf程序位置
    # * 操作Shell解锁pdf
    @param {type} 
    @return: 
    @author: Senkita
    '''
    try:
        filePath = UserInterface().userInterface()
        bgp = BackgroundProcessing(filePath)
        bgp.pdfDecrypt()
    except:
        sys.exit(0)


if __name__ == "__main__":
    main()
