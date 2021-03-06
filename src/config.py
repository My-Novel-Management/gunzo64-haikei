# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ('satomi', '聡美', '結城,聡美', 33,(1,1), 'female', '主婦', "me:私"),
            ("ayano", "文乃", "結城,文乃", 3,(1,1), "female", "娘", "me:あや"),
            ("taka", "隆文", "結城,隆文", 35,(1,1), "male", "技師", "me:僕"),
            ("tanaka", "ブライアン", "田中,ブライアン", 35,(1,1), "male", "技師", "me:オレ"),
            ("kotani", "小谷", "小谷,富美", 27,(1,1), "female", "会社員", "me:わたし"),
            ("take", "竹中", "竹中,吉信", 45,(1,1), "male", "会社員", "me:俺"),
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ("Toshima", "豊島区", "Tokyo"),
            ("Ohta", "大田区", "Tokyo"),
            ("Ikebukuro", "池袋", "Toshima"),
            ("Hachiouji", "八王子市", "Tokyo"),
            ("Home", "聡美の自宅", "Hachiouji"),
            ("AroundHome", "自宅周辺", "Hachiouji"),
            ("Living", "リビング", "Home"),
            ("BedRoom", "寝室", "Home"),
            ("Kitchen", "台所", "Home"),
            ("Dining", "食堂", "Home"),
            ("ReadingRoom", "書斎", "Home"),
            ("Company", "隆文の会社", "Tokyo"),
            ("Office", "オフィス", "Company"),
            ("Street", "路地", "Tokyo"),
            ("Park", "公園", "Tokyo"),
            ("Cemetery", "墓地", "Tokyo"),
            ("CeremonyHall", "葬儀場", "Tokyo"),
            ("Market", "スーパー", "Tokyo"),
            ("Famires", "ファミレス", "Tokyo"),
            ("Station", "駅", "Tokyo"),
            ("Subway", "地下鉄", "Tokyo"),
            ("InTrain", "電車内", "Tokyo"),
            ("NursingHome", "介護施設", "Tokyo"),
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
            ("suki", "嫌い"),
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ),
        }

