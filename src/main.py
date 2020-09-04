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
# from scenes import xxx


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
MAJOR, MINOR, MICRO = 1, 1, 0
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
RELEASED = (9, 1, 2020)


# Episodes
def ep_beginning(w: World):
    return w.episode('書き出し',
            )

def ep_his_dead(w: World):
    return w.episode("彼の死",
            )

def ep_dog_robo(w: World):
    return w.episode("犬のロボット",
            )

def ep_truth(w: World):
    return w.episode("真相",
            )


# Chapters
def ch_main(w: World):
    return w.chapter('main',
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
            )

def motif_note(w: World):
    return w.writer_note("モチーフメモ",
            "言葉の意味",
            "人によって定義が異なる",
            "小さい頃の虐待の記憶が意味を歪める",
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

