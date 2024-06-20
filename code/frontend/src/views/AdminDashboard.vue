<template>
  <div class="container mt-5">
    <h1>Admin Dashboard</h1>

    <form @submit.prevent="createGallery" class="mb-5">
      <div class="mb-3">
        <label for="galleryName" class="form-label">Gallery Name</label>
        <input type="text" class="form-control" id="galleryName" v-model="newGallery.name" required>
      </div>
      <button type="submit" class="btn btn-primary">Create Gallery</button>
    </form>

    <div v-if="galleries.length">
      <h2>Galleries</h2>
      <div v-for="gallery in galleries" :key="gallery.id" class="card mb-3">
        <div class="card-body">
          <h5 class="card-title">{{ gallery.name }}</h5>
          <button @click="deleteGallery(gallery.id)" class="btn btn-danger">Delete Gallery</button>
          <input type="file" @change="handleFileUpload(gallery.id, $event)" class="form-control mt-3" multiple>
        </div>
      </div>
    </div>
    <p v-else>No galleries available</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const galleries = ref([]);
const newGallery = ref({ name: '' });

async function fetchGalleries() {
  try {
    const response = await axios.get('http://localhost:5001/api/gallery', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    });
    galleries.value = response.data;
  } catch (error) {
    console.error('Error fetching galleries:', error);
  }
}

async function createGallery() {
  try {
    const response = await axios.post('http://localhost:5001/api/gallery', newGallery.value, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    });
    galleries.value.push(response.data);
    newGallery.value.name = '';
  } catch (error) {
    console.error('Error creating gallery:', error);
  }
}

async function deleteGallery(galleryId) {
  try {
    await axios.delete(`http://localhost:5001/api/gallery/${galleryId}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    });
    galleries.value = galleries.value.filter(gallery => gallery.id !== galleryId);
  } catch (error) {
    console.error('Error deleting gallery:', error);
  }
}

async function handleFileUpload(galleryId, event) {
  const files = event.target.files;
  if (!files.length) return;

  const formData = new FormData();
  formData.append('gallery_id', galleryId);
  for (let file of files) {
    formData.append('file', file); // Ensure 'file' is used as key for each file
  }

  try {
    await axios.post('http://localhost:5001/api/image', formData, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
        'Content-Type': 'multipart/form-data'
      }
    });
    alert('Files uploaded successfully');
  } catch (error) {
    console.error('Error uploading files:', error);
  }
}

onMounted(() => {
  fetchGalleries();
});
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
}
</style>