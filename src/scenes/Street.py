# -*- coding: utf-8 -*-
'''
Stage: "stage name"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def goto_his_office(w: World):
    return w.scene('お弁当を届けに',
            w.change_stage("Street"),
            )

