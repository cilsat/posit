var mymap = L.map("mapid").setView([-1.59, 112.84], 13);

var mbs = L.tileLayer(
  "https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw",
  {
    maxZoom: 18,
    attribution:
      'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
      '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
      'Imagery © <a href="http://mapbox.com">Mapbox</a>',
    id: "mapbox.streets"
  }
);

var ehp_ortho = L.tileLayer.wms("http://localhost:8080/geoserver/ehp/wms", {
  layers: "ehp:ehp_base",
  format: "image/png",
  maxZoom: 20,
  id: "ehp.base"
});

var ehp_block = L.tileLayer.wms("http://localhost:8080/geoserver/ehp/wms", {
  layers: "ehp:pg_block",
  format: "image/png",
  transparent: true,
  maxZoom: 20,
  id: "ehp.block"
});

var ehp_sawit = L.tileLayer.wms("http://localhost:8080/geoserver/ehp/wms", {
  layers: "ehp:pg_sawit",
  format: "image/png",
  transparent: true,
  maxZoom: 20,
  id: "ehp.sawit"
});

//mbs.addTo(mymap);
ehp_ortho.addTo(mymap);
ehp_block.addTo(mymap);
ehp_sawit.addTo(mymap);
