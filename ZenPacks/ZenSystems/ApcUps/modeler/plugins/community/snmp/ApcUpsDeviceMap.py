##########################################################################
# Author:               Jane Curry,  jane.curry@skills-1st.co.uk
# Date:                 March 28th, 2011
# Revised:
#
# ApcUpsDevice modler plugin
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

import logging
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap
from Products.DataCollector.plugins.DataMaps import MultiArgs

log = logging.getLogger('zen.ApcUps')

Manufacturer = "American Power Conversion Corp."

basicOutputStatusMap = {1: 'Unknown',
                        2: 'onLine',
                        3: 'onBattery',
                        4: 'onSmartBoost',
                        5: 'timedSleeping',
                        6: 'softwareBypass',
                        7: 'off',
                        8: 'rebooting',
                        9: 'switchedBypass',
                        10: 'hardwareFailureBypass',
                        11: 'sleepingUntilPowerReturn',
                        12: 'onSmartTrim'}


class ApcUpsDeviceMap(SnmpPlugin):
    maptype = "ApcUpsDeviceMap"

    snmpGetMap = GetMap({
        '.1.3.6.1.4.1.318.1.1.1.1.1.1.0': 'setHWProductKey',
        '.1.3.6.1.4.1.318.1.1.1.1.2.1.0': 'setOSProductKey',
        '.1.3.6.1.4.1.318.1.1.1.1.2.3.0': 'setHWSerialNumber',
        '.1.3.6.1.4.1.318.1.1.1.2.2.5.0': 'numBatteryPacks',
        '.1.3.6.1.4.1.318.1.1.1.2.2.6.0': 'numBadBatteryPacks',
        '.1.3.6.1.4.1.318.1.1.1.4.1.1.0': 'basicOutputStatus'})

    def condition(self, device, log):
        return device.snmpOid.startswith(".1.3.6.1.4.1.318.1.3.2")

    def process(self, device, results, log):

        log.info('processing {} for device {}'.format(self.name(), device.id))
        getdata, tabledata = results
        if not getdata:
            log.warn(' No response from {} for the {} plugin '.format(
                     device.id, self.name()))
            return
        om = self.objectMap(getdata)
        try:

            om.setHWProductKey = MultiArgs(om.setHWProductKey, Manufacturer)
            om.setOSProductKey = MultiArgs(om.setOSProductKey, Manufacturer)

            if (om.basicOutputStatus < 1 or om.basicOutputStatus > 12):
                om.basicOutputStatus = 1
            om.basicOutputStatusText = basicOutputStatusMap[om.basicOutputStatus]
        except (KeyError, IndexError, AttributeError, TypeError), e:
            log.warn(' Error in ApcUpsDeviceMap modeler plugin {}'.format(e))

        return om
