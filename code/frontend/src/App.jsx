import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import { AuthProvider, AuthContext } from './context/AuthContext.jsx';
import Home from './components/Home.jsx';
import GalleryView from './components/GalleryView.jsx';
import Login from './components/Admin/Login.jsx';
import Dashboard from './components/Admin/Dashboard.jsx';
import GalleryManager from './components/Admin/GalleryManager.jsx';
import PhotoManager from './components/Admin/PhotoManager.jsx';

const PrivateRoute = ({ element, ...rest }) => {
  const { user } = React.useContext(AuthContext);
  return user ? element : <Navigate to="/login" />;
};

function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/galleries/:id" element={<GalleryView />} />
          <Route path="/login" element={<Login />} />
          <Route path="/admin/dashboard" element={<PrivateRoute element={<Dashboard />} />} />
          <Route path="/admin/galleries" element={<PrivateRoute element={<GalleryManager />} />} />
          <Route path="/admin/photos" element={<PrivateRoute element={<PhotoManager />} />} />
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;