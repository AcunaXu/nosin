import requests
import random
import csv
from lxml import etree

url = "https://www.xicidaili.com/nn/"
headers = [
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
           ]
header = random.choices(headers)[0]
print(header)

def request1():
    response = requests.get(url=url, headers={"User-Agent": header})
    response.encoding = 'utf-8'
    ip_html = etree.HTML(response.text)
    datas = ip_html.xpath('/html/body/div/div[2]/table/tr[@class="odd"]')
    for data in datas:
        dip1 = data.xpath('td[2]/text()')
        dip2 = data.xpath('td[3]/text()')
        dip3 = data.xpath('td[6]/text()')
        ip1 = dip3[0]
        ip2 = dip1[0]
        ip3 = dip2[0]
        ip = ip1, ip2+":"+ip3,

        url_wenshu = 'http://wenshu.court.gov.cn/'
        proxies = {'{0}'.format(ip1): '{1}:{2}'.format(ip1, ip2, ip3)}
        print(proxies)
        try:
            requests.get(url=url_wenshu, proxies=proxies, headers={"User-Agent": header})
        except:
            print('FAIL')
        else:
            print('PASS')
            yield ip


def op(datas):
    with open("ips.csv", "w", newline='', encoding='utf-8') as f:
        ff = csv.writer(f)
        ff.writerows(datas)

def main():
    datas = request1()
    op(datas)

if __name__ == '__main__':
    main()
