<template>
  <div>
    <div v-if="isLoading" class="loading-container">
      <img src="@/assets/loading.svg" alt="Loading..." class="loading-animation">
    </div>
    <div v-else>
      <div v-if="gallery">
        <h1>{{ gallery.name }}</h1>
        <button @click="openUploadModal">Filter by Face</button>
        <div class="row">
          <div class="col-md-3" v-for="picture in pictures" :key="picture.id">
            <img :src="getPictureUrl(picture.filename)" class="img-thumbnail mb-2" alt="Picture">
          </div>
        </div>
      </div>
      <p v-else>Loading gallery...</p>
    </div>

    <!-- Upload Modal -->
    <div class="modal fade" id="uploadModal" tabindex="-1" aria-labelledby="uploadModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="uploadModalLabel">Upload Image</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <input type="file" @change="handleFileUpload" class="form-control" accept="image/*">
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary" @click="submitImage">Submit</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import { Modal } from 'bootstrap';

const gallery = ref(null);
const pictures = ref([]);
const isLoading = ref(true);
const route = useRoute();
const selectedImage = ref(null);
let uploadModal = null;

async function fetchGalleries() {
  try {
    const response = await axios.get('http://localhost:5001/api/gallery/', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    });
    const galleries = response.data;
    const galleryId = route.params.id;
    gallery.value = galleries.find(g => g.id == galleryId);
    console.log('Fetched galleries:', galleries);
    console.log('Selected gallery:', gallery.value);
  } catch (error) {
    console.error('Error fetching galleries:', error);
  }
}

async function fetchPictures() {
  const galleryId = route.params.id;
  try {
    const response = await axios.get(`http://localhost:5001/api/image/?gallery_id=${galleryId}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    });
    pictures.value = response.data;
    console.log('Fetched pictures:', response.data);
  } catch (error) {
    console.error('Error fetching pictures:', error);
  }
}

function getPictureUrl(filename) {
  return `https://msvc-gallery.s3.eu-central-1.amazonaws.com/${filename}`;
}

function openUploadModal() {
  console.log("Opening upload modal...");
  selectedImage.value = null;
  uploadModal = new Modal(document.getElementById('uploadModal'));
  uploadModal.show();
}

function handleFileUpload(event) {
  console.log("File upload triggered...");
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      selectedImage.value = e.target.result;
      console.log("Selected image: ", selectedImage.value);
    };
    reader.readAsDataURL(file);
  }
}

async function submitImage() {
  if (!selectedImage.value) {
    alert('Please select an image to upload.');
    return;
  }

  const galleryId = route.params.id;
  try {
    console.log("Sending image to backend for comparison...");
    const response = await axios.post(`http://localhost:5001/api/rekognition/`, {
      gallery_id: galleryId,
      image: selectedImage.value
    }, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    });
    const matchedPictures = response.data;
    pictures.value = matchedPictures;
    console.log('Matched pictures:', matchedPictures);

    if (uploadModal) {
      uploadModal.hide();
    }
  } catch (error) {
    console.error('Error comparing faces:', error);
    alert('An error occurred while comparing faces. Please try again.');
  }
}

onMounted(async () => {
  await fetchGalleries();
  if (gallery.value) {
    await fetchPictures();
  }
  isLoading.value = false;
});
</script>

<style scoped>
.row {
  margin-top: 20px;
}
.loading-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
.loading-animation {
  width: 100px;
  height: 100px;
}
</style>