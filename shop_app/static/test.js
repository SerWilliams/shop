Ext.onReady(function(){
     Ext.define('Shops', {
     extend: 'Ext.data.Model',
     fields: [
         {name: 'name', type: 'string'},
         {name: 'code',  type: 'int'},
         {name: 'address',  type: 'string'},
         {name: 'active',  type: 'boolean'},
         // {name: 'last_date',  type: 'string'},
         // {name: 'id',  type: 'int'},
         ]
     });

     var myStore = Ext.create('Ext.data.Store', {
         model: 'Shops',
         proxy: {
             type: 'ajax',
             url: '/shops',
             reader: {
                 type: 'json',
                 rootProperty: 'shops'
             }
         },
         autoLoad: true
     });

    Ext.create('Ext.grid.Panel', {
        title:'Shops',
        renderTo: Ext.getBody(),
        store: myStore,
        // width: 1000,
        // height: 400,
        padding:10,
        bodyPadding:5,
        columns : [{
            text: 'Код',
            dataIndex: 'code',
         },{
            text: 'Наименование',
            dataIndex: 'name',
            width: 150,
         },{
            text: 'Адрес',
            dataIndex: 'address',
            width: 200,
         },{
            text: 'Активный',
            dataIndex: 'active',
         }],
    });
});

// Ext.onReady(function() {
//     var store = Ext.create('Ext.data.Store', {
//         fields: ['name', 'email', 'phone'],
//         data: [
//             {'name': 'Lisa', "email": "lisa@simpsons.com", "phone": "555-111-1224"},
//             {'name': 'Bart', "email": "bart@simpsons.com", "phone": "555-222-1234"},
//             {'name': 'Homer', "email": "home@simpsons.com", "phone": "555-222-1244"},
//             {'name': 'Marge', "email": "marge@simpsons.com", "phone": "555-222-1254"}
//         ]
//     });
//
// Ext.create('Ext.grid.Panel', {
//     title: 'Simpsons',
//
//     store: store,
//
//     columns: [
//         { text: 'Name',  dataIndex: 'name', width: 200 },
//         { text: 'Email', dataIndex: 'email', width: 250 },
//         { text: 'Phone', dataIndex: 'phone', width: 120 }
//     ],
//
//     height: 200,
//     layout: 'fit',
//     fullscreen: true
// });
// });