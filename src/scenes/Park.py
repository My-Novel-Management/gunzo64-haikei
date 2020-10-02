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
def shape_of_family(w: World):
    return w.scene("家族の形",
            )


def with_dog(w: World):
    return w.scene('犬と娘と',
            )

