// src/store/alertStore.js
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useAlertStore = defineStore('alert', () => {
    const alerts = ref([]);

    function addAlert(type, title, message) {
      const alert = {
        id: Date.now(),
        type,
        title,
        message,
        timestamp: Date.now(),
      };
      alerts.value.push(alert);

      // Optionally auto-remove the alert after a delay
      setTimeout(() => {
        removeAlert(alert.id);
      }, 5000); // Remove after 5 seconds
    }

    function removeAlert(id) {
      alerts.value = alerts.value.filter(alert => alert.id !== id);
    }

    function forceUpdate() {
        // Trigger reactivity by touching each alert
        alerts.value.forEach(alert => {
          alert.timestamp = alert.timestamp;
        });
      }
  
    return { alerts, addAlert, removeAlert, forceUpdate };
});
