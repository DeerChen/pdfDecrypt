# -*- mode: python ; coding: utf-8 -*-

block_cipher = pyi_crypto.PyiBlockCipher(key='pdfDecrypt')


a = Analysis(['main.py'],
             pathex=['C:\\Users\\千北\\Desktop\\pdfDecrypt'],
             binaries=[],
             datas=[
                ('assets', 'assets'),
                ('lib', 'lib'),
                ('bin', 'bin'),
                ('include', 'include')
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=True,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='解锁pdf',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=['vcruntime140.dll'],
          runtime_tmpdir=None,
          console=False , icon='assets\\pdf.ico')
