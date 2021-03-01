import React from "react";
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import "leaflet-sidebar-v2";
import "./leaflet-sidebar.css";
import "./leaflet-sidebar.min.css";
import "./leaflet-sidebar.js";
import "./leaflet-sidebar.min.js";
import Sidebar from "./Sidebar";
class Map extends React.Component {
  componentDidMount() {
    // create map
    this.map = L.map("map", {
      renderer: L.canvas(),
      center: [37.09024, -95.712891],

      zoom: 4,
      layers: [
        L.tileLayer(
          "http://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}",
          {
            attribution:
              "&copy; <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a>"
          }
        )
      ]
    });
    var sidebar = L.control
      .sidebar({
        autopan: false,
        position: "right",
        container: "sidebar",
        closeButton: true
      })
      .addTo(this.map)
      .open("home");

    sidebar.on("content", function(ev) {
      switch (ev.id) {
        case "autopan":
          sidebar.options.autopan = true;
          break;
        default:
          sidebar.options.autopan = false;
      }
    });
  }
  datacallback = () => {
    console.log("hello");
    this.map.invalidateSize();
  };
  getAlert() {
    console.log("hello");
    this.map.invalidateSize();
  }

  render() {
    return (
      <div
        style={{
          height: "100vh"
        }}
        id="map"
      >
        <div id="sidebar" class="leaflet-sidebar collapsed">
          <div class="leaflet-sidebar-tabs">
            <ul role="tablist">
              <li role="tab">
                <a href="#home">
                  <i class="fa fa-bars" />
                </a>
              </li>
            </ul>
          </div>

          <div class="leaflet-sidebar-content">
            <div class="leaflet-sidebar-pane" id="home">
              <h1 class="leaflet-sidebar-header">
                Vehicles Details
                <div class="leaflet-sidebar-close">
                  <i class="fa fa-caret-left" />
                </div>
              </h1>
              <Sidebar />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Map;
