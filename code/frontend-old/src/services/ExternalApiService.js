import axios from "axios";

import { useAuthStore } from '@/stores/auth.store';

export const callExternalApi = async (options) => {
  try {
    options.config['headers'] = authHeader();
    const response = await axios(options.config);
    const { data } = response;

    return {
      data,
      error: null,
    };

  } catch (error) {

    if (axios.isAxiosError(error)) {
      const axiosError = error;

      const { response } = axiosError;
      const { token, logout } = useAuthStore();
      if ([401, 403].includes(error.response.status) && token) {
        logout();
      }

      let message = "http request failed";

      if (response && response.statusText) {
        message = response.statusText;
      }

      if (axiosError.message) {
        message = axiosError.message;
      }

      if (response && response.data && response.data.message) {
        message = response.data.message;
      }

      return {
        data: null,
        error: {
          message,
        },
      };
    }

    return {
      data: null,
      error: {
        message: error.message,
      },
    };
  }
};


function authHeader() {
  const { token } = useAuthStore();
  const isLoggedIn = !!token;

  if (isLoggedIn) {
    return {Authorization: `Bearer ${token}`};
  } else {
    return {};
  }
}
