/** @odoo-module **/

import { Component, useRef } from "@odoo/owl";
import { registry } from "@web/core/registry";

class AwesomeDashboard extends Component {}

AwesomeDashboard.components = {};
AwesomeDashboard.template = "school_management.clientaction";

registry.category("actions").add("school_management.dashboard", AwesomeDashboard);

// class Increment extends Component {
//   btn = useRef("btn");
//   setup() {
//     this.num = useState({ value: 0 });
//   }

//   increment() {
//     this.num.value++;

//   }
// }
// Increment.components = {};
// Increment.template = "school_management.clientaction1";

// registry.category("actions").add("school_management.dashboard1", Increment);
