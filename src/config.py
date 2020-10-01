# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ('satomi', '聡美', '', 33,(1,1), 'female', '主婦', "me:私"),
            ("ayano", "文乃", "", 3,(1,1), "female", "娘", "me:あや"),
            ("taka", "隆文", "", 35,(1,1), "male", "技師", "me:僕"),
            ("tanaka", "ブライアン", "田中,ブライアン", 35,(1,1), "male", "技師", "me:オレ"),
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ("Toshima", "豊島区", "Tokyo"),
            ("Ikebukuro", "池袋", "Toshima"),
            ("Hachiouji", "八王子市", "Tokyo"),
            ("Home", "聡美のマンション", "Hachiouji"),
            ("Company", "隆文の会社", "Tokyo"),
            ),
        "DAYS": (
            # (tag / name / month / day / year)
            ),
        "TIMES": (
            # (tag / name / hour / minute)
            ),
        "ITEMS": (
            # (tag / name / cate / info)
            ),
        "WORDS": (
            # (tag / name / cate / info)
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ),
        }

