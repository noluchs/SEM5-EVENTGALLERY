<template>
  <div>
    <div v-if="isLoading" class="loading-container">
      <img src="@/assets/loading.svg" alt="Loading..." class="loading-animation">
    </div>
    <div v-else>
      <div v-if="gallery">
        <h1>{{ gallery.name }}</h1>
        <button @click="openCamera">Filter by Face</button>
        <div class="row">
          <div class="col-md-3" v-for="picture in pictures" :key="picture.id">
            <img :src="getPictureUrl(picture.filename)" class="img-thumbnail mb-2" alt="Picture">
          </div>
        </div>
      </div>
      <p v-else>Loading gallery...</p>
    </div>

    <!-- Camera Modal -->
    <div class="modal fade" id="cameraModal" tabindex="-1" aria-labelledby="cameraModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="cameraModalLabel">Capture Image</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <video v-if="!capturedImage" id="video" width="100%" autoplay></video>
            <canvas v-show="false" id="canvas"></canvas>
            <img v-if="capturedImage" :src="capturedImage" class="img-thumbnail mb-2" alt="Captured Image">
            <button v-if="!capturedImage" @click="captureImage" class="btn btn-primary mt-3">Capture</button>
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
const capturedImage = ref(null);
let cameraModal = null;

async function fetchGalleries() {
  try {
    const response = await axios.get('${process.env.VUE_APP_API_URL}/api/gallery/', {
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
    const response = await axios.get(`${process.env.VUE_APP_API_URL}/api/image/?gallery_id=${galleryId}`, {
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

function openCamera() {
  console.log("Opening camera modal...");
  selectedImage.value = null;
  capturedImage.value = null;
  cameraModal = new Modal(document.getElementById('cameraModal'));
  cameraModal.show();

  const video = document.getElementById('video');

  if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true }).then(function (stream) {
      video.srcObject = stream;
      video.play();
    });
  }
}

function captureImage() {
  const video = document.getElementById('video');
  const canvas = document.getElementById('canvas');
  const context = canvas.getContext('2d');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  context.drawImage(video, 0, 0, canvas.width, canvas.height);
  capturedImage.value = canvas.toDataURL('image/png');
  console.log("Captured image: ", capturedImage.value);
}

async function submitImage() {
  if (!capturedImage.value) {
    alert('Please capture an image.');
    return;
  }

  const galleryId = route.params.id;
  try {
    console.log("Sending image to backend for comparison...");
    const response = await axios.post(`${process.env.VUE_APP_API_URL}/api/rekognition/`, {
      gallery_id: galleryId,
      image: capturedImage.value
    }, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    });
    const matchedPictures = response.data;
    pictures.value = matchedPictures;
    console.log('Matched pictures:', matchedPictures);

    if (cameraModal) {
      cameraModal.hide();
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