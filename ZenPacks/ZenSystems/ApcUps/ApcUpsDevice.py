##############################################################################
#
# Copyright (C) Zenoss, Inc. 2015, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

# ZenPack Imports
from . import schema
from Products.ZenRelations.RelSchema import *


class ApcUpsDevice(schema.ApcUpsDevice):
    """Custom model code for ApcUpsDevice class."""

    class_dynamicview_group = 'Devices'
    impacted_by = ['apcUpsBatterys', ]

schema.ApcUpsDevice._relations += (
    ('ApcUpsBat', ToManyCont(ToOne,
     'ZenPacks.ZenSystems.ApcUps.ApcUpsBattery', 'ApcUpsDevBat')),)
