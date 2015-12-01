##############################################################################
#
# Copyright (C) Zenoss, Inc. 2015, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################
from zope.event import notify
from Products.Zuul.catalog.events import IndexingEvent
from Products.ZenModel.migrate.Migrate import Version
from Products.ZenModel.ZenPack import ZenPackMigration
import logging

log = logging.getLogger("zen.migrate")


class UpdateRelations(ZenPackMigration):
    """
    Update relations for NetAppInterface component
    """
    version = Version(1, 2, 0)

    def migrate(self, pack):
        import pdb; pdb.set_trace()
        _log = logging.getLogger('Zope.ZCatalog')
        _log.setLevel(logging.FATAL)
        log.info(
            "Update relations for /Power/UPS/ApcUps devices"
        )

        dc = pack.dmd.Devices.getOrganizer('/Power/UPS/ApcUps')
        for dev in dc.getDevices():

            log.info('Update relations for {0}'.format(dev.name()))
            dev.buildRelations()
            components = []

            for battery in dev.ApcUpsBat():
                log.info('Remove old relation for {0} in {1}'.format(
                    battery.name(), dev.name()))
                dev.ApcUpsBat._delObject(battery.id)
                components.append(battery)

            for comp in components:
                log.info('Add new relation for {0} in {1}'.format(comp.name(),
                                                                  dev.name()))
                comp.buildRelations()
                dev.apcUpsBatterys._setObject(comp.id, comp)
                comp.index_object()
            dev.index_object()
            # indexing devices and components for impact after updating
            notify(IndexingEvent(dev))
            for component in dev.getDeviceComponents():
                notify(IndexingEvent(component))

UpdateRelations()
