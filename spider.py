# -*- coding: utf-8 -*-
"""
Github projects spy
"""
from optparse import OptionParser

from grab import Grab
from grab.spider import Spider, Task
from weblib.logs import default_logging

from spiders.explore import ExploreSpider
from spiders.lang_python import LangPythonSpider
from config import default_spider_params, Session

if __name__ == '__main__':
    default_logging()
    parser = OptionParser()

    # command line options
    parser.add_option("-p", "--python", action="store_true",
                      dest="parse_manufactures", default=False)

    options, args = parser.parse_args()
    
    if options.parse_manufactures:
        print "Scape python projects"
        bot = LangPythonSpider(**default_spider_params())
    else:
        print "Scrape trandings"
        bot = ExploreSpider(**default_spider_params())

    bot.load_proxylist('/var/proxylistrus.txt',  "text_file", "http")
    bot.create_grab_instance(timeout=4096, connect_timeout=10)
    bot.run()
    print bot.render_stats() 