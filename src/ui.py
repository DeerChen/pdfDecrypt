'''
@Description: 
@Author: Senkita
@Date: 2020-06-10 13:53:22
@LastEditors: Senkita
@LastEditTime: 2020-06-10 15:30:43
'''
import PySimpleGUI as sg
from pathlib import Path
from src.utils import resource_path


class UserInterface:

    def warningPopup(self, cueWord):
        '''
        @description: 警告框
        @param {str}
        @return: {function}
        @author: Senkita
        '''
        warningPopup = sg.Popup('警告!', cueWord, icon=resource_path(
            Path('assets').joinpath('pdf.ico')))
        if warningPopup in (None, 'OK'):
            return self.userInterface()

    def userInterface(self):
        '''
        @description: 文件选择界面
        @param {type}
        @return: {str}
        @author: Senkita
        '''
        layout = [
            [sg.T('待解锁pdf文件路径:')],
            [
                sg.I(
                    size=(40, None),
                    disabled=True
                ),
                sg.FileBrowse(
                    button_text='打开',
                    file_types=(('pdf文件', '*.pdf'),)
                )
            ],
            [sg.Submit('确定'), sg.Cancel('取消')]
        ]
        window = sg.Window('解锁pdf', layout)
        window.SetIcon(icon=resource_path(
            Path('assets').joinpath('pdf.ico')))
        event, value = window.Read()
        if event == '确定':
            window.Close()
            if '' == value[0]:
                self.warningPopup('存在漏填项!')
            else:
                return value[0]
        elif event in (None, '取消'):
            window.Close()
