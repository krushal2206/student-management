/** @odoo-module **/

import { Component, useState } from "@odd/owl";
import { registry } from "@web/core/registry";

class increseNumber extends Component {
  setup() {
    this.num = useState({
      count: 0,
    });

    // // click event
    // this.onClick = this.onClick.bind(this);
    // // this.el.addEventListener("Click", this.onClick());
    // this.el.addEventListener("click", this.onClick);
  }

  onClick() {
    this.num.count += 1;
    // this.render();
  }
}
increseNumber.template = "school_management.clientactioncounter";

registry.category("actions").add("school_management.counter", increseNumber);
// export default increseNumber;
