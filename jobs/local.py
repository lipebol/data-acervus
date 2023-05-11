#!/usr/bin/python3

import os
import json
import textwrap

def local():
    wrapper = textwrap.TextWrapper(width=70)
    directory = os.path.expanduser('~/config_Conky/Scripts/jobs')
    file = open(f'{directory}/local.json')
    item = json.load(file)
    i0 = wrapper.fill(text=item["vagas"][0])
    i1 = wrapper.fill(text=item["vagas"][1])
    i2 = wrapper.fill(text=item["vagas"][2])
    print("\n" + i0)
    print("\n" + i1)
    print("\n" + i2)

local()