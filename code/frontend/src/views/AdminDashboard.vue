<template>
  <div class="container mt-5">
    <h1>Admin Dashboard</h1>

    <form @submit.prevent="createGallery" class="mb-5">
      <div class="mb-3">
        <label for="galleryName" class="form-label">Gallery Name</label>
        <input type="text" class="form-control" id="galleryName" v-model="newGallery.name" required>
      </div>
      <div class="mb-3">
        <label for="coverImage" class="form-label">Cover Image</label>
        <input type="file" class="form-control" id="coverImage" @change="handleCoverImageUpload" required>
      </div>
      <button type="submit" class="btn btn-primary">Create Gallery</button>
    </form>

    <div v-if="galleries.length">
      <h2>Galleries</h2>
      <div v-for="gallery in galleries" :key="gallery.id" class="card mb-3">
        <div class="card-body">
          <h5 class="card-title">{{ gallery.name }}</h5>
          <img :src="gallery.cover_image_url" alt="Cover Image" class="img-thumbnail">
          <button @click="deleteGallery(gallery.id)" class="btn btn-danger">Delete Gallery</button>
          <button @click="openManagePicturesModal(gallery)" class="btn btn-secondary">Manage Pictures</button>
        </div>
      </div>
    </div>
    <p v-else>No galleries available</p>

    <!-- Manage Pictures Modal -->
    <div class="modal fade" id="managePicturesModal" tabindex="-1" aria-labelledby="managePicturesModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="managePicturesModalLabel">Manage Pictures</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <h5 v-if="selectedGallery">{{ selectedGallery.name }}</h5>
            <input type="file" @change="handleFileUpload($event)" class="form-control mt-3" multiple>
            <div class="mt-4">
              <h6>Existing Pictures</h6>
              <div v-if="pictures.length" class="row">
                <div class="col-md-3" v-for="picture in pictures" :key="picture.id">
                  <img :src="getPictureUrl(picture.filename)" class="img-thumbnail mb-2">
                  <button @click="deletePicture(picture.id)" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </div>
              <p v-else>No pictures available</p>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import { Modal } from 'bootstrap';

const galleries = ref([]);
const newGallery = ref({ name: '' });
const coverImage = ref(null);
const selectedGallery = ref(null);
const pictures = ref([]);

async function fetchGalleries() {
  try {
    const response = await axios.get('http://localhost:5001/api/gallery/', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    });
    galleries.value = response.data;
  } catch (error) {
    console.error('Error fetching galleries:', error);
  }
}

async function fetchPictures(galleryId) {
  try {
    const response = await axios.get(`http://localhost:5001/api/image/?gallery_id=${galleryId}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    });
    pictures.value = response.data;
  } catch (error) {
    console.error('Error fetching pictures:', error);
  }
}

async function createGallery() {
  try {
    const formData = new FormData();
    formData.append('name', newGallery.value.name);
    formData.append('cover_image', coverImage.value);

    const response = await axios.post('http://localhost:5001/api/gallery/', formData, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
        'Content-Type': 'multipart/form-data'
      }
    });
    galleries.value.push(response.data);
    newGallery.value.name = '';
    coverImage.value = null;
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

function handleCoverImageUpload(event) {
  coverImage.value = event.target.files[0];
}

function openManagePicturesModal(gallery) {
  selectedGallery.value = gallery;
  fetchPictures(gallery.id);
  new Modal(document.getElementById('managePicturesModal')).show();
}

function handleFileUpload(event) {
  const files = event.target.files;
  if (!files.length) return;

  const formData = new FormData();
  formData.append('gallery_id', selectedGallery.value.id);
  for (let file of files) {
    formData.append('files', file);
  }

  axios.post('http://localhost:5001/api/image/', formData, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem('token')}`,
      'Content-Type': 'multipart/form-data'
    }
  })
    .then(() => {
      alert('Files uploaded successfully');
      fetchPictures(selectedGallery.value.id);
    })
    .catch(error => {
      console.error('Error uploading files:', error);
    });
}

async function deletePicture(pictureId) {
  try {
    await axios.delete(`http://localhost:5001/api/image/${pictureId}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    });
    pictures.value = pictures.value.filter(picture => picture.id !== pictureId);
  } catch (error) {
    console.error('Error deleting picture:', error);
  }
}

function getPictureUrl(filename) {
  return `https://msvc-gallery.s3.eu-central-1.amazonaws.com/${filename}`;
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