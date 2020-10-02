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
def spacious(w: World):
    return w.scene("広い新居",
            w.change_camera("satomi"),
            w.change_stage("Living"),
            w.change_time("afternoon"),
            w.change_date(10,10, 2025),
            )


def daughter_and_me(w: World):
    return w.scene("娘と私と",
            w.change_stage("Living"),
            )


def dog_robo(w: World):
    return w.scene('犬型ロボット',
            w.change_stage("Living"),
            )

