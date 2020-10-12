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
    sato, ayano = w.get("satomi"), w.get("ayano")
    return w.scene('娘と鉄道内で',
            w.change_stage("InTrain"),
            sato.be("なんとか座らせてもらってちんまりとしている$S"),
            ayano.be(),
            sato.do("通勤時刻は過ぎていたので少し空いていた"),
            sato.do("会社員時代に満員電車で苦労していたことを思い出す"),
            sato.do("身長が低くてつり革がぎりぎり届く高さで、人が多いと視界が失われてしまって"),
            sato.do("そんな時にも一緒に彼がいてくれれば安心することができた"),
            sato.do("$Sはいつも周囲にびくびくしながら生きている"),
            sato.do("それは今も変わらない"),
            sato.do("アナウンスが流れ、彼の会社の最寄り駅が近づいていることが分かった"),
            sato.do("降りる準備をする"),
            )

