<!-- src/components/AlertToast.vue -->
<template>
  <div class="toast-container position-fixed bottom-0 end-0 p-3">
    <div v-for="alert in alerts" :key="alert.id"
         class="toast show"
         :class="getToastClass(alert.type)"
         role="alert"
         aria-live="assertive"
         aria-atomic="true">
      <div class="toast-header">
        <strong class="me-auto">{{ alert.title }}</strong>
        <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close" @click="dismissAlert(alert.id)"></button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAlertStore } from '@/stores/alert.store';
import { computed } from 'vue';

const store = useAlertStore();
const alerts = computed(() => store.alerts.map(alert => ({
  ...alert,
})));

function getToastClass(type) {
  switch (type) {
    case 'info':
        return 'bg-info text-white';
    case 'error':
        return 'bg-danger text-white';
    case 'success':
        return 'bg-success text-white';
    case 'warning':
        return 'bg-warning text-white';
    default:
        return 'bg-secondary text-dark';
  }
}

function dismissAlert(id) {
  store.removeAlert(id);
}
</script>
