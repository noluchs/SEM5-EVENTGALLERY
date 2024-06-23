// path: src/stores/auth.store.js
import { defineStore } from 'pinia';
import { ref } from 'vue';
import { callExternalApi } from "../services/ExternalApiService";
import router from '../router';
import { useAlertStore } from '@/stores/alert.store';

export const useAuthStore = defineStore('auth', () => {
    const token = ref(getItemFromLocalStorage('token'));
    const user = ref(getItemFromLocalStorage('user'));
    const returnUrl = ref(null);
    const alertStore = useAlertStore(); // Initialize once, use everywhere

    function getItemFromLocalStorage(key) {
        try {
            return JSON.parse(localStorage.getItem(key)) || null;
        } catch (error) {
            return null;
        }
    }

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
            const { data, error } = await callExternalApi({ config });
            if (error) {
                alertStore.addAlert('error', error);
                return null;
            } else {
                if (successMessage) {
                    alertStore.addAlert('success', successMessage);
                }
                return data;
            }
        } catch (error) {
            alertStore.addAlert('error', 'An error occurred during the API call');
            return null;
        }
    }

    async function register(name, email, password) {
        const config = {
            url: 'http://localhost:5001/users/',
            method: "POST",
            data: { name, email, password }
        };
        await handleApiCall(config, 'Registration successful');
    }

    async function login(email, password) {
        const config = {
            url: 'http://localhost:5001/users/login/',
            method: "POST",
            data: { email, password }
        };
        const data = await handleApiCall(config);
        if (data) {
            saveToken(data.token);
            saveUser(data.user);
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
        logout,
        register,
    };
});