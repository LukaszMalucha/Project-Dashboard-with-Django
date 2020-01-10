<template>
  <div class="col s12 m4">
    <div class="card horizontal">
      <div class="card-image">
            <img :src="charity.image">
      </div>
      <div class="card-stacked">
                <div class="card-content">
                    <span class="flex">
                      <h5>{{ charity.name| truncatechars(16) }}</h5>
                      <button v-if="this.requestPosition == 'admin'" class="btn-inline-delete" @click="triggerDeleteCharity">Delete</button>
                    </span>
                    <p>{{ charity.description| truncatechars(60) }}</p>

                    <form class="form-inline" method="post" action="">
                        <button type="submit" class="btn btn-algorithm green">Donate 5€</button>
                    </form>

                </div>
            </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "CharityComponent",
  props: {
    charity: {
      type: Object,
      required: true,

    }
  },
  data() {
    return {
      requestPosition: null,
    }
  },
  filters: {
      truncatechars (value, limit) {
          if (value.length > limit) {
              value = value.substring(0, limit) + "...";
          }
          return value
      }
  },
  methods: {
    triggerDeleteCharity() {
      // emit an event to delete an charity instance
      this.$emit("delete-charity", this.charity)
    },
    setRequestPosition() {
      this.requestPosition = window.localStorage.getItem("position");
    },
  },
  created() {
    this.setRequestPosition();
  }

}
</script>
