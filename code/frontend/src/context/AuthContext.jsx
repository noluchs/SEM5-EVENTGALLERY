import React, { createContext, useState } from 'react';
import axios from 'axios';
axios.defaults.baseURL = import.meta.env.VITE_API_URL;

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  const login = async (email, password) => {
    const response = await axios.post('/api/auth/login', { email, password });
    const { token } = response.data;
    localStorage.setItem('token', token);
    setUser(jwtDecode(token));
  };

  const register = async (username, email, password) => {
    await axios.post('/api/auth/register', { username, email, password });
  };

  const logout = () => {
    localStorage.removeItem('token');
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  );


};