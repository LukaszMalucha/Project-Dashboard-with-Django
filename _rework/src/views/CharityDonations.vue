<template>
<div v-if="this.checkout_cart.length == undefined" class="row plain-element">
  <div class="row header details-header">
      <div class="col-md-1 text-left plain-element img-column">
          <img src="@/assets/img/charity.jpg" class="img responsive img-header">
      </div>
      <div class="col-md-8 text-left plain-element">
          <div class="box">
              <h5>Your Donation List is Empty </h5>
              <router-link :to="{name: 'charity'}" class="btn-algorithm green"><i class="fas fa-1x fa-donate"></i> Back to Charities</router-link>
          </div>
        <p>
            After a successful transaction, for each LeanCoin Token you spend, the company will donate 1 &euro; for the selected Fundraising action.
            Fundraising is a great way to engage your friends, family and community to make a difference in the world. If you want to start your own fundraising project and need help, contact your program manager.
        </p>
    </div>
  </div>
</div>
<div v-else class="row plain-element">
  <div class="row header details-header">
    <div class="col-md-1 text-left plain-element img-column">
        <img src="@/assets/img/charity.jpg" class="img responsive img-header">
    </div>
    <div class="col-md-8 text-left plain-element">
        <div class="box">
            <h5>My Donations</h5>
            <router-link v-if="this.checkout_cart.length > 0" :to="{name: 'charity-donate', params: { checkout: this.checkoutList }}" class="btn-algorithm green"><i class="fas fa-1x fa-donate"></i> Proceed</router-link>
        </div>
        <p>
            After a successful transaction, for each LeanCoin Token you spend, the company will donate 1 &euro; for the selected Fundraising action.
            Fundraising is a great way to engage your friends, family and community to make a difference in the world. If you want to start your own fundraising project and need help, contact your program manager.
        </p>
    </div>
  </div>
  <div class="dashboard-cards">
    <div class="row row-cards">
      <div v-for="charity in this.checkout_cart" class="col s12 m4" :key="charity.id">
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
    },
    cartList: {
      type: Array,
    }
  },
  data() {
    return {
      donations: [],
      checkout_cart: {},
      checkoutList: [],
    }
  },
  methods: {
    getCartData() {
      if (this.cart) {
        this.checkout_cart = this.cart;
        this.checkoutList = this.cartList;
      }
    },
    triggerDeleteDonation(charity) {
          this.cart.splice(this.cart.indexOf(charity), 1);
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
    this.getCartData();
  }
}
</script>