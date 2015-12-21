# -*- coding: utf-8 -*-
from grab.spider import Spider

from spiders.base import BaseHubSpider

import re

class ModelSpider(BaseHubSpider):
    
    def task_initial(self, grab, task):
        repos = grab.doc.select(
            '//tbody/tr') 
        p = re.compile('modification\.php\?manufacture=\d*&model=(\d*)')
        for repo in repos:
            q = p.match(repo.select(".//@href").text()).group(1) # @UnusedVariable
            data = {
                'name': repo.select(".//td")[0].text() ,
                'link': repo.select(".//td/a/@href").text(),
                'modelid': p.match(repo.select(".//td/a/@href").text()).group(1),
                'startman': repo.select(".//td")[1].text() ,
                'stopman': repo.select(".//td")[2].text() ,
            }

            self.saveModel(data)
            self.log_progress(data['name'] + ' / ' + data['link'])