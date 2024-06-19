import React, { useState, useEffect } from 'react';
import axios from 'axios';
import GalleryCard from './common/GalleryCard.jsx';

const Home = () => {
  const [galleries, setGalleries] = useState([]);

  useEffect(() => {
    const fetchGalleries = async () => {
      try {
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/galleries`);
        // Ensure response data is an array
        const data = Array.isArray(response.data) ? response.data : [];
        setGalleries(data);
      } catch (error) {
        console.error('Error fetching galleries:', error);
        setGalleries([]); // Set galleries to an empty array on error
      }
    };

    fetchGalleries();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 py-8">
      <h2 className="text-2xl font-bold text-center mb-8">Galleries</h2>
      <div className="container mx-auto grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        {galleries.map((gallery) => (
          <GalleryCard key={gallery._id} gallery={gallery} />
        ))}
      </div>
    </div>
  );
};

export default Home;