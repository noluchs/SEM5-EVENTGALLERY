<script setup>
import { useAuth0 } from '@/plugins/auth0';

const logout = async () => {
  const auth0 = await useAuth0();
  auth0.logout({
    returnTo: window.location.origin
  });
};
</script>

<template>
  <button @click="logout">Logout</button>
</template>