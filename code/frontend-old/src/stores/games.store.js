import { callExternalApi } from "../services/ExternalApiService";

import { ref, computed } from 'vue'
import { defineStore} from 'pinia'
import { useAlertStore } from '@/stores/alert.store';

import { useRouter } from 'vue-router';


export const useGamesStore = defineStore('games', () => {
  
  const games = ref([]);
  const currentGame = ref();
  const currentRoomInfo = ref();
  const currentRoomState = ref();
  const roomState_loading = ref(true);
  const roomInfo_loading = ref(true);
  const games_loading = ref(true);

  const router = useRouter();

  const getGameById = computed(() => (id) => {
    if (games.value) {
      return games.value.find(x => x.id == id);
    } else {
      return null;
    }
  });

  const exitsLocked = computed(() => {
    if (currentRoomState.value) {
      return currentRoomState.value.exits_locked
    } else {
      return true;
    }
  });

  /////
 // Assuming 'games', 'loading' are reactive refs outside this function
  async function getGames() {
    games_loading.value = true;  // Start loading

    const config = {
        url: `/api/games`,
        method: "GET",
    };
    try {
        const { data, error } = await callExternalApi({ config });
        if (error) {
            throw new Error(error.message); // Transform API error into an exception
        }
        games.value = data || [];  // Safely assign data or empty array if data is undefined/null
    } catch (error) {
        // Utilize a centralized store for alert notifications
        useAlertStore().addAlert('error', `Failed to load games: ${error.message}`);
        games.value = [];  // Ensure games is set to an empty array in case of error
    } finally {
        games_loading.value = false;  // Ensure that the loading indicator is turned off
    }
  }

  /////
  async function getCurrentRoomInfo(GameId) {
    roomInfo_loading.value = true

    const config = {
      url: `/api/games/${GameId}/current-room/info`,
      method: "GET",
    };

    try {
      const { data, error } = await callExternalApi({ config });
      if (error) {
        throw new Error(error.message); // Propagate a clear error message up the chain
      }
      currentRoomInfo.value = data;  // Update the room state with the returned data
      return data; // Return data for chaining or confirmation of success
    } catch (error) {
      // Log and display error using a centralized alert system
      useAlertStore().addAlert('error', `Could not retrieve Room Info: ${error.message}`);
      throw error; // Allows caller to handle or log the error further if necessary
    } finally {
      roomInfo_loading.value = false; // Ensure that the loading indicator is turned off
    }
  }

  /////
  async function examineObject(GameId, ObjectId) {
    roomState_loading.value = true
    const config = {
      url: `/api/games/${GameId}/current-room/objects/${ObjectId}/examine`,
      method: "GET",
    };

    try {
      const { data, error } = await callExternalApi({ config });
      if (error) {
        throw new Error(error.message); // Propagate a clear error message up the chain
      }
      currentRoomState.value = data;  // Update the room state with the returned data
      return data; // Return data for chaining or confirmation of success
    } catch (error) {
      // Log and display error using a centralized alert system
      useAlertStore().addAlert('error', `Could not retrieve RoomState: ${error.message}`);
      throw error; // Allows caller to handle or log the error further if necessary
    } finally {
      roomState_loading.value = false; // Ensure that the loading indicator is turned off
    }
  };


  /////
  async function interactObject(GameId, ObjectId, use_with_id, parameter) {
    
    roomState_loading.value = true;

    let requestData = {};

    // Conditionally add use_with_id and parameter if they are valid
    if (use_with_id) { // Add any additional checks if needed, like use_with_id !== null
      requestData.object_id = use_with_id;
    };
    if (parameter && parameter!==''){
     // Add any additional checks if needed, like parameter !== ''
      requestData.parameter = parameter;
    };

    const config = {
      url: `/api/games/${GameId}/current-room/objects/${ObjectId}/interact`,
      data: requestData,
      method: "POST",
    };
    try {
      const { data, error } = await callExternalApi({ config });
      if (error) {
        throw new Error(error.message); // Propagate a clear error message up the chain
      }
      currentRoomState.value = data;  // Update the room state with the returned data
      return data; // Return data for chaining or confirmation of success
    } catch (error) {
      // Log and display error using a centralized alert system
      useAlertStore().addAlert('error', `Could not retrieve RoomState: ${error.message}`);
      throw error; // Allows caller to handle or log the error further if necessary
    } finally {
      roomState_loading.value = false; // Ensure that the loading indicator is turned off
    }

  };

  /////

  // Assuming 'loading', 'currentRoomState', 'currentRoomExits' are reactive refs outside this function
  async function examineCurrentRoom(GameId) {
    roomState_loading.value = true;

    const config = {
      url: `/api/games/${GameId}/current-room/examine`,
      method: "GET",
    };
    try {
      const { data, error } = await callExternalApi({ config });
      if (error) {
        throw new Error(error.message); // Propagate a clear error message up the chain
      }
      currentRoomState.value = data;  // Update the room state with the returned data
      return data; // Return data for chaining or confirmation of success
    } catch (error) {
      // Log and display error using a centralized alert system
      useAlertStore().addAlert('error', `Could not retrieve RoomState: ${error.message}`);
      throw error; // Allows caller to handle or log the error further if necessary
    } finally {
      roomState_loading.value = false; // Ensure that the loading indicator is turned off
    }
  }


  /////
  // Assuming 'loading', 'currentRoomState' are reactive refs outside this function
  async function move(GameId, direction) {
    roomState_loading.value = true;  // Assume loading is a reactive state managed externally
  
    const config = {
      url: `/api/games/${GameId}/move`,
      method: "PUT",
      data: { 'direction': direction },
    };
    try {
      const { data, error } = await callExternalApi({ config });
      if (error) {
        throw new Error(error.message);  // Centralize throwing of errors
      }
      currentRoomState.value = data;  // Update current room state with the response data
      return data;  // Return data for further processing or chaining
    } catch (error) {
      // Use a centralized alert store to manage and display error messages
      useAlertStore().addAlert('error', `Could not move: ${error.message}`);
      throw error;  // Re-throw error if you need to handle it further up the call chain
    } finally {
      roomState_loading.value = false;  // Ensure loading is turned off regardless of success or failure
    }
  }
  

  /////
  async function endGame(GameId) {
    const config = {
      url: `/api/games/${GameId}`,
      method: "DELETE",
    };
    const { data, error } = await callExternalApi({ config });
    
    if (error)
    {
        const alertStore = useAlertStore();
        alertStore.addAlert('error', error.message);
    }
    games.value = games.value.filter( (x) => x.id !== GameId)
  };


  /////
  async function startGame() {
    games_loading.value = true;
    
    const config = {
      url: `/api/games/start`,
      method: "POST",
    };

    try {
      const { data, error } = await callExternalApi({ config });
      if (error) {
        throw new Error(error.message);  // Centralize throwing of errors
      }
      currentGame.value = data;  // Update current room state with the response data
      games.value.push(data);
      router.push(`/play-game/${currentGame.value.id}`);
      return data;  // Return data for further processing or chaining
    } catch (error) {
      // Use a centralized alert store to manage and display error messages
      useAlertStore().addAlert('error', `Could not start Game: ${error.message}`);
      throw error;  // Re-throw error if you need to handle it further up the call chain
    } finally {
      games_loading.value = false;  // Ensure loading is turned off regardless of success or failure
    }
    
  }

  return { games, getGameById, currentRoomState, exitsLocked, currentRoomInfo, startGame, getCurrentRoomInfo, endGame, getGames, examineCurrentRoom, move, examineObject, interactObject, games_loading, roomInfo_loading, roomState_loading }
  
});