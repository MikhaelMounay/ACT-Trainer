import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
import MathJax, { initMathJax, renderByMathjax } from "mathjax-vue3";
import VueMobileDetection from "vue-mobile-detection";

initMathJax(
  { url: "https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-chtml-full.js" },
  () => {
    renderByMathjax(document.getElementById("app"));
  }
);

createApp(App)
  .use(store)
  .use(router)
  .use(MathJax)
  .use(VueMobileDetection)
  .mount("#app");
