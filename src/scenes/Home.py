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
            ayano.be("ベビィベッドで静かにしている"),
            taka.do("娘を見て一番の笑顔になる"),
            taka.do("抱き上げてもいいか？　という質問"),
            sato.talk("いいですけど、気をつけてくださいよ"),
            sato.do("以前落としかけたことを思い出す"),
            taka.talk("ええと"),
            taka.do("恐る恐る抱き上げる"),
            ayano.do("目覚めて泣き声を上げる"),
            sato.talk("ほら"),
            sato.do("すぐに変わる"),
            sato.do("あやしながら"),
            sato.talk("あまり家に戻ってこないから顔を忘れちゃったんじゃないですか？"),
            taka.talk("そんなことないよなー", "$ayanoはいい子だから覚えてるだろ？",
                "それにほら"),
            taka.do("自分が会社で作ったパパ代理ボットを見せて"),
            taka.talk("いつでもこれでパパとおしゃべりできるんだぞ？"),
            taka.do("キーホルダサイズのボットはお腹のスイッチでしゃべる"),
            taka.voice("$ayano、パパだよー", "$ayanoはいつもかわいいねー"),
            sato.talk("かわいいしか言わないじゃありませんか"),
            taka.talk("毎日かわいいと聞かせればもっとかわいくなるんじゃないか？"),
            sato.do("呆れる$S"),
            )


def goout_with_bento(w: World):
    sato, ayano = w.get("satomi"), w.get("ayano")
    return w.scene("弁当と一緒におでかけを",
            w.change_time("morning"),
            sato.be("久しぶりに出かける準備をしている"),
            sato.do("薄化粧だけれどそれでもいつもより入念に仕上げる"),
            sato.do("$ayanoは起きてきょろきょろと落ち着かない様子で"),
            # TODO:出かけるところから
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

