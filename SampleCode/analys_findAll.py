import os
from bs4 import BeautifulSoup

print("HTML解析開始")

# HTMLファイル 保存先のディレクトリ
save_dir = os.path.dirname(os.path.abspath(__file__)) + "/html/"
# HTMLファイルパス
# html_file = save_dir + "/kurikin.wp.xdomain.jp.html"
html_file = save_dir + "/kabuoji3.com.html"

with open(html_file, encoding='utf-8') as f:

    bsoup = BeautifulSoup(f, "html5lib")

    # HTMLから該当の範囲を取得
    # syutoku_area = "menu-\%e3\%83\%a1\%e3\%82\%a4\%e3\%83\%b3\%e3\%83\%a1\%e3\%83\%8b\%e3\%83\%a5\%e3\%83\%bc-1"
    syutoku_area = "#tools"
    ele = bsoup.select_one(syutoku_area)
    #menu-\%e3\%83\%a1\%e3\%82\%a4\%e3\%83\%b3\%e3\%83\%a1\%e3\%83\%8b\%e3\%83\%a5\%e3\%83\%bc-1
    # ele = bsoup.select_one("div.postList:nth-child(4)")
    #tools > ul:nth-child(1) > li:nth-child(1) > a > section > h2 > span.jp

    if ele is None:
        print("見つかりませんでした")
    else:
        # h1タグのリストを取得
        # allTitles = ele.find_all("h1")
        # allTitles = ele.find_all("item-label")
        allTitles = ele.find_all("h2")
        # for h1 in allTitles:
        for h2 in allTitles:
            # h1の中のaタグの表示文字列を取得
            print(h2.select_one("span.jp").string)
            #tools > ul:nth-child(1) > li:nth-child(1) > a > section > h2 > span.jp
            #tools > ul:nth-child(2) > li:nth-child(1) > a > section > h2 > span.jp

    # if ele is None:
    #     print("見つかりませんでした")
    # else:
    #     # h1タグのリストを取得
    #     # allTitles = ele.find_all("h1")
    #     allTitles = ele.find_all("item-label")
    #     for h1 in allTitles:
    #         # h1の中のaタグの表示文字列を取得
    #         print(h1.select_one("a").string)

print("HTML解析終了")