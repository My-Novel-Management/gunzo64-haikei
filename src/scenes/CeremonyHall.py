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
def his_ceremony(w: World):
    return w.scene('彼の葬儀',
            w.change_stage("CeremonyHall"),
            )

