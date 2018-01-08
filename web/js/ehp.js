var format = "image/png";
var projection = new ol.proj.Projection({
  code: "EPSG:4326",
  units: "degrees",
  axisOrientation: "neu",
  global: false
});
var bounds = [
  112.7741790372,
  -1.6093271348800289,
  112.89911676039605,
  -1.5474746356
];

var map = new ol.Map({
  layers: [
    new ol.layer.Tile({
      source: new ol.source.OSM(),
      opacity: 0.7
    }),
    new ol.layer.Tile({
      source: new ol.source.TileWMS({
        url: "http://localhost:8080/geoserver/ehp/wms",
        params: {
          format: format,
          versioN: "1.1.1",
          tiled: true,
          styles: "",
          layers: "ehp:ehp_base",
          tilesOrigin: bounds[0] + "," + bounds[1]
        }
      }),
      opacity: 1.0
    })
  ],
  target: "map",
  controls: ol.control.defaults({
    attributionOptions: {
      collapsible: true
    }
  }),
  view: new ol.View({
    projection: projection
  })
});

map.getView().fit(bounds, map.getSize());
