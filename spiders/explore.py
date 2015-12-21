# -*- coding: utf-8 -*-
from grab.spider import Spider

from spiders.base import BaseHubSpider

import re

class ExploreSpider(BaseHubSpider):
    
    def task_initial(self, grab, task):
        repos = grab.doc.select(
            '//a[@class="m_select"]')
        p = re.compile('model\.php\?manufacture=(\d*)')
        for repo in repos:
            q = p.match(repo.select(".//@href").text()).group(1) # @UnusedVariable
            data = {
                'name': repo.text() ,
                'link': repo.select(".//@href").text(),
                'manid': p.match(repo.select(".//@href").text()).group(1),
            }

            self.saveManufacture(data)
            self.log_progress(data['name'] + ' / ' + data['link'])