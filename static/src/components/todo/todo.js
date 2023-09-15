//**@odoo-module */
import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";

//Root class
class TodoList extends Component {
  setup() {
    this.state = useState({
      tasks: [],
      newTask: "",
    });

    console.log("Yeah! It's working");

    this.addTask = () => {
      console.log("ADD");
      if (this.state.newTask.trim()) {
        this.state.tasks.push(this.state.newTask);
        console.log();
        this.state.newTask = "";
      }
    };

    this.deleteTask = (taskIndex) => {
      console.log("Deleted");
      this.state.tasks.splice(taskIndex, 1);
    };
  }
}

TodoList.components = {};
TodoList.template = "school_management.todolist";

registry.category("actions").add("school_management.todo", TodoList);
