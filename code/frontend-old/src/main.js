import { createApp } from 'vue';
import { createPinia } from 'pinia' // Import

import App from './App.vue';
import router from './router';

import 'bootstrap';

// Import custom CSS
import './scss/styles.scss'

// Import all of Bootstrap's JS
import * as bootstrap from 'bootstrap';
import "bootstrap-icons/font/bootstrap-icons.css"
window.bootstrap = bootstrap;

const pinia = createPinia();
const app = createApp(App);

app
  .use(pinia) // Create the root store
  .use(router)
  .mount('#app')