/** @odoo-module **/

import publicWidget from "web.public.widget";

publicWidget.registry.SchoolInfo = publicWidget.Widget.extend({
  selector: ".school-info",
  start() {
    let citiesRaw = this.el.querySelector("#info-school-raw");

    if (citiesRaw) {
      this._rpc({
        route: "/schools",
        paramas: {},
      }).then((data) => {
        let html = ``;
        data.forEach((city) => {
          html += `<div class="col-lg-3 mb-5">
          <div class="text-center">
              <div class="img-container mb-2">
                  <img class="country-image rounded" src="data:image/png;base64,${
                    city.image
                  }" style="max-width: 120px; height: auto; box-shadow: 0px 0px 10px rgba(0,0,0,0.3);"/>
              </div>
              <div>
                  <h5 class="mb-1" style="font-size: 18px;">${
                    city.school_name ? city.school_name : ""
                  }</h5>
                  <div>${city.state_id ? city.state_id[1] : ""}</div>
                  <div>${city.country_id ? city.country_id[1] : ""}</div>
              </div>
          </div>
      </div>`;
        });
        citiesRaw.innerHTML = html;
      });
    }
  },
});

export default publicWidget.registry.SchoolInfo;
