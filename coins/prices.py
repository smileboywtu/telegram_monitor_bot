# -*- coding: utf-8 -*-

import requests


def get_usdt_price_banner_from_aicoin():
    """
    从 banner 获取 usdt 的价格

    """
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "https://www.aicoin.cn/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "Accept-Language": "zh,en;q=0.9,zh-CN;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Cookie": "HWWAFSESID=f3d577c02de261de2f; HWWAFSESTIME=1582680745680; _pk_testcookie..undefined=1; _pk_testcookie.2.57ea=1; Hm_lvt_3c606e4c5bc6e9ff490f59ae4106beb4=1582680768; _ga=GA1.2.956220123.1582680769; _gid=GA1.2.850658697.1582680769; _pk_ses.2.57ea=1; _pk_testcookie.2.f745=1; _pk_ref.2.f745=%5B%22%22%2C%22%22%2C1582690786%2C%22https%3A%2F%2Fwww.aicoin.cn%2F%22%5D; _pk_ses.2.f745=1; XSRF-TOKEN=eyJpdiI6InpzaE90U0pxOU1oT2hNTUoydTVpOFE9PSIsInZhbHVlIjoiMmswd0FqdGFqZDVzenNKXC9OZ1pUcGJYUTF2QlVxWHFlVWJKOUNHS1VTSXRXZ25NS20yRDJ6eHY2QStueitEQURKYnRpemNqYkc0KzFwclFPMUZaTFpRPT0iLCJtYWMiOiI0MzY2NzI5OTM5Yzc2N2E5ZDA3MGNjZjQ0ZjYxNWIzZGU2YzgzNDkwMjFiOTYyMjYxZGU0ZWI0NmE0NTJhNTc1In0%3D; _pk_id.2.f745=bdf779e7802382db.1582690785.1.1582690792.1582690785.; _pk_id.2.57ea=05e95de5a792d163.1582680766.2.1582692287.1582690779.; Hm_lpvt_3c606e4c5bc6e9ff490f59ae4106beb4=1582692288; aicoin_session=eyJpdiI6IlR6b2poeWd6N3MzYitBdGo0Ylwva2FBPT0iLCJ2YWx1ZSI6ImdTcTE4ME1OenZcL25ObUdrSlhcL2h0QnJGOHg2SFFPSUl5VDFpUzl3czBBK1wvZ2w2U0I0ekp1XC95Uk02bU42enlyZ25vSVptZEE2XC9nXC9GNzJaMWE0U1ZBPT0iLCJtYWMiOiJhNDZhNTUxYTUzZGFlYWQ0M2JjN2Q5NzFkOTI4MTJjYzZkM2M4OGI2OTM2NGYwNzBkYTA2Y2IwY2VmMTc0MzQxIn0%3D"
    }

    query = {
        "p": 1,
        "language": "cn",
        "currency": "usd",
        "open_time": 24
    }

    url = "https://www.aicoin.cn/api/home/new-banner"
    try:
        resp = requests.get(url, params=query, headers=headers, timeout=5)
        rjson = resp.json()
        if rjson["success"]:
            return rjson["data"]["banner"][4]
        return []
    except TimeoutError:
        return None


def get_price_from_aicoin(coin_name, key_filter=""):
    """
    从 AI coin 获取货币价格信息

    """
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "https://www.aicoin.cn/search?s=cmt",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "Accept-Language": "zh,en;q=0.9,zh-CN;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }
    form = {
        "key": coin_name,
        "currency": "cny",
        "type": 4,
        "page_size": 20,
        "curr_page": 1
    }

    url = "https://www.aicoin.cn/api/chart/market/search"
    try:
        resp = requests.post(url, data=form, headers=headers, timeout=5)
        rjson = resp.json()
        if rjson["success"]:
            return [e for e in rjson["data"]["list"] if key_filter in e["key"]][0]
        return []
    except TimeoutError:
        return None


if __name__ == "__main__":
    # print(get_price_from_aicoin("usdt", "usdtcnyt:bitasset"))
    print(get_usdt_price_banner_from_aicoin())
