<template>
    <div id="app">
      <router-view/>
    </div>
</template>

<script>
import { mapActions, } from 'vuex';

export default {
    name: "App",
    components: {
    },
    methods: {
      ...mapActions(['getUserInfo']),
    },
    computed: {

    },
    created() {
        this.getUserInfo()
    }
}
</script>