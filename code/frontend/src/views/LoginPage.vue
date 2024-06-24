<script setup>
  import { useAuth0 } from '@auth0/auth0-vue';
  const { loginWithRedirect } = useAuth0();
  function login() {
  loginWithRedirect();
}
</script>

<template>
  <main class="form-signin w-100 m-auto">
    <h1 class="h3 mb-3 fw-normal">Please Login</h1>
    <button class="btn btn-primary w-100 py-2" @click="login">Login with Auth0</button>
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
</style>