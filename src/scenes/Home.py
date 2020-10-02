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
def tired_my_husband(w: World):
    return w.scene("疲れている夫",
            )


def not_back_home(w: World):
    return w.scene("戻らない夫",
            )


def missing(w: World):
    return w.scene('彼はもういない',
            )

