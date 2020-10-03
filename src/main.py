#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from storybuilder.assets import common_rubi
from config import ASSET
# import scenes
from scenes import BedRoom
from scenes import Cemetery
from scenes import CeremonyHall
from scenes import Company
from scenes import Dining
from scenes import Famires
from scenes import Home
from scenes import InTrain
from scenes import Kitchen
from scenes import Living
from scenes import Market
from scenes import NursingHome
from scenes import Office
from scenes import Park
from scenes import ReadingRoom
from scenes import Station
from scenes import Street
from scenes import Subway


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Structure    - 1/8: 3K
#   4. Spec
#   5. Plot         - 1/4: 7K
#   6. Scenes
#   7. Conte        - 1/2: 15K
#   8. Layout
#   9. Draft        - 1/1: 30K
#
################################################################

# Constant
TITLE = "拝啓、あなたが嫌いです"
MAJOR, MINOR, MICRO = 1, 6, 0
COPY = "あなたがずっと、嫌いでした"
ONELINE = "仕事バカの夫は死後に犬型ロボットをプレゼントした。妻はそれに「ずっと嫌いでした」と告白する"
OUTLINE = "約30000字の恋愛中編。仕事で忙しかった夫は死後に自分のAIを載せた犬型ロボットをプレゼントした。それに対して残された妻は告白する。ずっと嫌いでしたと"
THEME = "人にとって言葉の定義は異なる"
GENRE = "恋愛／SF"
TARGET = "20-40years"
SIZE = "原稿70-250枚（20K-80K）"
CONTEST_INFO = "群像新人賞"
CAUTION = ""
NOTE = "エブリスタの妄想コンテストに応募した作品のリメイク"
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
TAGS = ["ドラマ",]
RELEASED = (10, 1, 2020)


# Episodes
def ep_beginning(w: World):
    return w.episode('書き出し',
            w.plot_note("あなたが嫌いです、という音声レターの書き出し"),
            w.plot_note("$ayanoが生まれてから特に夫は家に帰ってこなくなった"),
            w.plot_note("仕事熱心で、帰ってきてもすぐに部屋に入って寝てしまう"),
            w.plot_note("ある日、$satomiは夫に弁当を届けに彼の会社まで娘と二人で出かけた"),
            w.plot_note("会社に行くと、彼が意外とみんなから頼られていたり、人気があったりするのが分かった"),
            w.plot_note("けれど帰り際、自分とは違う仲良さそうな家族の姿を目にする"),
            w.plot_note("家庭に恵まれない自分の境遇を思う"),
            Living.spacious(w),
            Home.tired_my_husband(w),
            Dining.talk_with_taka(w),
            BedRoom.one_idea(w),
            Street.goto_his_office(w),
            InTrain.with_daughter(w),
            Office.his_work_place(w),
            Park.shape_of_family(w),
            Living.daughter_and_me(w),
            )

def ep_his_dead(w: World):
    return w.episode("彼の死",
            w.plot_note("夫があまり帰らなくなる"),
            w.plot_note("会話もなくなり、常に娘と二人だけという時間"),
            w.plot_note("そんな時にテレビではペットロスの話をやっていた"),
            w.plot_note("それを緩和するのに再びペットを買ったり、クローンペットを飼ったり"),
            w.plot_note("あったはずのものが失われたその隙間を、人々は色々な方法で埋めようとする"),
            w.plot_note("夫にペットのことを相談してみたが、返答はなかった"),
            w.plot_note("$takaの訃報がもたらされる"),
            w.plot_note("彼の葬儀を行う"),
            w.plot_note("親族や両親から色々と言われる"),
            w.plot_note("$satomiの父親と少しだけ顔を合わせる"),
            w.plot_note("母はまだ施設に入っていると知り、安堵する"),
            w.plot_note("娘と二人きりになり、どうすることもできなく途方にくれる"),
            Home.not_back_home(w),
            Dining.talk_about_pet(w),
            Market.his_dead_news(w),
            CeremonyHall.his_ceremony(w),
            Famires.talk_with_dad(w),
            NursingHome.meet_mother(w),
            Home.missing(w),
            )

def ep_dog_robo(w: World):
    return w.episode("犬のロボット",
            w.plot_note("小包でロボットが送られてくる"),
            w.plot_note("彼の遺言で、ロスケア犬型ロボットの試作機がやってきたのだ"),
            w.plot_note("彼がペットロスケアを目的としたロボット犬を開発していたと知る"),
            w.plot_note("そのロボット犬は$satomiの話し相手となった"),
            w.plot_note("その日から$satomiはロボット犬のモニターをすることになった"),
            w.plot_note("ロボットだけれど普通の犬のように扱うことにする"),
            w.plot_note("世話する対象が増えたことで$satomiの精神も少し安定し始める"),
            w.plot_note("彼女は犬に$takaに対する気持ちを語って聞かせた"),
            w.plot_note("彼との出会い"),
            w.plot_note("彼と結婚することになり"),
            w.plot_note("両親、特に母親との面会のことも"),
            w.plot_note("そうこうしているうちに月日が流れた"),
            Living.dog_robo(w),
            Park.with_dog(w),
            )

def ep_truth(w: World):
    return w.episode("真相",
            w.plot_note("彼の命日、一周忌に二人で墓参りをする"),
            w.plot_note("毎日録音をしてきた天国の彼への音声レターはそろそろいっぱいになっただろうか"),
            w.plot_note("墓につくと、突然犬が彼の声でしゃべりはじめた"),
            w.plot_note("彼は$satomiが「好き」を「嫌い」と言っていることに気づいていた"),
            w.plot_note("彼女は小さい頃に母親から「嫌い」と言われ続け、それを自然と「好き」に変換してしまうように意識を改変してしまった"),
            w.plot_note("それは$satomiの人生を不幸にしてしまっていた"),
            w.plot_note("彼女は愛した人間に「嫌い」と伝えてしまうのだ"),
            w.plot_note("それを理解していて$takaは彼女と一緒になった"),
            w.plot_note("もともと長生きはできないと考えていた$takaは、自分が死んでから彼女にかけられたその呪いを説くように考えた"),
            w.plot_note("録音された音声レターが再生される"),
            w.plot_note("けれどそれは「嫌い」を「好き」に変換したものだった"),
            w.plot_note("たくさんの、彼への、娘への「愛」がそこには記録されていた"),
            w.plot_note("上書きされた「好き」で、$satomiは本当の「好き」に気づく"),
            w.plot_note("娘に「好き」と伝えた"),
            Cemetery.his_anniversary(w),
            Cemetery.her_truth(w),
            )


# Chapters
def ch_main(w: World):
    return w.chapter('main',
            w.plot_setup("$satomiは夫を「嫌い」だった"),
            w.plot_setup("娘の$ayanoと自分を置いて、夫は仕事に打ち込んでいた"),
            w.plot_turnpoint("夫が死んだ"),
            w.plot_develop("夫が残したロス用ロボット犬が家にやってくる"),
            w.plot_develop("$satomiはその犬に日々の会話を残しつつ$ayanoの面倒を見る"),
            w.plot_develop("$tanakaと出会い、夫が隠して$satomiと$ayanoの為にロボット犬を作っていたと聞かされる"),
            w.plot_develop("ロボット犬の様子がおかしくなる"),
            w.plot_turnpoint("$satomiは母親の訃報を知る"),
            w.plot_resolve("ペットロボは夫の本当の目的を告げる"),
            w.plot_resolve("$satomiが「嫌い」という言葉を「好き」の意味に変換して使っていたことを告げる"),
            w.plot_resolve("記録していた$satomiの亡き夫へのボイスレターの「嫌い」を全て「好き」に上書きし、彼女の呪いを解いた"),
            ep_beginning(w),
            ep_his_dead(w),
            ep_dog_robo(w),
            ep_truth(w),
            )


# Notes
def write_note(w: World):
    return w.writer_note("覚書",
            )

def plot_note(w: World):
    return w.writer_note("プロットメモ",
            "あなたが嫌いです、という告白文から始まる",
            "嫌いというのが実は彼女にとっての「好き」だった、が真実",
            "結婚した彼はその「嫌いが好き」を理解していて、嫌いと言われ続けていた",
            "いつかは好きに変えたいと思っていたが、志半ばで倒れてしまう",
            "彼女は死んだ彼に対して「嫌い」と日々を綴る",
            "それはロボットに愚痴るようにして記録されていた",
            "最後に全ての記録文章が「好き」に変わる",
            "そこで娘も「好き」を知る",
            "主人公の「過去」特に「家族からの扱われ方」について書いておく必要がある",
            "それは直接的ではなく、想像できるように「家族」についてのピースをあちこちに散らばらせること",
            )

def chara_note(w: World):
    return w.writer_note("人物メモ",
            "主人公の彼女",
            "隆文：主人公の夫で技術者",
            "主人公の娘",
            "ロボット犬",
            "診療所の先生",
            "ブライアン",
            )

def stage_note(w: World):
    return w.writer_note("舞台メモ",
            "住宅街、特に新興住宅地だった場所がいい",
            "家庭、家族を思わせるところで、よく仲良さそうな家族が目に就く場所。公園が近いとか",
            "でもその中にはごく稀にひどい家族も混ざっていると",
            )

def theme_note(w: World):
    return w.writer_note("テーマメモ",
            "人間は生きるために真実ですら歪める",
            "人間の防衛本能として「嘘を真実にして」までも自分を肯定しようとする",
            "本作では「嫌い」という言葉を吐き続けられた女性がそれを「好き」と変換して思い込むことで生きてこられた、という人生を抱えている",
            "家族は正しいとか、家族だから愛があるとか、そんなまやかしはもう通用しない",
            "家族であっても人間同士であり、そこには傷つけ合うことだってある",
            "だからこそ、その中で生き延びる為に必死になって嘘を真実にする",
            "虐待、それは何も暴力に限らない",
            "言葉だって、いや言葉だからこそ人を傷つける",
            "トラウマになる",
            "これはそれが浄化されるまでの物語だ",
            "最後まで読めばその「違和感」が感動に変わる",
            "今までのものが上書きされ、リバーサル",
            "○○ロス",
            "大切なものを失った心の隙間を埋める「産業」としてのロボット",
            "定義をする、ということと、その上書き",
            "コンピュータの挙動",
            "元勤め先はコンピュータ関係",
            "なるべく対人でないものの方が良かった、という",
            )

def motif_note(w: World):
    return w.writer_note("モチーフメモ",
            "言葉の意味",
            "人によって定義が異なる",
            "小さい頃の虐待の記憶が意味を歪める",
            "定義",
            "虐待",
            "自己防衛",
            "ロスを癒やすロボットペット",
            )


# Main
def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(common_rubi.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_taginfos(*TAGS)
    w.config.set_released(*RELEASED)
    return w.run(
            write_note(w),
            plot_note(w),
            chara_note(w),
            stage_note(w),
            theme_note(w),
            motif_note(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

