<script setup>

import { useRouter } from "vue-router";
import { useAuthStore } from '@/stores/auth.store';
import { storeToRefs } from 'pinia';

const router = useRouter();
const authStore = useAuthStore();

const { inviteToken } = storeToRefs(useAuthStore());

const handleGetToken =  () => {
  authStore.getInviteToken("boris.langer@gmx.net");
};

</script>

<template>
    <div class="container" style="max-width: 512px; margin: auto; text-align: center; padding-top: 20px;">
        <div class="row g-2">
            <div class="col-12 gy-4">
                <p style="margin-bottom: 20px;">With this token you can invite other users. Send the token by email or other means.</p>
                <div class="form-floating mb-3">
                    <textarea class="form-control" placeholder="generate a token" id="floatingTextarea2" style="height: 120px">{{ inviteToken }}</textarea>
                    <label for="floatingTextarea2">Token</label>
                </div>
                <button type="button" @click="handleGetToken()" class="btn btn-danger">
                    <span class="bi-x-circle"></span> Get Invite Token
                </button>
            </div>
        </div>
    </div>
</template>