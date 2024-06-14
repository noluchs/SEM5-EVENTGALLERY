import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import PhotoCard from './common/PhotoCard.jsx';

const GalleryView = () => {
  const { id } = useParams();
  const [photos, setPhotos] = useState([]);
  const [gallery, setGallery] = useState(null);

  useEffect(() => {
    const fetchGallery = async () => {
      try {
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/galleries/${id}`);
        setGallery(response.data);
      } catch (error) {
        console.error('Error fetching gallery:', error);
      }
    };

    const fetchPhotos = async () => {
      try {
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/photos/${id}`);
        setPhotos(response.data);
      } catch (error) {
        console.error('Error fetching photos:', error);
      }
    };

    fetchGallery();
    fetchPhotos();
  }, [id]);

  return (
    <div className="min-h-screen bg-gray-100 py-8">
      {gallery && <h2 className="text-2xl font-bold text-center mb-8">{gallery.title}</h2>}
      <div className="container mx-auto grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        {photos.map((photo) => (
          <PhotoCard key={photo._id} photo={photo} />
        ))}
      </div>
    </div>
  );
};

export default GalleryView;