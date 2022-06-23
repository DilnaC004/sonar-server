//https://github.com/spmcneal/Medium-Flask/tree/main/Flask-Leaflet

var map = L.map("map").fitWorld();

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

markers = [
  { lat: 50.170751360207284, lon: 14.387907638083814 },
  { lat: 50.16603704625749, lon: 14.403228414674532 },
];

markers.forEach((m) => {
  L.marker([m.lat, m.lon]).addTo(map).bindPopup("hello");
});

map.flyTo([markers[0].lat, markers[1].lon], 18);
