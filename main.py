import requests
from lxml import html

# ウェブページからHTMLデータを取得
url = 'https://openaccess.thecvf.com/CVPR2023?day=all'
response = requests.get(url)
html_content = response.text

# lxmlを使用してHTMLをパース
tree = html.fromstring(html_content)

# XPathを使用して要素を取得
elements = tree.xpath('/html/body/div[3]/dl/dt')

# 取得した要素を表示
for element in elements:
    print(element.text_content())
