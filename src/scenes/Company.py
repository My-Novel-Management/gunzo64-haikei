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
def his_company(w: World):
    sato, ayano = w.get("satomi"), w.get("ayano")
    return w.scene("彼の会社",
            w.change_stage("Company"),
            sato.come("メモの地図を見ながらきょろきょろと歩いている"),
            ayano.be(),
            sato.do(""),
            )
