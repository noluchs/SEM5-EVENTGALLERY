<script setup>

import { useRouter } from "vue-router";
import { useAuthStore } from '@/stores/auth.store';
import { useForm, useField } from 'vee-validate';
import * as Yup from 'yup';

const router = useRouter();
const authStore = useAuthStore();

// Define the validation schema
const schema = Yup.object({
  name: Yup.string().required('Nickname is required'),
  email: Yup.string().email('Must be a valid email').required('Email is required'),
  password: Yup.string().min(6, 'Password must be at least 6 characters long').required('Password is required'),
  token: Yup.string().required('Invitation token is required')
});

// Setup form handling with VeeValidate
const { handleSubmit, errors } = useForm({
  validationSchema: schema
});

const { value: name } = useField('name');
const { value: email } = useField('email');
const { value: password } = useField('password');
const { value: token } = useField('token');

const onSubmit = handleSubmit(values => {
  authStore.register(values.name, values.email, values.password, values.token);
  router.push('/');
});

</script>


<template>
    <div class="container" style="max-width: 512px;">
        <div class="row g-2">
            <div class="col gy-4">
                <legend>Please Register</legend>
                <form @submit.prevent="onSubmit">
                <div class="form-group mb-2">
                    <label>Your Nickname</label>
                    <input v-model="name" type="text" class="form-control"/>
                    <span v-if="errors.name" class="error-text">{{ errors.name }}</span>
                </div>
                <div class="form-group mb-2">
                    <label>Valid E-Mail Address</label>
                    <input v-model="email" type="email" class="form-control"/>
                    <span v-if="errors.email" class="error-text">{{ errors.email }}</span>
                </div>
                <div class="form-group mb-2">
                    <label>Password</label>
                    <input v-model="password" type="password" class="form-control"/>
                    <span v-if="errors.password" class="error-text">{{ errors.password }}</span>
                </div>
                <div class="form-group mb-2">
                    <label>Invitation Token</label>
                    <input v-model="token" type="text" class="form-control"/>
                    <span v-if="errors.token" class="error-text">{{ errors.token }}</span>
                </div>
                <div class="form-group">
                    <button type="submit" class="btn btn-primary">Submit</button>
                    <router-link to="/" class="btn btn-link">Cancel</router-link>
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