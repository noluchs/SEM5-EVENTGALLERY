<script setup>
import { useRoute } from 'vue-router';
import { storeToRefs } from 'pinia';
import { useGamesStore } from '@/stores/games.store';
import { ref, onMounted, watch } from 'vue';
import MsContextPopup from "@/components/MsContextPopup.vue";

const gamesStore = useGamesStore();
const route = useRoute();

const { currentRoomState, roomState_loading } = storeToRefs(useGamesStore());
const { currentRoomInfo,  roomInfo_loading} = storeToRefs(useGamesStore());
const { exitsLocked } = storeToRefs(useGamesStore());

const selectedGame = ref();
const selectedObject = ref();
const interact_with = ref();
const interact_parameter = ref();
const cacheKey = ref();


let msContextModal;

onMounted(() => {
    msContextModal = new window.bootstrap.Modal(document.getElementById('msContextModal'));
});

async function move_on(direction) {
    selectedObject.value = "";
    try {
        await gamesStore.move(route.params.id, direction); // Move in the specified direction
        cacheKey.value = Date.now(); // Update cache key to force image reload
        gamesStore.examineCurrentRoom(route.params.id); // Examine the current room after moving
        gamesStore.getCurrentRoomInfo(route.params.id); // Get the info of the newly moved-to room
    } catch (error) {
        console.error('Error processing move:', error);
    }
}

try {
    selectedObject.value = ""; // Reset selected object
    cacheKey.value = Date.now(); // Update cache key to force image reload
    interact_with.value = "";
    const gameId = route.params.id;
    gamesStore.examineCurrentRoom(gameId);
    gamesStore.getCurrentRoomInfo(gameId);
} catch (error) {
    console.error('Error fetching game:', error);
}


</script>

<template>
<div class="container" style="max-width: 768px;">

    <div class="row g-2">
        <!-- Display Image -->
        <div class="col-md-5 gy-3">
            <div class="card bg-dark text-white h-100">
                <div v-if="roomInfo_loading">
                    <div class="spinner-border m-5" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                </div>
                <div v-else>
                    <img :src="'/api/games/' + route.params.id + '/current-room/image' + '?cache=' + cacheKey" class="card-img" alt="...">
                    <div class="card-img-overlay">
                        <h4 class="card-title">{{ currentRoomInfo?.name }}</h4>
                        <button type="button" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#msContextModal">
                         info
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <!-- Display message -->
        <div class="col-md-7 gy-3">
            <div class="card h-100">
                <h5 class="card-header">Message</h5>
                <div v-if="roomState_loading">
                    <div class="spinner-border m-5" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                </div>
                <div v-else class="card-body">
                    <p class="card-text">{{currentRoomState?.message}}</p>
                </div>
            </div>
        </div>
    </div>

     <!-- Display exits -->
     <div v-if="currentRoomInfo">
        <div v-if="!exitsLocked" class="row g-3">
            <div class="col col-md-12 gy-4">
                <div class="card">
                    <h5 class="card-header">Exits</h5>
                    <div class="card-body">
                        <div v-if="roomInfo_loading">
                            <div class="spinner-border m-5" role="status">
                                <span class="visually-hidden">Loading...</span>
                            </div>
                        </div>
                        <div v-else>
                            <div class="d-flex flex-row flex-wrap">
                                <div class="p-1" v-for="exit in currentRoomInfo?.exits" :key="exit.direction">
                                    <button type="button" @click="move_on(exit.direction)" class="btn btn-info d-flex align-items-center">
                                        <span :class="`bi-door-closed-fill`" aria-hidden="true"></span>
                                        <span class="ms-2 flex-grow-1 text-start">{{ exit.direction }}</span>
                                        <span class="ms-3"><small class="text-muted">{{ exit.description }}</small></span>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>  
    
    <div class="row g-3">
        <!-- Display Objects -->
        <div class="col col-md-12 gy-4">
            <div class="card">
                <h5 class="card-header">Objects</h5>
                <div v-if="roomState_loading">
                    <div class="spinner-border m-5" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                </div>
                <div v-else>
                    <div class="card-body px-3 py-2">
                        <div class="d-flex flex-row flex-wrap">
                            <div class="p-1" v-for="object in currentRoomState?.objects" :key="object.id">
                                <button type="button" @click="selectedObject = object" class="btn btn-info d-flex align-items-center" style="width: 100%; min-width: 100px; height: 40px;">
                                    <span :class="`bi-${object.icon}`" aria-hidden="true"></span>
                                    <span class="ms-2 flex-grow-1 text-start">{{ object.name }}</span>
                                </button>
                            </div>
                        </div>
                    </div>
                    <div v-if="selectedObject">
                        <!-- Details on selectedObject -->
                        <div class="card-body px-3 py-2">
                            <h6 class="card-title">Details on {{ selectedObject.name }}</h6>
                            <p class=""card-text>{{selectedObject.description}}</p>
                        </div>
                        <div class="card-body px-3 py-1">
                            <div class="row">
                                <div class="col-auto">
                                    <a href="#" class="btn btn-primary" @click="gamesStore.examineObject(route.params.id, selectedObject.id)">Examine</a>
                                </div>
                                <div class="col">
                                    <div class="container">
                                        <div class="row">
                                            <div class="col-12 col-md-auto mb-2 mb-md-0">
                                                <a href="#" class="btn btn-primary btn-block" @click="gamesStore.interactObject(route.params.id, selectedObject.id, interact_with, interact_parameter)">
                                                    Interact
                                                </a>
                                            </div>
                                            <div class="col-12 col-md">
                                                <select v-model="interact_with" class="form-select" aria-label="Object to combine">
                                                    <option selected value="">with...</option>
                                                    <template v-for="object in currentRoomState?.objects">
                                                        <option v-if="object.id !== selectedObject.id" :key="object.id" :value="object.id">
                                                            {{ object.name }}
                                                        </option>
                                                    </template>
                                                </select>
                                            </div>
                                            <div class="col-12 col-md">
                                                <input v-model="interact_parameter" type="text" class="form-control" placeholder="parameter" />
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<MsContextPopup></MsContextPopup>
      
</template>
