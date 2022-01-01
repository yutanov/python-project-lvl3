//nileMap
var leafletMapNm = {};
leafletMapNm.mapLayers = {};
var overlaysNm = {};
var baseMapsNm = {};
var mapNm;

//drainagePatternMap
var leafletMapDP = {};
leafletMapDP.mapLayers = {};
var overlaysDP = {};
var baseMapsDP = {};
var mapDP;

//alluviumMap
var leafletMapAlv = {};
leafletMapAlv.mapLayers = {};
var overlaysAlv = {};
var baseMapsAlv = {};
var mapAlv;

//nileMap
leafletMapNm.init = function () {
    var MapCentreNm = [30.9670, 31.1670];
    var initZoomNm = 8;
    var southWestNm = L.latLng(-89.98155760646617, -180);
    var northEastNm = L.latLng(89.99346179538875, 180);
    var boundsNm = L.latLngBounds(southWestNm, northEastNm);

    /** Create the Leaflet map instance */
    mapNm = L.map('nileMap', {
        center: MapCentreNm,
        zoom: initZoomNm,
        maxBounds: boundsNm,
        fullscreenControl: true
    });

//ref https://esri.github.io/esri-leaflet/api-reference/layers/basemap-layer.html
    var imageryNm = L.esri.basemapLayer("Imagery").addTo(mapNm);    
    baseMapsNm["<img width='20' height='20' src='/js/leafletmaps/images/imagery.png' /> <span style='vertical-align: top; color: black; font-size: 12px;'>Satellite Imagery</span>"] = imageryNm;

    /** Restrict the map to one Earth */
    mapNm.on('drag', function () {
        mapNm.panInsideBounds(boundsNm, { animate: false });
    });

    /** Add scale control to map */
    L.control.scale().addTo(mapNm);

    return true;
}

//drainagePatternMap
leafletMapDP.init = function () {
    var MapCentreDP = [15.989186, 50.135108];
    var initZoomDP = 9;
    var southWestDP = L.latLng(-89.98155760646617, -180);
    var northEastDP = L.latLng(89.99346179538875, 180);
    var boundsDP = L.latLngBounds(southWestDP, northEastDP);

    /** Create the Leaflet map instance */
    mapDP = L.map('drainagePatternMap', {
        center: MapCentreDP,
        zoom: initZoomDP,
        maxBounds: boundsDP,
        fullscreenControl: true
    });

//ref https://esri.github.io/esri-leaflet/api-reference/layers/basemap-layer.html
    var imageryDP = L.esri.basemapLayer("Imagery").addTo(mapDP);   
    baseMapsDP["<img width='20' height='20' src='/js/leafletmaps/images/imagery.png' /> <span style='vertical-align: top; color: black; font-size: 12px;'>Satellite Imagery</span>"] = imageryDP;

    /** Restrict the map to one Earth */
    mapDP.on('drag', function () {
        mapDP.panInsideBounds(boundsDP, { animate: false });
    });

    /** Add scale control to map */
    L.control.scale().addTo(mapDP);

/** Add WMS to map to show geology */
    var theWmsURL_1 = "http://mapsref.brgm.fr/wxs/1GG/YGSMRB_Bedrock_and_Structural_Geology?";
    var theLayerCode_1 = "YEM_YGSMRB_1M_Superficial";
    var theWMS_1 = L.tileLayer.wms( theWmsURL_1, {
      layers: theLayerCode_1,
      format: 'image/png',
      transparent: true,
      attribution: "YGSMRB",
      version: '1.3.0',
      crs: L.CRS.EPSG4326,
      zIndex: 3
    }).addTo(mapDP);

    return true;
}

//alluviumMap
leafletMapAlv.init = function () {
    var MapCentreAlv = [53.2, -1.25];
    var initZoomAlv = 8;
    var southWestAlv = L.latLng(-89.98155760646617, -180);
    var northEastAlv = L.latLng(89.99346179538875, 180);
    var boundsAlv = L.latLngBounds(southWestAlv, northEastAlv);

    /** Create the Leaflet map instance */
    mapAlv = L.map('alluviumMap', {
        center: MapCentreAlv,
        zoom: initZoomAlv,
        maxBounds: boundsAlv,
        fullscreenControl: true
    });

//ref https://esri.github.io/esri-leaflet/api-reference/layers/basemap-layer.html
    var imageryAlv = L.esri.basemapLayer("Imagery").addTo(mapAlv);   
    baseMapsAlv["<img width='20' height='20' src='/js/leafletmaps/images/imagery.png' /> <span style='vertical-align: top; color: black; font-size: 12px;'>Satellite Imagery</span>"] = imageryAlv;

    /** Restrict the map to one Earth */
    mapAlv.on('drag', function () {
        mapAlv.panInsideBounds(boundsAlv, { animate: false });
    });

    /** Add scale control to map */
    L.control.scale().addTo(mapAlv);

/** Add WMS to map to show geology */
    var theWmsURL_1 = "http://ogc.bgs.ac.uk/cgi-bin/BGS_Bedrock_and_Superficial_Geology/ows?";
    var theLayerCode_1 = "GBR_BGS_625k_SLS";
    var theWMS_1 = L.tileLayer.wms( theWmsURL_1, {
      layers: theLayerCode_1,
      format: 'image/png',
      transparent: true,
      attribution: "British Geological Survey (BGS)",
      version: '1.3.0',
      crs: L.CRS.EPSG4326,
      zIndex: 3
    }).addTo(mapAlv);

    return true;
}

$(document).ready(leafletMapNm.init);
$(document).ready(leafletMapDP.init);
$(document).ready(leafletMapAlv.init);