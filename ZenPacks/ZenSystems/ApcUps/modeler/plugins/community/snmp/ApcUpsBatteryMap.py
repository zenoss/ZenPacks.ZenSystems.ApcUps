##########################################################################
# Author:               Jane Curry,  jane.curry@skills-1st.co.uk
# Date:                 March 28th, 2011
# Revised:
#
# ApcUpsBattery modeler plugin
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

import logging
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap

log = logging.getLogger('zen.ApcUps')

BatteryStatusMap = {1: (2, 'Status Unknown'),
                    2: (0, 'Status Normal'),
                    3: (5, 'Battery Low')}

BatteryReplaceIndicatorMap = {0: (2, ' Status Unknown'),
                              1: (0, 'OK'),
                              2: (5, 'Battery needs replacing')}


class ApcUpsBatteryMap(SnmpPlugin):
    """Map APC UPS Battery table to model."""
    compname = ""
    maptype = "ApcUpsBatteryMap"
    modname = "ZenPacks.ZenSystems.ApcUps.ApcUpsBattery"
    relname = "apcUpsBatterys"

    snmpGetMap = GetMap({
        '.1.3.6.1.4.1.318.1.1.1.2.1.1.0': 'batteryStatus',
        '.1.3.6.1.4.1.318.1.1.1.2.1.2.0': 'timeOnBattery',
        '.1.3.6.1.4.1.318.1.1.1.2.1.3.0': 'batteryLastReplacementDate',
        '.1.3.6.1.4.1.318.1.1.1.2.2.4.0': 'batteryReplaceIndicator'})

    def process(self, device, results, log):

        log.info('processing {} for device {}'.format(self.name(), device.id))
        getdata, tabledata = results
        rm = self.relMap()
        if not getdata:
            log.warn(' No response from {} for the {} plugin'.format(
                     device.id, self.name()))
            return

        om = self.objectMap(getdata)
        try:
            # timeOnBattery is in timeticks (1/100 sec)
            om.timeOnBattery = om.timeOnBattery / 6000
            om_id = "ApcUpsBattery"
            om.id = self.prepId(om_id)

            # Transform batteryReplaceIndicator into a status
            if (om.batteryReplaceIndicator < 1 or om.batteryReplaceIndicator > 2):
                om.batteryReplaceIndicator = 0
            values = BatteryReplaceIndicatorMap[om.batteryReplaceIndicator]
            om.batteryReplaceIndicator, om.batteryReplaceIndicatorText = values

            # Transform battery status into a severity number
            if (om.batteryStatus < 1 or om.batteryStatus > 3):
                om.batteryStatus = 1
            index = om.batteryStatus
            om.batteryStatus, om.batteryStatusText = BatteryStatusMap[index]

            om.snmpindex = '0'
            rm.append(om)
        except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
            log.warn(' Error in ApcUpsBatteryMap modeler plugin %s', errorInfo)
        return rm




