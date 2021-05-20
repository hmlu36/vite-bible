import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config';
import Panel from 'primevue/panel';
import Dropdown from 'primevue/dropdown';
import TabMenu from 'primevue/tabmenu';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import Tag from 'primevue/tag';

import 'primevue/resources/primevue.min.css';
import 'primevue/resources/themes/saga-green/theme.css';
import 'primeflex/primeflex.css';
import 'primeicons/primeicons.css';

createApp(App)
    .use(PrimeVue)
    .use(router)
    .component('Panel', Panel)
    .component('Dropdown', Dropdown)
    .component('TabMenu', TabMenu)
    .component('Button', Button)
    .component('InputText', InputText)
    .component('Tag', Tag)
    .mount('#app')
