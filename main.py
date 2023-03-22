# -*- coding: utf-8 -*-
import requests
import json
from local_config import CLIENT_RAKUTEN

def main():
    KEYWORD = "リーバイス ヴィンテージ パンツ デニム"
    REQ_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
    HITS_PER_PAGE = 30  # NOTE: ページあたり商品数

    params = {
        "applicationId": CLIENT_RAKUTEN["APPLICATION_ID"],
        "affiliateId": CLIENT_RAKUTEN["AFF_ID"],
        "format": "json",
        "formatVersion": "2",
        "sort": "-itemPrice",
        "minPrice": 100,
        "keyword": KEYWORD,
        "hits": HITS_PER_PAGE,
    }

    # 1-1: 楽天の商品検索APIにリクエストを投げ、レスポンスを受け取る。
    cnt = 1
    params["page"] = cnt
    res = requests.get(REQ_URL, params)
    res = json.loads(res.text)
    print(res)

if __name__ == "__main__":
    main()
