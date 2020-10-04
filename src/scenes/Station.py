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
def have_a_trouble(w: World):
    sato, ayano = w.get("satomi"), w.get("ayano")
    return w.scene("電車に乗るのも大変で",
            w.change_stage("Station"),
            sato.come("なんとか最寄り駅へと辿り着く"),
            sato.do("改札を抜けて、構内を移動する"),
            # TODO
            )
