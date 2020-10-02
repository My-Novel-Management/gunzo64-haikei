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
def his_anniversary(w: World):
    return w.scene("彼の命日",
            )


def her_truth(w: World):
    return w.scene('彼女の真実',
            )

