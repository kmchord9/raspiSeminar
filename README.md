# raspiSeminar


## kivy環境構築
```
sudo apt update && \
sudo apt install -y libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
   pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   python-setuptools libgstreamer1.0-dev git-core \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} python-dev libmtdev-dev \
   xclip xsel libjpeg-dev && \
python3 -m pip install --upgrade --user pip setuptools && \
python3 -m pip install --upgrade --user Cython==0.29.9 pillow && \
python3 -m pip install --user https://codeload.github.com/kivy/kivy/zip/1.11.1

```


```
git clone https://github.com/kmchord9/raspiSeminar.git
cd raspiSeminar
garden install --app matplotlib
```
