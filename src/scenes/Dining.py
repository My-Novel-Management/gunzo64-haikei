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
def talk_with_taka(w: World):
    sato = w.get("satomi")
    ayano = w.get("ayano")
    taka = w.get("taka")
    return w.scene("新婚の会話",
            w.change_stage("Dining"),
            w.change_time("night"),
            sato.be(),
            taka.be("座って箸を握っている"),
            sato.do("お茶漬けと自家製の漬物、それに味噌汁と卵焼き"),
            taka.talk("茶漬けだけでいいって言ったのに"),
            sato.talk("作ってあったんだから食べてください",
                "誰のために作ってると思っているんですか"),
            taka.talk("ありがとう", "いつも遅くなってすまない",
                "いただきます"),
            taka.do("急に真面目になって、手を合わせてから、食べ始める"),
            taka.do("美味しそうに食べる"),
            sato.think("その表情をこうやって見ているのが何よりの幸福なんだと思う"),
            )


def talk_about_pet(w: World):
    sato = w.get("satomi")
    return w.scene('ペットの話',
            w.change_stage("Dining"),
            )

