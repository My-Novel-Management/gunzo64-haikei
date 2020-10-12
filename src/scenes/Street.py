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
    return w.scene('お弁当を届けに',
            w.change_stage("Street"),
            sato.come("通りをベビィカーを押しながら歩いている"),
            ayano.be(),
            sato.do("$ayanoに話しかけながら周囲のことを話す"),
            sato.do("住宅街で近くには小さな公園や散歩道が整備されている"),
            sato.do("遊歩道を歩けば車と遭遇せずに駅近くまでいけるのも魅力だ"),
            sato.do("隣接して博物館や図書館もある"),
            sato.think("のんびりとした気分で母と娘の二人だけででかけていると、ちらちらと過る、昔の思い出"),
            sato.think("子どもは無条件で親と一緒に過ごすことを強要される"),
            sato.think("家族、と呼ばれるものに対しての憧れは、小さい頃に幸せな記憶を持つ者だけに限られるのではないだろうか"),
            sato.think("彼は早くに母親を失い、父の手一つで育った"),
            sato.think("少し歳の離れた姉の存在も大きかったのだろう"),
            sato.think("そんな中でも幸福の意味を知り、彼は$Mに教えてくれた"),
            sato.think("娘を与えてくれた"),
            ayano.do("笑顔"),
            sato.think("娘はいつも笑っている",
                "生まれて最初の一月は泣いてばかりだった"),
            sato.think("こちら側が寝ることも叶わず、それでもなんとか娘のためとがんばった"),
            sato.think("現在は少し落ち着いている"),
            sato.think("それでもいつ泣き出すかと思うと、体が震えることもある"),
            sato.think("彼に、たまには外に出かけるのもいいと言われているけれど、それもなかなか難しい"),
            sato.think("小さな子どもを連れているというのがどういう状況か、休日に一緒に出かけてくれることのない彼にはあまり想像できないのだろう"),
            sato.do("ベビィカーのタイヤがはまる"),
            sato.do("それをなんとか押して脱出しようとするが、うまくいかない"),
            sato.do("見かねた配達員が手伝ってくれた"),
            sato.talk("どうもありがとうございます"),
            )

