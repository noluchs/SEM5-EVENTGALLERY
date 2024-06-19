import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import GalleryPage from '../views/GalleryPage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/gallery/:id',
    name: 'GalleryPage',
    component: GalleryPage
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router