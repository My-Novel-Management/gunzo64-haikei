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
    sato = w.get("satomi")
    ayano = w.get("ayano")
    return w.scene("広い新居",
            w.change_camera("satomi"),
            w.change_stage("Living"),
            w.change_time("afternoon"),
            w.change_date(10,10, 2025),
            w.comment("$satomiの一人称で"),
            sato.be("$ayanoと二人きりで新居の広い空間にいる"),
            sato.do("建売の一戸建ての広い室内描写"),
            sato.do("ベビィベッドをゆする"),
            ayano.be("まだ生後まもない"),
            ayano.talk("あうあう"),
            sato.do("言葉もまだしゃべれない",
                "それでも必死に何かを伝えようとしている"),
            sato.think("――$sukiです"),
            sato.do("目の前の存在を見つめ、そう唇を動かす"),
            sato.do("左手の結婚指輪を見つめる"),
            sato.do("自分がまさか結婚できるとは思ってもみなかった"),
            sato.do("娘も生まれて、家族ができるなんて思ってもみなかった"),
            sato.do("$takaさん、$meはあなたが$sukiです"),
            )


def daughter_and_me(w: World):
    return w.scene("娘と私と",
            w.change_stage("Living"),
            )


def dog_robo(w: World):
    return w.scene('犬型ロボット',
            w.change_stage("Living"),
            )

