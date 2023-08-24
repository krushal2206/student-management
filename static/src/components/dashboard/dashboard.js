/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

class AwesomeDashboard extends Component {}

AwesomeDashboard.components = {};
AwesomeDashboard.template = "school_management.clientaction";

registry
  .category("actions")
  .add("school_management.dashboard", AwesomeDashboard);
