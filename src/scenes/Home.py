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
def tired_my_husband(w: World):
    sato = w.get("satomi")
    ayano = w.get("ayano")
    taka = w.get("taka")
    return w.scene("疲れている夫",
            w.change_stage("Home"),
            sato.be("娘のおむつを替えている"),
            ayano.be(),
            sato.do("娘は大人しくしてくれている"),
            taka.come("帰ってくる夫"),
            # NOTE: 外見描写
            taka.do("ほっそりとした男性"),
            sato.talk("$takaさん、おかえりなさい"),
            taka.talk("ただいま", "いやあ今日は酷いバグ祭りでね、本当に疲れたよ"),
            sato.do("最近やたらと「疲れた」と口にすることが多い夫"),
            sato.talk("ご飯、また軽いものにします？"),
            taka.talk("今日は食べてきたからいいや",
                "あ、でも茶漬けだけもらおうかな",
                "少し薬も飲んでおきたいし"),
            taka.talk("$ayanoはどうだ？", "大変なら預け先も少し考えた方がいい気がしてるんだが"),
            sato.talk("$meは大丈夫ですよ",
                "それに$ayanoも大人しくいい子にしてくれていますし"),
            # TODO: 人となりと状況設定
            )


def not_back_home(w: World):
    sato = w.get("satomi")
    return w.scene("戻らない夫",
            w.change_stage("Home"),
            )


def missing(w: World):
    sato = w.get("satomi")
    return w.scene('彼はもういない',
            w.change_stage("Home"),
            )

