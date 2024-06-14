import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';
import jwtDecode from 'jwt-decode';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      setUser(jwtDecode(token));
    }
  }, []);

  const login = async (email, password) => {
    try {
      const response = await axios.post(`${import.meta.env.VITE_API_URL}/auth/login`, { email, password });
      const { token } = response.data;
      localStorage.setItem('token', token);
      setUser(jwtDecode(token));
    } catch (error) {
      console.error('Login error:', error);
    }
  };

  const register = async (username, email, password) => {
    try {
      await axios.post(`${import.meta.env.VITE_API_URL}/auth/register`, { username, email, password });
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