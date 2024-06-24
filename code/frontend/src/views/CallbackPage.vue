<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuth0 } from '@auth0/auth0-vue';

const { handleRedirectCallback } = useAuth0();
const router = useRouter();

onMounted(async () => {
  try {
    await handleRedirectCallback();
    router.push('/');
  } catch (error) {
    console.error('Error handling redirect callback:', error);
  }
});
</script>

<template>
  <div>Loading...</div>
</template>