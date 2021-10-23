# -*- mode: python ; coding: utf-8 -*-
import site
site_pkgs = site.getsitepackages()[0]

block_cipher = None

a = Analysis(['parquet_table/__main__.py'],
             pathex=['parquet_table'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += Tree("data",prefix="data")
a.datas += Tree(f"{site_pkgs}/dash_core_components", prefix="dash_core_components")
a.datas += Tree(f"{site_pkgs}/dash_html_components", prefix="dash_html_components")
a.datas += Tree(f"{site_pkgs}/dash_renderer", prefix="dash_renderer")

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='__main__',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='__main__')
