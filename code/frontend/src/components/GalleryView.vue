<template>
  <div v-if="gallery">
    <h1>{{ gallery.name }}</h1>
    <div class="row">
      <div class="col-md-3" v-for="(picture, index) in pictures" :key="picture.id">
        <img
          :src="getPictureUrl(picture.filename)"
          class="img-thumbnail mb-2"
          alt="Picture"
          @click="openModal(index)"
        >
      </div>
    </div>

    <!-- Picture Modal -->
    <div class="modal fade" id="pictureModal" tabindex="-1" aria-labelledby="pictureModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="pictureModalLabel">Picture</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <img :src="getPictureUrl(currentPicture.filename)" class="img-fluid" alt="Picture">
            <div class="mt-3">
              <social-sharing
                :url="shareUrl"
                title="Check out this picture"
                description="A beautiful picture from the gallery"
                inline-template
              >
                <div>
                  <network network="facebook">
                    <i class="fab fa-facebook"></i> Share
                  </network>
                  <network network="twitter">
                    <i class="fab fa-twitter"></i> Tweet
                  </network>
                  <network network="whatsapp">
                    <i class="fab fa-whatsapp"></i> Share
                  </network>
                  <network network="email">
                    <i class="fas fa-envelope"></i> Email
                  </network>
                </div>
              </social-sharing>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary" @click="prevPicture" :disabled="currentIndex === 0">Previous</button>
            <button type="button" class="btn btn-primary" @click="nextPicture" :disabled="currentIndex === pictures.length - 1">Next</button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <p v-else>Loading gallery...</p>
</template>

<script setup>
import { ref } from 'vue';
import SocialSharing from 'vue-social-sharing';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import { Modal } from 'bootstrap';

const props = defineProps({
  gallery: Object,
  pictures: Array
});

const currentIndex = ref(0);
const currentPicture = ref({});
const shareUrl = ref('');

function getPictureUrl(filename) {
  return `https://msvc-gallery.s3.eu-central-1.amazonaws.com/${filename}`;
}

function openModal(index) {
  currentIndex.value = index;
  currentPicture.value = props.pictures[index];
  shareUrl.value = getPictureUrl(currentPicture.value.filename);
  const modal = new Modal(document.getElementById('pictureModal'));
  modal.show();
}

function prevPicture() {
  if (currentIndex.value > 0) {
    currentIndex.value--;
    currentPicture.value = props.pictures[currentIndex.value];
    shareUrl.value = getPictureUrl(currentPicture.value.filename);
  }
}

function nextPicture() {
  if (currentIndex.value < props.pictures.length - 1) {
    currentIndex.value++;
    currentPicture.value = props.ppictures[currentIndex.value];
    shareUrl.value = getPictureUrl(currentPicture.value.filename);
  }
}
</script>

<style scoped>
.row {
  margin-top: 20px;
}
</style>