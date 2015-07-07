'''
    Module ptop.statistics

    Generate stats by using the plugins in the ../plugins directory and gather the common info in one section so as 
    to render the info in the GUI
'''

import os
import logging
from ptop.utils import ThreadJob


logger = logging.getLogger('ptop.statistics')


class Statistics:
    def __init__(self,sensors_list,stop_event):
        '''
            Record keeping for primitive system parameters
        '''
        self.plugin_dir = os.path.join(os.path.dirname(__file__),'plugins') #plugins directory
        self.plugins = sensors_list # plugins list
        self.statistics = {} # statistics object to be passed to the GUI
        for sensor in self.plugins:
            self.statistics[sensor.name] = sensor.currentValue
        self.stop_event = stop_event

    def generate(self):
        '''
            Generate the stats using the plugins list periodically
        '''
        for sensor in self.plugins:
            # update the sensors value periodically
            logger.info('Started thread job for the sensor {0}'.format(sensor))
            job = ThreadJob(sensor.update,self.stop_event,sensor.interval)
            job.start()



        

