# -*- coding: utf-8 -*-
"""生成 cards.snh48.xlsx（SNH48 上海现役成员索引）并向 pages.unified.xlsx 追加专题行。"""
import os, openpyxl

XLSX = r"D:\Universal Space\publish\xlsx"
CARDS_DIR = os.path.join(XLSX, "cards-pages")
SNH_XLSX = os.path.join(CARDS_DIR, "cards.snh48.xlsx")
PAGES = os.path.join(XLSX, "pages.unified.xlsx")

HEADERS = ["row_seq","dir_path","cat_id","cat_name","card_layout","card_title","card_desc",
           "card_media","card_tags","card_id","card_order",
           "link_1_name","link_1_url","link_2_name","link_2_url","link_3_name","link_3_url",
           "link_4_name","link_4_url","link_5_name","link_5_url","link_6_name","link_6_url",
           "link_7_name","link_7_url","link_8_name","link_8_url","link_9_name","link_9_url",
           "link_10_name","link_10_url","enabled","is_ad"]

# (name, sid)  —— sid 取自官网 mobile/member.html 真实成员主页
TEAMS = {
    "sii": ("Team SII", [
        ("曹可甜","10337"),("蒋夏羽","10324"),("刘婧阳","10350"),("刘诗彤","10338"),("李婷","10353"),
        ("芦馨怡","10267"),("柳雨呈","10339"),("刘增艳","10125"),("宁轲","10230"),("盛乐","10329"),
        ("田姝丽","10130"),("吴志越","10376"),("由淼","10227"),("闫明筠","10094"),("杨心渝","10289"),
        ("张雷雷","10318"),("张倩","10299"),("周童玥","10290"),
    ]),
    "nii": ("Team NII", [
        ("柏欣妤","10234"),("葛俊言","10371"),("黄孟浠","10372"),("胡晓慧","10118"),("金莹玥","10178"),
        ("李继醇","10349"),("潘瑛琪","10126"),("秦箐忆","10368"),("青钰雯","10238"),("沈馨","10354"),
        ("唐程成","10295"),("徐佳琳","10355"),("叶凡","10298"),("杨宇馨","10249"),("臧文萱","10370"),
        ("周湘","10293"),("钟亚男","10336"),("朱怡欣","10320"),
    ]),
    "hii": ("Team HII", [
        ("陈嘉仪","10344"),("陈俞希","10312"),("龚晨美","10322"),("何馨曼","10373"),("蒋舒婷","10120"),
        ("康楚翊","10325"),("李佳恩","10151"),("林舒晴","10212"),("刘思雨","10352"),("刘钇霏","10367"),
        ("阙佳慧","10328"),("覃柯蒙","10330"),("宋昕冉","10087"),("王佳琪","10374"),("温若其","10286"),
        ("王天娇","10375"),("应籽言","10334"),("张宸","10377"),("郑柯炜","10358"),("张琼予","10218"),
        ("曾雪婷","10359"),
    ]),
    "x": ("Team X", [
        ("陈琳","10081"),("金泓言","10313"),("蒋欣洳","10347"),("林佳怡","10259"),("刘小涵","10274"),
        ("马欣宇","10340"),("王睿琦","10220"),("熊紫轶","10269"),("杨冰怡","10093"),("禹佳蔚","10261"),
        ("闫娜","10258"),("杨秋野","10316"),("杨晔","10247"),("钟郭菲杨","10357"),("朱虹蓉","10342"),
        ("朱瑞缘","10343"),("曾昕妍","10360"),
    ]),
    "trainee": ("预备生", [
        ("丁小凡","10362"),("何蔡娴","10378"),("何绮多","10363"),("韩云伊","10361"),("黄子珊","10364"),
        ("黄子欣","10346"),("黄紫怡","10323"),("吉雅楠","10365"),("李沁洁","10366"),("李子忻","10315"),
        ("谭思慧","10341"),("武博涵","10260"),("徐诗琪","10167"),("杨宝君","10369"),("左婧媛","10273"),
    ]),
}

def build_rows():
    rows = []
    seq = 0
    for key, (label, members) in TEAMS.items():
        for name, sid in members:
            seq += 1
            if key == "trainee":
                desc = "SNH48（上海）女子偶像组合预备生（练习生）。"
            else:
                desc = "SNH48（上海）女子偶像组合成员，所属 %s。" % label
            url = "https://www.snh48.com/mobile/member-detail.html?sid=%s&gid=10" % sid
            row = {h: "" for h in HEADERS}
            row["row_seq"] = seq
            row["dir_path"] = "topics/snh48"
            row["cat_id"] = key
            row["cat_name"] = label
            row["card_layout"] = 1
            row["card_title"] = name
            row["card_desc"] = desc
            row["card_media"] = ""
            row["card_tags"] = "SNH48,%s" % label
            row["card_id"] = ""
            row["card_order"] = ""
            row["link_1_name"] = "SNH48 官方主页 - %s" % name
            row["link_1_url"] = url
            row["enabled"] = "True"
            row["is_ad"] = ""
            rows.append(row)
    return rows

def write_cards(rows):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Sheet"
    ws.append(HEADERS)
    for r in rows:
        ws.append([r[h] for h in HEADERS])
    wb.save(SNH_XLSX)
    print("生成 %s : %d 行" % (os.path.basename(SNH_XLSX), len(rows)))

def append_page():
    wb = openpyxl.load_workbook(PAGES)
    ws = wb.active
    # 读表头
    header = [c.value for c in ws[1]]
    new_row = {h: "" for h in header}
    new_row.update({
        "dir_path": "topics/snh48",
        "title": "SNH48 成员索引 - 正协导航",
        "description": "正协导航 SNH48 成员索引：收录 SNH48（上海）女子偶像组合现役成员，按 Team SII / NII / HII / X 及预备生分组陈列，每张卡片直达成员官方主页，方便粉丝快速查找与关注。",
        "keywords": "SNH48,SNH48成员,SNH48成员索引,丝芭传媒,女子偶像组合,Team SII,Team NII,Team HII,Team X",
        "channel_intro": "本站为独立第三方粉丝索引站，与 SNH48 / 丝芭传媒无隶属关系。本频道按队伍整理 SNH48（上海）现役成员，每张卡片直达成员官方主页（snh48.com），仅供索引聚合，不代表本站立场。",
        "enabled": "True",
        "channel_intro_enabled": "True",
        "ad_slots": "1,2",
        "stat_ga4": "True",
        "stat_baidu": "True",
        "search_box": None,
    })
    ws.append([new_row.get(h, "") for h in header])
    wb.save(PAGES)
    print("pages.unified.xlsx 追加行: topics/snh48")

if __name__ == "__main__":
    rows = build_rows()
    write_cards(rows)
    append_page()
