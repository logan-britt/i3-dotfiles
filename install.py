import os
import shutil
import platform

# stop the script from running on anything but linux
if not platform.system() == 'Linux':
    raise RuntimeError('This operating system is not supported.')

# create all the paths possible that we might need.
home_path = str(os.path.expanduser('~'))
config_folder_path = str(os.path.join(home_path, '.config'))
i3_folder_path = str(os.path.join(config_folder_path, 'i3'))
config_file_path = str(os.path.join(i3_folder_path, 'config'))

# get the text of the config file of i3-gaps
i3_config_text = []
with open('i3-config.txt', 'r') as config_file:
    for line in config_file:
        i3_config_text.append(line)

i3_config_string = ''
for line in i3_config_text:
    config_string += line

# move the i3 config file into its folder or create the folder and move the file
if '.config' in os.listdir(home_path):
    if 'i3' in os.listdir(config_folder_path):
        with open(config_file_path, 'w') as config_file:
            config_file.write(config_string)

    else:
        os.mkdir(i3_folder_path)
        with open(config_file_path, 'w') as config_file:
            config_file.write(config_string)

else:
    os.mkdir(config_folder_path)
    os.mkdir(i3_folder_path)
    with open(config_file_path, 'w') as config_file:
        config_file.write(config_string)

# here we get the picom config file and move it into place
picom_config_text = []
with open('picom-config.txt', 'r') as picom_config:
    for line in picom_config:
        picom_config_text.append(line)

picom_config_string = ''
for i in range(len(picom_config_text)):
    picom_config_string += picom_config_text[i]

picom_config_folder_path = str(os.path.join(config_folder_path, 'picom'))
picom_config_file_path = str(
        os.path.join(picom_config_folder_path, 'picom.conf'))

if 'picom' in os.listdir(config_folder_path):
    with open(picom_config_file_path, 'w') as picom_config:
        picom_config.write(picom_config_string)

else:
    os.mkdir(picom_config_folder_path)
    with open(picom_config_file_path, 'w') as picom_config:
        picom_config.write(picom_config_text)

# here we get the polybar config text and move it into its folder
polybar_config_path = os.path.join(config_folder_path, 'polybar')

polybar_start_path = os.path.join(polybar_config_path, 'start.sh')
polybar_config_path = os.path.join(polybar_config_path, 'config')

if 'polybar' in os.listdir(config_folder_path):
    shutil.move('polybar-config.txt', polybar_config_path)
    shutil.move('polybar-launch.sh', polybar_start_path)

else:
    os.mkdir(polybar_config_path)

    shutil.move('polybar-config.txt', polybar_config_path)
    shutil.move('polybar-launch.sh', polybar_start_path)

# create the folder and move a background image
os.mkdir('/wallpapers')
os.mkdir('/wallpapers/sfw')
os.mkdir('wallpapers/nsfw')

shutil.copy('base.png', '/wallpapers/sfw/base.png')
