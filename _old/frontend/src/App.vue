<template>
    <div id="app">
      <router-view/>
    </div>
</template>

<script>
import { apiService } from "@/common/api.service.js"
export default {
    name: "App",
    components: {
    },
    methods: {
      async setUserInfo() {
        const dataUser = await apiService("/api/user/current-user/");
        const requestUser = dataUser["email"];
        const dataPosition = await apiService("/api/user/current-position/");
        const requestPosition = dataPosition["position"]
        window.localStorage.setItem("email", requestUser);
        window.localStorage.setItem("position", requestPosition);
      },
    },
    created() {
        this.setUserInfo();
    }
}
</script>