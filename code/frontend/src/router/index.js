import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import LoginPage from '@/views/LoginPage.vue';
import CallbackPage from '@/views/CallbackPage.vue';
import AdminDashboard from '@/views/AdminDashboard.vue';
import GalleryPage from '@/views/GalleryPage.vue'; // Import GalleryPage component
import { authGuard } from '@auth0/auth0-vue';

const routes = [
  { path: '/', component: HomeView },
  { path: '/login', component: LoginPage },
  { path: '/callback', component: CallbackPage },
  {
    path: '/admin',
    component: AdminDashboard,
    beforeEnter: authGuard
  },
  { path: '/gallery/:id', component: GalleryPage } // Add GalleryPage route
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;