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
def goto_his_office(w: World):
    sato, ayano = w.get("satomi"), w.get("ayano")
    return w.scene("彼の会社に向かって出発",
            w.change_stage("AroundHome"),
            w.change_time("midmorning"),
            sato.come("自宅から出てきて、玄関の施錠を確認する"),
            ayano.be("ベビィカーで楽しそうにしている$S"),
            sato.do("よい天気で、近隣からは赤ん坊の泣き声や、婦人たちのしゃべり声"),
            sato.do("営業で回っている人の姿も見かける"),
            sato.do("ベビィカーを押して出かける$S"),
            )
