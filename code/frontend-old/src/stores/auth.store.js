import { defineStore } from 'pinia';
import { ref } from 'vue';
import { callExternalApi } from "../services/ExternalApiService";
import router from '../router';
import { useAlertStore } from '@/stores/alert.store';

export const useAuthStore = defineStore('auth', () => {
    const token = ref(JSON.parse(localStorage.getItem('token')));
    const user = ref(JSON.parse(localStorage.getItem('user')));
    const returnUrl = ref(null);
    const inviteToken = ref(null);
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
    }

    async function register(name, email, password, invite_token) {
        const config = {
            url: '/api/users/',
            method: "POST",
            data: { name, email, password, invite_token }
        };
        await handleApiCall(config, 'Registration successful');
    }

    async function getInviteToken(email) {
        const config = {
            url: '/api/users/invite',
            method: "POST",
            data: { email }
        };
        const data = await handleApiCall(config);
        if (data) {
            inviteToken.value = data.token;
        }
    }

    async function login(email, password) {
        const config = {
            url: '/api/users/login',
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
        inviteToken,
        login,
        logout,
        register,
        getInviteToken,
    };
});
