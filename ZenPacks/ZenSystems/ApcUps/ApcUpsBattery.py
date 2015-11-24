##############################################################################
#
# Copyright (C) Zenoss, Inc. 2015, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

from . import schema
from Products.ZenRelations.RelSchema import *


class ApcUpsBattery(schema.ApcUpsBattery):
    """
    Custom model code for ApcUpsBattery class. We need old relations
    to update existing instances such as object path
    """

    class_dynamicview_group = 'Aps Ups Batterys'
    impacts = ['apcUpsDevice', ]

schema.ApcUpsBattery._relations += (
    ("ApcUpsDevBat", ToOne(ToManyCont,
     "ZenPacks.ZenSystems.ApcUps.ApcUpsDevice", "ApcUpsBat")),)
