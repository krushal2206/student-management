/** @odoo-module **/

import options from "web_editor.snippets.options";

options.registry.ExploreSchoolOptions = options.Class.extend({
  start() {
    let citiesRow = this.$target.find("#info-school-raw");

    if (citiesRow) {
      this._rpc({
        route: "/cities/",
        params: {},
      }).then((data) => {
        let html = ``;
        data.forEach((city) => {
          html += `<div class="col-lg-3 mb-5">
          <div class="text-center">
              <div class="img-container mb-2">
                  <img class="country-image rounded" src="data:image/png;base64,${
                    city.image
                  }" style="width: 200px; height: 150px; box-shadow: 0px 0px 10px rgba(0,0,0,0.3);"/>
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
        citiesRow.html(html);
      });
    }
  },
});

export default {
  ExploreSchoolOptions: options.registry.ExploreSchoolOptions,
};
