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
def one_idea(w: World):
    sato = w.get("satomi")
    ayano = w.get("ayano")
    return w.scene("あるアイデア",
            w.change_stage("BedRoom"),
            w.change_time("midnight"),
            sato.be("寝室で寝ている$S"),
            ayano.be("ベビィベッドで寝ていたが、ふと目覚めて小さな声をあげる"),
            sato.do("寝室は彼とは別にしていた",
                "彼が夜遅く帰ってきてゆっくり休めるように別室に布団を敷いてある"),
            sato.talk("起きちゃったのね"),
            sato.do("起き上がり、様子を見る"),
            sato.do("ミルクをあげながら考える"),
            sato.do("子どもが生まれる前は毎日弁当を作ってあげていたことを思い出す"),
            sato.do("今は近所にいきつけの定食屋があるからいいと断っていたが、久しぶりに作ろうと思った"),
            )
