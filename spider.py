# -*- coding: utf-8 -*-
"""
Github projects spy
"""
from optparse import OptionParser

from weblib.logs import default_logging

from spiders.manufacture import ManufactureSpider
from config import default_spider_params, Session
from spiders import model
from grab.spider import data
from models import Manufacture
from spiders.model import ModelSpider

if __name__ == '__main__':
    default_logging()
    parser = OptionParser()

    # command line options
    parser.add_option("-p", "--python", action="store_true",
                      dest="parse_manufactures", default=False)

    options, args = parser.parse_args()
    
    # print "Scrape main"
    # bot = ExploreSpider(**default_spider_params())
    bot = ModelSpider(**default_spider_params())
    session = Session()

    for item in session.query(Manufacture).all():
            bot.initial_urls.append('http://tecdoc.autodoc.ru/'+item.link)

    bot.load_proxylist('/var/proxylistrus.txt',  "text_file", "http")
    bot.create_grab_instance(timeout=4096, connect_timeout=10)
    bot.run()
    #print bot.render_stats() 