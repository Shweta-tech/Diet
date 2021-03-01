angular.module('ui.bootstrap.demo', ['ngAnimate', 'ui.bootstrap']);
angular.module('ui.bootstrap.demo').controller('DropdownCtrl', function($scope) {
    var map = new L.Map('map', {
        zoom: 10,
        minZoom: 8,
        maxZoom: 12
    });
    var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var osm = new L.TileLayer(osmUrl, { minZoom: 8, maxZoom: 12 });
    map.setView(new L.LatLng(-36.5, 143.98), 6);
    map.addLayer(osm);

    // Try to comment following lines to group the button and dropdown list
    var sidebar = L.control.sidebar('sidebar', {
        position: 'left'
    });

    map.addControl(sidebar);
    sidebar.show();

});