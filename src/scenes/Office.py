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
def his_work_place(w: World):
    sato, ayano = w.get("satomi"), w.get("ayano")
    taka = w.get("taka")
    kotani = w.get("kotani")
    return w.scene('彼の仕事場',
            w.change_stage("Office"),
            sato.come("ベビィカーと$ayanoを手に、上がってくる$S"),
            sato.do("オフィスを覗き込むと受付の女性がこっちを見た"),
            kotani.be(),
            kotani.talk("何か御用ですか？"),
            sato.talk("あの、$takaさんの妻です"),
            kotani.talk("ああ、$ln_takaさんの奥様",
                "いつも大変お世話になってるんですよ",
                "あちらです"),
            kotani.do("含みがありそうな笑みを浮かべる"),
            sato.think("どういう存在なのかよく分からないけれど、好意的に受け入れればいいのかと考える"),
            taka.be("パソコンがたくさん並ぶデスクの中で、隣の人と何やら神妙な顔つきで話し合っている"),
            sato.do("初めて見る仕事中の彼の姿"),
            taka.do("モニタを見ながら相談している"),
            kotani.talk("$ln_takaさん", "奥様が来られてますよ"),
            taka.talk("え？"),
            taka.do("$satomiの姿を見つけてにっこりする"),
            taka.talk("どうしたんだ"),
            sato.talk("これです"),
            sato.do("弁当を見せる"),
            taka.talk("わざわざありがとう",
                "でも弁当なんていつぶりだ？"),
            sato.talk("たまには、ね"),
            sato.do("周囲の目が"),
            )

