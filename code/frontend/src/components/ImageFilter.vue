/* eslint-disable */
<template>
  <div>
    <h1>Galleries</h1>
    <div class="row">
      <div class="col-md-4" v-for="gallery in galleries" :key="gallery.id" @click="openGallery(gallery.id)">
        <div class="card mb-4">
          <img :src="gallery.coverImage" class="card-img-top" alt="Gallery Cover">
          <div class="card-body">
            <h5 class="card-title">{{ gallery.name }}</h5>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data() {
    return {
      galleries: []
    }
  },
  created() {
    this.fetchGalleries();
  },
  methods: {
    fetchGalleries() {
      // Fetch galleries from backend
    },
    openGallery(id) {
      this.$router.push(`/gallery/${id}`);
    }
  }
}
</script>