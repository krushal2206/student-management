/** @odoo-module **/
import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";

class AwesomeDashboard extends Component {}

// AwesomeDashboard.components = {};
AwesomeDashboard.template = "school_management.clientaction2";

class TodoTask extends Component {
  //   static Component = { AwesomeDashboard };
  //   btn = useRef("btn");
  //   btnn = useRef("btn");
  setup() {
    this.count = useState({ value: 1 });
    this.down = useState({ value: 100 });
  }

  increment() {
    this.count.value++;
  }
  decrement() {
    this.down.value--;
  }
}

TodoTask.components = { AwesomeDashboard };
TodoTask.template = "school_management.clientaction3";

registry.category("actions").add("school_management.dashboard2", TodoTask);
