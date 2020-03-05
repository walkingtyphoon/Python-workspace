import re

# import urllib.request
#
# req = urllib.request.Request("https://list.mogu.com/book/clothing/50244?acm=3.mce.1_10_1mcsq.132494.0.oBqcZrSaq4syh.pos_2-m_521481-sd_119&ptp=31.v5mL0b.0.0.T904Mx44")
# res = urllib.request.urlopen(req)
# html = res.read().decode("UTF-8")
# with open("01.html","w", encoding="utf-8") as ht:
#     ht.write(html)

with open("01.html", "r", encoding="utf-8") as ht:
    asd = str(ht.readlines())
    value = re.findall("<img src='.*?' alt='(.*?)'>", asd)
    print(value)
