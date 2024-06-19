<script setup>

import { ref, onMounted } from "vue";
import ConfirmDeletePopup from "@/components/ConfirmDeletePopup.vue";

import { storeToRefs } from 'pinia'
import { useGamesStore } from '@/stores/games.store'
import { useRouter, useRoute } from 'vue-router';

const { games, games_loading } = storeToRefs(useGamesStore())
const { getGames, endGame } = useGamesStore()

const gamesStore = useGamesStore();

const itemToDeleteId = ref([0]);
const route = useRoute();
const router = useRouter();

let deleteModal;

onMounted(() => {
  deleteModal = new window.bootstrap.Modal(document.getElementById('deleteModal'));
});

const openDeleteModal = (id) => {
  itemToDeleteId.value = id;
  deleteModal.show();
};

const confirmDelete = () => {
  endGame(itemToDeleteId.value)
  itemToDeleteId.value = 0;
  deleteModal.hide();
};

getGames();

</script>

<template>
  <div class="container mt-3">
    <div v-if="games_loading">
      <p>Loading games...</p>
    </div>
    <div v-else>
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <div class="col">
          <div class="card bg-info h-100">
            <div class="card-body d-flex align-items-center justify-content-center">
              <button type="button" @click="gamesStore.startGame()" class="btn btn-primary">
                <span class="bi-play-circle"></span> Start Game
              </button>
            </div>
          </div>
        </div>
        <div class="col" v-for="item in games" :key="item.id">
          <div class="card h-100">
            <div class="card-body">
              <h5 class="card-title">Game {{ item.id }}</h5>
              <p class="card-text">started on: {{ item.started_on }}</p>
              <p class="card-text">rooms: {{ item.num_rooms }}</p>
            </div>
            <div class="card-footer d-flex align-items-center justify-content-center">
              <div class="btn-group btn-group-sm">
                <RouterLink class="btn btn-primary" :to="`/play-game/${item.id}`"><span class="bi-play-circle"></span> Play</RouterLink>
                <button type="button" @click="openDeleteModal(item.id)" class="btn btn-danger">
                  <span class="bi-x-circle"></span> End Game
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <ConfirmDeletePopup @confirmdelete-click="confirmDelete"></ConfirmDeletePopup>
</template>
