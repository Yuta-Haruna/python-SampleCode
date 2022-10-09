import os
from bs4 import BeautifulSoup

print("HTML解析開始")

# HTMLファイル 保存先のディレクトリ
save_dir = os.path.dirname(os.path.abspath(__file__)) + "/html/"
# HTMLファイルパス
html_file = save_dir + "/kurikin.wp.xdomain.jp.html"

with open(html_file, encoding='utf-8') as f:

    bsoup = BeautifulSoup(f, "html5lib")

    # HTMLから該当の文字を取得
    syutoku_area = "#menu-item-28 > a > div > div.item-label"
    ele = bsoup.select_one(syutoku_area)
    # ele = bsoup.select_one(".entry-body > h2:nth-child(3)")
    #post-115 > div > div.new-entry-cards.widget-entry-cards.no-icon.cf.card-large-image.large-thumb.ect-vertical-card-2.ect-vertical-card.ect-2-columns.ecb-entry-border > a:nth-child(1) > div > div > div.new-entry-card-title.widget-entry-card-title.card-title
    #post-115 > div > div.new-entry-cards.widget-entry-cards.no-icon.cf.card-large-image.large-thumb.ect-vertical-card-2.ect-vertical-card.ect-2-columns.ecb-entry-border > a:nth-child(1) > div > div > div.new-entry-card-title.widget-entry-card-title.card-title
    #post-115 > div > div.new-entry-cards.widget-entry-cards.no-icon.cf.card-large-image.large-thumb.ect-vertical-card-2.ect-vertical-card.ect-2-columns.ecb-entry-border > a:nth-child(2) > div > div > div.new-entry-card-title.widget-entry-card-title.card-title
    if ele is None:
        print("見つかりませんでした")
    else:
        print("見つかりました：" + ele.string)

print("HTML解析終了")