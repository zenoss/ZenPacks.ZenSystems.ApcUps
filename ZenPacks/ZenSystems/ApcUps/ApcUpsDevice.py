##########################################################################
# Author:               Jane Curry,  jane.curry@skills-1st.co.uk
# Date:                 March 28th, 2011
# Revised:
#
# ApcPduDevice object class
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

from . import schema


class ApcUpsDevice(schema.ApcUpsDevice):
    """
    Custom model code for ApcUpsDevice class. We need this to
    install new Zenoss version on top of ZenSystems one
    """

    class_dynamicview_group = 'Devices'
