<!--
 * @Description: 
 * @Author: Senkita
 * @Date: 2020-06-10 15:58:34
 * @LastEditors: Senkita
 * @LastEditTime: 2020-06-10 16:02:06
--> 
# pdfDecrypt
给qpdf套个GUI
## 生成exe
```shell
pyinstaller.exe -F -w -i .\assets\pdf.ico -n 解锁pdf --key pdfDecrypt --upx-dir .\upx394w\ --upx-exclude vcruntime140.dll --clean --win-private-assemblies .\main.py

pyinstaller.exe -F .\解锁pdf.spec --upx-dir .\upx394w\
```