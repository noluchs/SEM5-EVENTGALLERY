import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';
import jwt_decode from 'jwt-decode';

axios.defaults.baseURL = '/api';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      setUser(jwt_decode(token));
    }
  }, []);

  const login = async (email, password) => {
    try {
      const response = await axios.post('/users/login', { email, password });
      const { token } = response.data;
      localStorage.setItem('token', token);
      setUser(jwt_decode(token));
    } catch (error) {
      console.error('Login error:', error);
    }
  };

  const register = async (username, email, password) => {
    try {
      await axios.post('/users/create', { username, email, password });
    } catch (error) {
      console.error('Registration error:', error);
    }
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