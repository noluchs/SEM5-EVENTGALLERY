<template>
  <div v-if="gallery">
    <h1>{{ gallery.name }}</h1>
    <button @click="startCamera">Filter Pictures by Face</button>
    <div v-if="cameraEnabled">
      <video ref="video" width="320" height="240" autoplay></video>
      <button @click="captureImage">Capture</button>
    </div>
    <div class="row">
      <div class="col-md-3" v-for="picture in filteredPictures" :key="picture.id">
        <img :src="getPictureUrl(picture.filename)" class="img-thumbnail mb-2" alt="Picture">
      </div>
    </div>
  </div>
  <p v-else>Loading gallery...</p>
</template>

<script setup>
import {ref, onMounted} from 'vue';
import {useRoute} from 'vue-router';
import axios from 'axios';

const gallery = ref(null);
const pictures = ref([]);
const filteredPictures = ref([]);
const cameraEnabled = ref(false);
const video = ref(null);
const route = useRoute();

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
    filteredPictures.value = response.data; // Initialize filtered pictures
    console.log('Fetched pictures:', response.data);
  } catch (error) {
    console.error('Error fetching pictures:', error);
  }
}

function getPictureUrl(filename) {
  return `https://msvc-gallery.s3.eu-central-1.amazonaws.com/${filename}`;
}

function startCamera() {
  cameraEnabled.value = true;
  navigator.mediaDevices.getUserMedia({video: true}).then((stream) => {
    video.value.srcObject = stream;
  }).catch((error) => {
    console.error('Error accessing camera:', error);
  });
}

async function captureImage() {
  const canvas = document.createElement('canvas');
  canvas.width = video.value.videoWidth;
  canvas.height = video.value.videoHeight;
  const context = canvas.getContext('2d');
  context.drawImage(video.value, 0, 0, canvas.width, canvas.height);
  const imageData = canvas.toDataURL('image/png');

  // Send the captured image to the backend for Rekognition
  try {
    const response = await axios.post('http://localhost:5001/api/rekognition/', {
      image: imageData,
      gallery_id: gallery.value.id
    }, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    });
    filteredPictures.value = response.data;
    console.log('Filtered pictures:', response.data);
  } catch (error) {
    console.error('Error comparing faces:', error);
  }

  cameraEnabled.value = false;
}

onMounted(() => {
  fetchGalleries().then(() => {
    if (gallery.value) {
      fetchPictures();
    }
  });
});
</script>

<style scoped>
.row {
  margin-top: 20px;
}
</style>