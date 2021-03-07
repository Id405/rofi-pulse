#!/usr/bin/python
import pulsectl
import sys
from rofi import Rofi

# Get list of sink inputs with names of the client they belong to
# Using client names are more descriptive than sink input names but some still suck (like WebRTC client for discord)

clients = []

inputs = []
input_names = []
input_clients = []

with pulsectl.Pulse('control-menu') as pulse:
    for client in pulse.client_list():
        clients.append(client)

    for input in pulse.sink_input_list():
        inputs.append(input)

        client = [client for client in clients if client.index == input.client][0]

        input_names.append(client.name)
        input_clients.append(client)


# Initialize rofi and then pop up menus for selecting sink input from list and actions to perform on sink inputs
# TODO add sources into this list so mic levels can be easily controlled aswell

r = Rofi()

while True:
    input_index, input_name = r.select('Select an input', input_names, message="input name...")

    if input_index == -1:
        sys.exit()

    input = inputs[input_index]
    input_client = input_clients[input_index]
    input_name = input_client.name

    with pulsectl.Pulse('control-menu') as pulse:
        old_action = 0
        while True:
            volume = input.volume.value_flat
            volume = "{:1.2f}".format(volume).replace('.', '').lstrip('0') # This is a terrible way to format the percent into a string but ¯\_(ツ)_/¯
            
            muted = ""
            if input.mute == 1:
                muted = "[muted]"

            # 0 == raise volume, 1 == lower volume, 2 == mute, 3 == back
            action, name = r.select(f'{input_name} {volume:2s}% {muted}', ['raise volume', 'lower volume', 'mute', 'back'], message="action...", select=old_action)

            # Whats a switch statement?
            if action == -1:
                sys.exit()
            if action == 0:
                pulse.volume_change_all_chans(input, 0.05)
            if action == 1:
                pulse.volume_change_all_chans(input, -0.05)
            if action == 2:
                if input.mute != 1:
                    pulse.mute(input)
                else:
                    pulse.mute(input, 0)
            if action == 3:
                break
            
            old_action = action
