# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['run_django.py'],
    pathex=['D:\\Sonata0807'],
    binaries=[
        ('D:\\Sonata0807\\python312.dll', '.'),
    ],
    datas=[
        ('D:\\Sonata0807\\product_tracking\\templates', 'product_tracking\\templates'),
        ('D:\\Sonata0807\\product_tracking\\static', 'product_tracking\\static'),
        ('C:\\Program Files\\Python312\\DLLs', 'DLLs'),
        ('C:\\Program Files\\Python312\\Lib', 'Lib'),
        ('C:\\Program Files\\Python312\\Lib\\site-packages', 'Lib\\site-packages'),
    ],
    hiddenimports=[
        'django',
        'django.contrib.staticfiles',
        'django.core.management',
        'custom_django_command.management.commands.runserver_command',
        'whitenoise',
        'whitenoise.middleware',
        'whitenoise.storage',
        'serial',
        'serial.tools.list_ports'
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='custom_django_command',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='custom_django_command',
)
