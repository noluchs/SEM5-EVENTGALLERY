<template>
  <div>
    <h1>Galleries</h1>
    <div class="row">
      <div class="col-md-4" v-for="gallery in galleries" :key="gallery.id" @click="openGallery(gallery.id)">
        <div class="card mb-4">
          <img :src="gallery.cover_image" class="card-img-top" alt="Gallery Cover">
          <div class="card-body">
            <h5 class="card-title">{{ gallery.title }}</h5>
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
    async fetchGalleries() {
  try {
    const response = await fetch('http://localhost:5001/api/gallery/');
    if (response.ok) {
      this.galleries = await response.json();
    } else {
      console.error('Failed to fetch galleries');
    }
  } catch (error) {
    console.error('Error fetching galleries:', error);
  }
},
    openGallery(id) {
      this.$router.push(`/gallery/${id}`);
    }
  }
}
</script>