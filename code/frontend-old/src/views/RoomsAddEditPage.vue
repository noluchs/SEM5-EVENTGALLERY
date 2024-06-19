<script setup>
import { ref, onMounted } from 'vue';
import { useField, useForm } from 'vee-validate';
import * as Yup from 'yup';
import { useRouter, useRoute } from 'vue-router';
import { useRoomsStore } from '@/stores/rooms.store';
import { useAlertStore } from '@/stores/alert.store';

const router = useRouter();
const route = useRoute();
const id = route.params.id;
const roomsStore = useRoomsStore();
const alertStore = useAlertStore();

const title = ref(id ? 'Edit Room' : 'Add Room');

const urlRegExp = /^(?:([a-z0-9+.-]+):\/\/)(?:\S+(?::\S*)?@)?(?:(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*\.?)(?::\d{2,5})?(?:[/?#]\S*)?$/

const { handleSubmit, errors, setFieldValue } = useForm({
  validationSchema: Yup.object({
    name: Yup.string().required('Room name is required'),
    ms_context: Yup.string(),
    uri: Yup.string().matches(urlRegExp, 'Must be a valid URL').required('URI is required')
  })
});

const { value: name, setValue: setName } = useField('name');
const { value: ms_context, setValue: setMs_context } = useField('ms_context');
const { value: uri, setValue: setUri } = useField('uri');

// Initialize or update form fields reactively
onMounted(() => {
  if (id) {
    const selectedRoom = roomsStore.getRoomById(id);
    if (selectedRoom) {
      setName(selectedRoom.name);
      setMs_context(selectedRoom.ms_context)
      setUri(selectedRoom.uri);
    }
  }
});

// On form submission, pass the form data to the appropriate store function
const onSubmit = handleSubmit(async (values) => {
    try {
        let message;
        if (id) {
            // Pass object directly with name and uri
            await roomsStore.updateRoom(id, { name: values.name, ms_context: values.ms_context, uri: values.uri });
            message = 'Room updated';
        } else {
            await roomsStore.createRoom({ name: values.name, ms_context: values.ms_context, uri: values.uri });
            message = 'Room added';
        }
        alertStore.addAlert('success', message);
        router.push('/all-rooms');
    } catch (error) {
        alertStore.addAlert('error', error.message || 'Failed operation');
    }
});
</script>


<template>
  <div class="container" style="max-width: 512px;">
    <div class="row g-2">
      <div class="col gy-4">
        <legend>{{ title }}</legend>
        <form @submit.prevent="onSubmit">
          <div class="form-group mb-2">
            <label>Room Name</label>
            <input v-model="name" type="text" class="form-control"/>
            <span class="error-text" v-if="errors.name">{{ errors.name }}</span>
          </div>
          <div class="form-group mb-2">
            <label>Microservice Context</label>
            <input v-model="ms_context" type="text" class="form-control"/>
            <span class="error-text" v-if="errors.name">{{ errors.name }}</span>
          </div>
          <div class="form-group mb-2">
            <label>URI or IP</label>
            <input v-model="uri" type="text" class="form-control"/>
            <span class="error-text" v-if="errors.uri">{{ errors.uri }}</span>
          </div>
          <div class="form-group">
            <button type="submit" class="btn btn-primary">Save</button>
            <router-link to="/all-rooms" class="btn btn-link">Cancel</router-link>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>


<style scoped>
.error-text {
  color: rgba(255, 230, 0, 0.903);
  font-weight: bold;
  font-size: 0.875em; /* Example: smaller font size */
}
</style>
