<script setup>

import { storeToRefs } from 'pinia'
import { useAuthStore } from '@/stores/auth.store'

import { useRouter } from "vue-router";
const router = useRouter();

const { token, user } = storeToRefs(useAuthStore())

const handleLogout = () => {
    const authStore = useAuthStore();
    authStore.logout()
};

const handleLogin = () => {
  router.push('/login')
}


</script>
 

<template>
  <nav class="navbar navbar-expand-lg bg-primary" data-bs-theme="dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">micro Adventures</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarColor01" aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarColor01">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <RouterLink to="/" class="nav-link">Home
              <span class="visually-hidden">(current)</span>
            </RouterLink>
          </li>
          <div class="nav-item">
              <RouterLink to="/all-rooms" class="nav-link">Rooms</RouterLink>
          </div>
          <div class="nav-item">
              <RouterLink to="/all-games" class="nav-link">Games</RouterLink>
          </div>
          <div class="nav-item">
              <RouterLink to="/invite" class="nav-link">Invite</RouterLink>
          </div>
        </ul>
        <div v-if="user" class="fw-lighter">{{ user.name }}</div>
        <div v-if="token"><button type="button" class="btn btn-primary" @click="handleLogout">Log Out</button></div>
        <div v-else><button type="button" class="btn btn-primary" @click="handleLogin">Log In</button></div>
      </div>
    </div>
  </nav>

</template>