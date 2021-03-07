# Control PulseAudio with rofi

This is a simple python script to control PulseAudio sink input volumes using rofi. This is useful for people using a tiling window manager with rofi as their application launcher/window switcher/whatever else.

### Images

![](images/main.png)
![](images/menu.png)

### Installation

```
pip install rofi-pulse
```

then the menu can be launched with `rofi_pulse`

example sxhkd entry
```
# Volume control menu
super + q
	~/.local/bin/rofi_pulse
```

