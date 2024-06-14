import React, { useState, useEffect } from 'react';
import axios from 'axios';

const GalleryManager = () => {
  const [galleries, setGalleries] = useState([]);
  const [title, setTitle] = useState('');
  const [coverImage, setCoverImage] = useState('');

  useEffect(() => {
    const fetchGalleries = async () => {
      try {
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/galleries`);
        setGalleries(response.data);
      } catch (error) {
        console.error('Error fetching galleries:', error);
      }
    };

    fetchGalleries();
  }, []);

  const handleCreateGallery = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`${import.meta.env.VITE_API_URL}/galleries`, { title, coverImage });
      setGalleries([...galleries, response.data]);
      setTitle('');
      setCoverImage('');
    } catch (error) {
      console.error('Error creating gallery:', error);
    }
  };

  const handleDeleteGallery = async (id) => {
    try {
      await axios.delete(`${import.meta.env.VITE_API_URL}/galleries/${id}`);
      setGalleries(galleries.filter(gallery => gallery._id !== id));
    } catch (error) {
      console.error('Error deleting gallery:', error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 py-8">
      <div className="container mx-auto">
        <h2 className="text-2xl font-bold text-center mb-8">Manage Galleries</h2>
        <form onSubmit={handleCreateGallery} className="space-y-4 mb-8">
          <div>
            <label className="block text-sm font-medium text-gray-700">Title</label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded mt-1"
              placeholder="Title"
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">Cover Image URL</label>
            <input
              type="text"
              value={coverImage}
              onChange={(e) => setCoverImage(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded mt-1"
              placeholder="Cover Image URL"
              required
            />
          </div>
          <button type="submit" className="w-full py-2 text-white bg-blue-500 rounded hover:bg-blue-600">
            Create Gallery
          </button>
        </form>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          {galleries.map(gallery => (
            <div key={gallery._id} className="p-4 bg-white rounded shadow">
              <img src={gallery.coverImage} alt={gallery.title} className="w-full h-48 object-cover rounded" />
              <h3 className="mt-4 text-lg font-bold">{gallery.title}</h3>
              <button
                onClick={() => handleDeleteGallery(gallery._id)}
                className="mt-4 py-2 px-4 bg-red-500 text-white rounded hover:bg-red-600"
              >
                Delete Gallery
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default GalleryManager;