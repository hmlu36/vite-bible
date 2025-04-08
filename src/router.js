// router.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from './views/Home.vue';
import SearchPage from './views/SearchPage.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/search', component: SearchPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
