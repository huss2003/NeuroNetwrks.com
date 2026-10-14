"""Tell Bing (and other IndexNow engines) that every page in the sitemap changed.
Run after each production deploy:  python3 tools/preview-gen/indexnow.py"""
import json, re, urllib.request, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
SITE = "https://neuronetwrks.com"
KEY = re.search(r'INDEXNOW_KEY = "(\w+)"', open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build.py")).read()).group(1)
sm = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "site-preview", "sitemap.xml")).read()
urls = re.findall(r"<loc>(.*?)</loc>", sm)
body = json.dumps({"host": "neuronetwrks.com", "key": KEY, "keyLocation": f"{SITE}/{KEY}.txt", "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={"Content-Type": "application/json; charset=utf-8"})
with urllib.request.urlopen(req, timeout=30) as r:
    print("IndexNow:", r.status, f"({len(urls)} URLs)")
