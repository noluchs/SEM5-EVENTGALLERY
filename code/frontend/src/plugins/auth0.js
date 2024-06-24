import { createAuth0 } from '@auth0/auth0-vue';
import config from '../../config.json';

export const auth0 = createAuth0({
  domain: config.VITE_APP_AUTH0_DOMAIN,
  clientId: config.VITE_APP_AUTH0_CLIENT_ID,
  authorizationParams: {
    redirect_uri: window.location.origin + '/callback'
  }
});