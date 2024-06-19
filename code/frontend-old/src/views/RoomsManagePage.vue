<script setup>

import { ref, onMounted } from "vue";
import ConfirmDeletePopup from "@/components/ConfirmDeletePopup.vue";

import { storeToRefs } from 'pinia'
import { useRoomsStore } from '@/stores/rooms.store'

const { rooms, loading } = storeToRefs(useRoomsStore())
const { getRooms, deleteRoom } = useRoomsStore()

const itemToDeleteId = ref([0]);

let deleteModal;

onMounted(() => {
  deleteModal = new window.bootstrap.Modal(document.getElementById('deleteModal'));
});

const openDeleteModal = (id) => {
  itemToDeleteId.value = id;
  deleteModal.show();
};

const confirmDelete = () => {
  deleteRoom(itemToDeleteId.value)
  itemToDeleteId.value = 0;
  deleteModal.hide();
};

getRooms();

</script>

<template>
  <div class="container mt-3">
    <div v-if="loading">
      <p>Loading rooms...</p>
    </div>
    <div v-else>
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <div class="col">
          <div class="card bg-info h-100">
            <div class="card-body d-flex align-items-center justify-content-center">
              <RouterLink to="/add-edit-room" class="btn btn-secondary stretched-link"><span class="bi-plus-circle"></span> Add Room</RouterLink>
            </div>
          </div>
        </div>
        <div class="col" v-for="item in rooms" :key="item.id">
          <div class="card h-100">
            <div class="card-body">
              <h5 class="card-title">{{ item.name }}</h5>
              <p class="card-text">URI or IP: {{ item.uri }}</p>
              <p class="card-text">Microservice Context: {{ item.ms_context }}</p>
            </div>
            <div class="card-footer d-flex align-items-center justify-content-center">
              <div class="btn-group btn-group-sm">
                <RouterLink class="btn btn-primary" :to="`/add-edit-room/${item.id}`"><span class="bi-pencil-fill"></span> Edit</RouterLink>
                <button type="button" @click="openDeleteModal(item.id)" class="btn btn-danger">
                  <span class="bi-x-circle"></span> Delete
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
