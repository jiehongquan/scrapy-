from scrapy import cmdline


def main():
    cmdline.execute('scrapy crawl douban_spider'.split())
   
   
if __name__ == '__main__':
    main()
