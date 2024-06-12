import React, { useState } from 'react';
import axios from 'axios';

const PhotoUpload = () => {
  const [file, setFile] = useState(null);
  const [imageUrl, setImageUrl] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('photo', file);

    const response = await axios.post(`${import.meta.env.VITE_API_URL}/photos/upload`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    setImageUrl(response.data.imageUrl);
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="w-full max-w-md p-8 space-y-4 bg-white rounded shadow-lg">
        <h2 className="text-2xl font-bold text-center">Upload Photo</h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <input type="file" onChange={handleFileChange} className="w-full p-2 border border-gray-300 rounded mt-1" />
          </div>
          <button type="submit" className="w-full py-2 mt-4 text-white bg-blue-500 rounded hover:bg-blue-600">
            Upload Photo
          </button>
        </form>
        {imageUrl && (
          <div className="mt-4">
            <p>Uploaded Image:</p>
            <img src={imageUrl} alt="Uploaded" className="w-full rounded" />
          </div>
        )}
      </div>
    </div>
  );
};

export default PhotoUpload;