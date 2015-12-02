(function(){
    Ext.onReady(function(){
    var DEVICE_OVERVIEW_PANEL = 'device_overview';
    var path = window.location.href;
    if (path.indexOf('/Devices/Power/UPS/ApcUps/devices') > 0){
        Ext.define("Zenoss.DeviceOverviewFormUps", {
            alias:['widget.devformpanelups'],
            extend:"Zenoss.DeviceOverviewForm",
            defaultType: 'displayfield',
            frame:false,
            flex: 1,
            bodyStyle: 'background-color:#fafafa;',
            minHeight: 400,
            items: [{
                fieldLabel: _t('Number Battery Packs'),
                name: 'numBatteryPacks',
                id: 'numbatterypacks-label1'
            },{
                fieldLabel: _t('Number Bad Battery Packs'),
                name: 'numBadBatteryPacks',
                id: 'numbadbatterypacks-label1'
            },{
                fieldLabel: _t('Basic Output Status'),
                name: 'basicoutputstatus',
                id: 'basicoutputstatus-label1'
            },{
                fieldLabel: _t('Basic Output Status Text'),
                autoWidth: true,
                name: 'basicOutputStatusText',
                id: 'basicoutputstatustext-label1'
            }]
        })
        Ext.ComponentMgr.onAvailable(DEVICE_OVERVIEW_PANEL, function(){
            var newel = Ext.create("Zenoss.DeviceOverviewFormUps");
            this.items.items[1].items.add(newel)
            this.forms.push(newel);
        });
    };
});

})();