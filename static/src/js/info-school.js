/** @odoo-module **/

import publicWidget from "web.public.widget";
import core from "web.core";

var Qweb = core.qweb;

publicWidget.registry.SchoolInfo = publicWidget.Widget.extend({
  selector: ".school-info",
  start() {
    this._rpc({
      route: "/schools",
      paramas: {},
    }).then((data) => {
      this.$target.replaceWith(
        Qweb.render("school_management.school_qweb", { school: data })
      );
      console.log(data);
    });
  },
});

export default publicWidget.registry.SchoolInfo;




