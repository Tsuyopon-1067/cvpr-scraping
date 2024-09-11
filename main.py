import requests
from lxml import html


def main():
    # ウェブページからHTMLデータを取得
    year = 2024
    url = 'https://openaccess.thecvf.com/CVPR' + str(year) + '?day=all'
    response = requests.get(url)
    html_content = response.text

# lxmlを使用してHTMLをパース
    tree = html.fromstring(html_content)

# XPathを使用して要素を取得
    elements = tree.xpath('/html/body/div[3]/dl/dt')

# 取得した要素を表示
    for element in elements:
        a_tag = element.find('a')
        if a_tag is not None:
            title = a_tag.text_content().strip()
            href = a_tag.get('href')
            if href and not href.startswith('http'):
                href = 'https://openaccess.thecvf.com' + href
            print(title + ',' + href)


if __name__ == "__main__":
    main()
