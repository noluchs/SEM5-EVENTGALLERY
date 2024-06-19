<script setup>
import { useGamesStore } from '@/stores/games.store';
import { storeToRefs } from 'pinia';
const gamesStore = useGamesStore();
const { currentRoomInfo, roomInfo_loading } = storeToRefs(useGamesStore());

</script>
<template>
  <div
    class="modal fade"
    id="msContextModal"
    tabindex="-1"
    aria-labelledby="microservice context label"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="msContextModalLabel">
            Microservice Context
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
            <div v-if="roomInfo_loading">
                <div class="spinner-border m-5" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
            </div>
            <div v-else>
                {{ currentRoomInfo.ms_context }}
            </div>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
