<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/stores/auth.store';
import { useRouter } from 'vue-router';

const router = useRouter();
const authStore = useAuthStore();

const password = ref('');
const username = ref('');

async function onSubmit() {
    try {
        await authStore.login(username.value, password.value);
        router.push('/admin'); // Redirect to admin dashboard after login
    } catch (error) {
        console.error('Login failed:', error);
        // Handle login error (e.g., show an error message)
    }
}
</script>

<template>
  <main class="form-signin w-100 m-auto">
    <form @submit.prevent="onSubmit">
      <h1 class="h3 mb-3 fw-normal">Please Login</h1>
      <div class="form-floating">
        <input type="email" class="form-control" v-model="username" id="floatingInput" placeholder="name@example.com">
        <label for="floatingInput">Email address</label>
      </div>
      <div class="form-floating">
        <input type="password" class="form-control" v-model="password" id="floatingPassword" placeholder="Password">
        <label for="floatingPassword">Password</label>
      </div>
      <div class="form-check text-start my-3">
        <input class="form-check-input" type="checkbox" value="remember-me" id="flexCheckDefault">
        <label class="form-check-label" for="flexCheckDefault">
          Remember me
        </label>
      </div>
      <button class="btn btn-primary w-100 py-2" type="submit">Login</button>
      <router-link to="/register" v-slot="{ navigate }">
        <button class="btn btn-link" @click="navigate">Register</button>
      </router-link>
    </form>
  </main>
</template>

<style scoped>
html,
body {
  height: 100%;
}

.form-signin {
  max-width: 330px;
  padding: 1rem;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>