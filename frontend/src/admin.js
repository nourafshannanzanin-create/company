import { createApp } from "vue";
import AdminApp from "./AdminApp.vue";
import "../styles.css";

document.documentElement.classList.add("js");

createApp(AdminApp).mount("#app");
