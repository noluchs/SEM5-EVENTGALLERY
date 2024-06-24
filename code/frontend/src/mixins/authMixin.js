import { useAuth0 } from '@/plugins/auth0';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

export const authMixin = {
  setup() {
    const router = useRouter();
    const isAuthenticated = ref(false);
    const user = ref(null);

    onMounted(async () => {
      const auth0 = await useAuth0();
      isAuthenticated.value = await auth0.isAuthenticated();
      if (!isAuthenticated.value) {
        router.push('/login');
      } else {
        user.value = await auth0.getUser();
        if (!user.value[`${import.meta.env.VITE_APP_AUTH0_NAMESPACE}/roles`].includes('admin')) {
          router.push('/'); // or show an unauthorized page
        }
      }
    });

    return { isAuthenticated, user };
  }
};