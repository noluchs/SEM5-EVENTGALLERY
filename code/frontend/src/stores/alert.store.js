import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useAlertStore = defineStore('alert', () => {
    const alerts = ref([]);

    function addAlert(type, message) {
        alerts.value.push({ type, message });
    }

    function removeAlert(index) {
        alerts.value.splice(index, 1);
    }

    return {
        alerts,
        addAlert,
        removeAlert
    };
});