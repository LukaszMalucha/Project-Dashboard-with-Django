<template>
  <div class="col s12 m6 l4">
    <div class="card horizontal">
      <div class="card-image">
            <img :src="charity.image">
      </div>
      <div class="card-stacked">
                <div class="card-content">
                    <span class="flex">
                      <h5>{{ charity.name| truncatechars(20) }}</h5>
                      <button v-if="this.requestPosition == 'admin'" class="btn-inline-delete" @click="triggerDeleteCharity">Delete</button>
                    </span>
                    <p>{{ charity.description| truncatechars(60) }}</p>
                        <button type="submit" @click="triggerAddDonation" class="btn btn-algorithm green">
                          Donate 5 <img src="https://project-gamification.s3-eu-west-1.amazonaws.com/static/img/leancoin-button.png" class="icon-small">
                        </button>

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
    triggerAddDonation() {
      this.$emit("add-donation", this.charity)
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
