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
def with_daughter(w: World):
    return w.scene('娘と鉄道内で',
            w.change_stage("InTrain"),
            )

