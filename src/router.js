// router.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from './components/Home.vue';
import SearchPage from './components/SearchPage.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/search', component: SearchPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
