##############################################################################
#
# Copyright (C) Zenoss, Inc. 2015, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

from zope.interface import implements
from zope.component import adapts

from Products.Zuul.interfaces import IReportable
from ZenPacks.zenoss.ZenETL.reportable import\
    (DEFAULT_STRING_LENGTH, DeviceReportable, BaseReportable)
from .ApcUpsDevice import ApcUpsDevice
from .ApcUpsBattery import ApcUpsBattery


class ApcUpsDeviceReportable(DeviceReportable):
    adapts(ApcUpsDevice)
    implements(IReportable)

    def reportProperties(self):

        result = super(ApcUpsDeviceReportable, self).reportProperties()
        result.append(('numBatteryPacks', 'string',
                       self.context.numBatteryPacks, DEFAULT_STRING_LENGTH))
        result.append(('numBadBatteryPacks', 'string',
                       self.context.numBadBatteryPacks, DEFAULT_STRING_LENGTH))
        result.append(('basicOutputStatus', 'string',
                       self.context.basicOutputStatus, DEFAULT_STRING_LENGTH))
        result.append(('basicOutputStatusText', 'string',
                       self.context.basicOutputStatusText, DEFAULT_STRING_LENGTH))
        return result


class ApcUpsBatteryReportable(BaseReportable):
    adapts(ApcUpsBattery)
    implements(IReportable)

    def reportProperties(self):
        eclass = self.entity_class_name
        for entry in super(ApcUpsBatteryReportable, self).reportProperties():
            yield entry
        yield (eclass + '_name', 'string', self.context.titleOrId(),
               DEFAULT_STRING_LENGTH)
