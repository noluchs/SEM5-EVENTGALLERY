import { defineStore } from 'pinia';
import { ref } from 'vue';
import axios from 'axios';
import router from '../router';
import { useAlertStore } from '@/stores/alert.store';

export const useAuthStore = defineStore('auth', () => {
    const token = ref(JSON.parse(localStorage.getItem('token')));
    const user = ref(JSON.parse(localStorage.getItem('user')));
    const returnUrl = ref(null);
    const alertStore = useAlertStore(); // Initialize once, use everywhere

    function saveUser(newUser) {
        user.value = newUser;
        localStorage.setItem('user', JSON.stringify(newUser));
    }

    function clearUser() {
        user.value = null;
        localStorage.removeItem('user');
    }

    function saveToken(newToken) {
        token.value = newToken;
        localStorage.setItem('token', JSON.stringify(newToken));
    }

    function clearToken() {
        token.value = null;
        localStorage.removeItem('token');
    }

    async function handleApiCall(config, successMessage) {
        try {
            const response = await axios(config);
            if (successMessage) {
                alertStore.addAlert('success', successMessage);
            }
            return { data: response.data, error: null };
        } catch (error) {
            alertStore.addAlert('error', error.response.data.message || 'An error occurred');
            return { data: null, error: error.response.data };
        }
    }

    async function login(email, password) {
        const config = {
            url: 'http://localhost:5001/users/login',
            method: "POST",
            data: { email, password }
        };
        const { data } = await handleApiCall(config);
        if (data) {
            saveToken(data.token);
            // User data might need to be fetched separately if not included in the login response
            saveUser({ email }); // Adjust as necessary if user data is returned
            router.push(returnUrl.value || '/');
        }
    }

    function logout() {
        clearToken();
        clearUser();
        router.push('/login');
    }

    return {
        token,
        user,
        returnUrl,
        login,
        logout
    };
});