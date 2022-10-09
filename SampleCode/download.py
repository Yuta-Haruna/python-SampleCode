import os
from urllib.request import *

print("ダウンロード開始")

# HTMLファイル 保存先のディレクトリ
save_dir = os.path.dirname(os.path.abspath(__file__)) + "/html/"

# なければ作成
if not os.path.exists(save_dir): 
    os.mkdir(save_dir)

# htmlをダウンロードするURL
# download_url = "http://kurikin.wp.xdomain.jp/"
download_url = "https://kabuoji3.com/"

# 保存先
# save_file = save_dir + "/kurikin.wp.xdomain.jp.html"
save_file = save_dir + "/kabuoji3.com.html"

# ダウンロード
urlretrieve(download_url, save_file)

print("ダウンロード完了")