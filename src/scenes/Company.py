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
            sato.do("会社の近くまできたのは久しぶりだった"),
            sato.do("昔から小さな工場の多い地域だったが徐々に閉鎖される工場が増えて風景も様変わりしていた"),
            sato.do("オフィスビルが増え、ソフト関係の会社も多く入るようになっていた"),
            sato.do("その新しい雑居ビル群の中に彼の会社はある"),
            sato.do("五階建てのビルを見つけ、入っていく"),
            )
