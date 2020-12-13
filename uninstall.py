import os
import shutil

config_path = str(os.path.join(
    os.path.expanduser('~'),
    '.config'
))

config_list = os.listdir(config_path)
if 'i3' in config_path:
    i3_path = os.path.join(config_path, 'i3')
    shutil.rmtree(i3_path)

if 'picom' in config_path:
    picom_path = os.path.join(config_path, 'picom')
    shutil.rmtree(picom_path)

if 'polybar' in config_path:
    polybar_path = os.path.join(config_path, 'polybar')
    shutil.rmtree(polybar_path)
