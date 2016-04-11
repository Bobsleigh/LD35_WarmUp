# -*- mode: python -*-

block_cipher = None

addedFiles = [ ('tiles', 'tiles'), ('sample','sample'), ('img', 'img'), ('fonts', 'fonts'), ('menu/sound', 'menu/sound') ]

a = Analysis(['main.py'],
             pathex=['C:\\Users\\Bobsleigh\\Documents\\PythonProjects\\LD35_WarmUp'],
             binaries=None,
             datas=addedFiles,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=False )
