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
            w.change_stage("Home"),
            )


def not_back_home(w: World):
    return w.scene("戻らない夫",
            w.change_stage("Home"),
            )


def missing(w: World):
    return w.scene('彼はもういない',
            w.change_stage("Home"),
            )

