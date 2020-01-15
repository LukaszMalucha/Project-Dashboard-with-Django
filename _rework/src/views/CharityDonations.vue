<template>
<div class="row plain-element">
  <div class="row header details-header">
    <div class="col-md-2 text-right plain-element img-column">
        <img src="@/assets/img/charity.jpg" class="img responsive img-header">
    </div>
    <div class="col-md-8 text-left">
        <div class="box">
            <h5>My Donations</h5>
            <router-link :to="{name: 'charity-donate', params: { checkout: cart }}" class="btn-algorithm green"><i class="fas fa-1x fa-donate"></i> Proceed</router-link>
        </div>
        <p>
            After a successful transaction, for each LeanCoin Token you spend, the company will donate 1 &euro; for the selected Fundraising action.
            Fundraising is a great way to engage your friends, family and community to make a difference in the world. If you want to start your own fundraising project and need help, contact your program manager.
        </p>
    </div>
  </div>
  <div class="dashboard-cards">
    <div class="row row-cards">
      <div v-for="charity in cart" class="col s12 m4" :key="charity.id">
        <div class="card horizontal">
          <div class="card-image">
                <img :src="charity.image">
          </div>
          <div class="card-stacked">
              <div class="card-content">
                  <span class="flex">
                    <h5>{{ charity.name| truncatechars(16) }}</h5>
                    <button class="btn-inline-delete" @click="triggerDeleteDonation(charity)">Delete</button>
                  </span>
                  <p>{{ charity.description| truncatechars(60) }}</p>
              </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>



<script>
export default {
  name: 'CharityDonations',
  components: {
  },
  props: {
    cart: {
      type: Array,
    }
  },
  data() {
    return {
      donations: [],
    }
  },
  methods: {
    triggerDeleteDonation(charity) {
        this.cart.splice(this.cart.indexOf(charity), 1);
        window.console.log(this.cart)
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
  created() {
    document.title = "Charity Donations";
    window.console.log(this.cart)
  }
}
</script>