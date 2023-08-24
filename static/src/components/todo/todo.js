//**@odoo-module */
import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

//Root class
class TodoList extends Component {
  setup() {}
}

TodoList.components = {};
TodoList.template = "school_management.todolist";

registry.category("actions").add("school_management.todo", TodoList);
