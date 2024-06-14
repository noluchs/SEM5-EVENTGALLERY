import React from 'react';
import { Link } from 'react-router-dom';

const Dashboard = () => {
  return (
    <div className="min-h-screen bg-gray-100 py-8">
      <div className="container mx-auto text-center">
        <h2 className="text-2xl font-bold mb-8">Admin Dashboard</h2>
        <div className="space-y-4">
          <Link to="/admin/galleries" className="block py-2 px-4 bg-blue-500 text-white rounded hover:bg-blue-600">Manage Galleries</Link>
          <Link to="/admin/photos" className="block py-2 px-4 bg-blue-500 text-white rounded hover:bg-blue-600">Manage Photos</Link>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;