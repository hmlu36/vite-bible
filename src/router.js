import { createWebHistory, createRouter } from "vue-router";

import Home from './pages/Home.vue';
import Query from './pages/Query.vue';
import About from './pages/About.vue';


const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home,
        },
        {
            path: '/query',
            name: 'query',
            component: Query,
        },
        {
            path: '/about',
            name: 'about',
            component: About,
        },
    ]
});


export default router;