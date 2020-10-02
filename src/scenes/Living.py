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
            )


def daughter_and_me(w: World):
    return w.scene("娘と私と",
            )


def dog_robo(w: World):
    return w.scene('犬型ロボット',
            )

