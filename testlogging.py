# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:09:48 2019

@author: Administrator
"""

import logging

logging.basicConfig(filename='info.log',
                    filemode='a',
                    level = logging.INFO,
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                    )
#logger = logging.getLogger(__name__)

#help(logging.getLogger)

logging.info("Start print log")
logging.debug("Do something")
logging.warning("Something maybe fail.")
logging.info("Finish")