import { callExternalApi } from "../services/ExternalApiService";

import { ref, computed } from 'vue'
import { defineStore} from 'pinia'

import { useAlertStore } from '@/stores/alert.store';

export const useRoomsStore = defineStore('rooms', () => {
  
  const rooms = ref([]);
  const loading = ref(false);
  const initialized = ref(false);

  const getRoomById = computed(() => (id) => {
    if (rooms.value) {
      return rooms.value.find(x => x.id == id);
    } else {
      return null;
    }
  });

  async function getRooms() {
    rooms.value = []
    loading.value = true
    const config = {
      url: `/api/rooms`,
      method: "GET",
    };
    const { data, error } = await callExternalApi({ config })
    if (error)
    {
        const alertStore = useAlertStore();
        alertStore.addAlert('error', error.message);
    }
    rooms.value = data;
    loading.value = false;
    initialized.value = true;
  };

  async function deleteRoom(RoomId) {
    const config = {
      url: `/api/rooms/${RoomId}`,
      method: "DELETE",
    };
    const { data, error } = await callExternalApi({ config });
    if (error)
    {
        const alertStore = useAlertStore();
        alertStore.addAlert('error', error.message);
    }
    rooms.value = rooms.value.filter( (x) => x.id !== RoomId)
  };

  async function createRoom(roomData) {
    const config = {
      url: `/api/rooms`,
      method: "POST",
      data: {'name':roomData.name, 'ms_context':roomData.ms_context, 'uri':roomData.uri}
    };
    const { data, error } = await callExternalApi({ config });

    const alertStore = useAlertStore();
    if (error)
    {
      alertStore.addAlert('error', error.message);
    } else {
      alertStore.addAlert('info', "Room successfully created");
    }

    rooms.value.push(data);
  };

  async function updateRoom(roomId, patchRoom) {
    const alertStore = useAlertStore();
    const index = rooms.value.findIndex(room => String(room.id) === String(roomId));
    if (index !== -1) {
      rooms.value[index] = { ...rooms.value[index], ...patchRoom };

      const config = {
        url: `/api/rooms/${roomId}`,
        method: "PATCH",
        data: {'name':patchRoom.name, 'ms_context':patchRoom.ms_context, 'uri':patchRoom.uri}
      };
      const { data, error } = await callExternalApi({ config });
      if (error)
      {
          alertStore.addAlert('error', error.message);
      }
    } else {
      alertStore.addAlert('error', "Something went wrong. Id of the room to patch not found.")
    }
  };

  return { rooms, getRooms, getRoomById, deleteRoom, createRoom, updateRoom, loading, initialized }
  
});