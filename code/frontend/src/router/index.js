import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import GalleryPage from '../views/GalleryPage.vue';
import LoginPage from '../views/LoginPage.vue'; // Updated name
import AdminDashboard from '../views/AdminDashboard.vue';

const routes = [
  { path: '/', name: 'Home', component: HomeView },
  { path: '/gallery/:id', name: 'Gallery', component: GalleryPage },
  { path: '/login', name: 'LoginPage', component: LoginPage }, // Updated name
  { path: '/admin', name: 'Admin', component: AdminDashboard }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;