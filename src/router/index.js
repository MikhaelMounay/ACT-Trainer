import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import TestsView from "../views/TestsView.vue";
import LiveTestView from "../views/LiveTestView.vue";
import Score_AnswersView from "../views/Score_AnswersView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/tests",
    name: "tests",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: TestsView,
  },
  {
    path: "/livetest/:testId/:testType/",
    name: "livetest",
    component: LiveTestView,
  },
  {
    path: "/score_answers/:testId/",
    name: "score_answers",
    component: Score_AnswersView,
  },
];

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes,
});

export default router;
