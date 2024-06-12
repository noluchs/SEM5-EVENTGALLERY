import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import { AuthProvider, AuthContext } from './context/AuthContext.jsx';
import Login from './components/Login.jsx';
import Register from './components/Register.jsx';
import PhotoUpload from './components/PhotoUpload.jsx';
import Gallery from './components/Gallery.jsx';

const PrivateRoute = ({ element, ...rest }) => {
  const { user } = React.useContext(AuthContext);
  return user ? element : <Navigate to="/login" />;
};

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="container mx-auto p-4">
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/upload" element={<PrivateRoute element={<PhotoUpload />} />} />
            <Route path="/galleries" element={<PrivateRoute element={<Gallery />} />} />
            <Route path="*" element={<Navigate to="/galleries" />} />
          </Routes>
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;