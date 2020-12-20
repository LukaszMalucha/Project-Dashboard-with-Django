<template>
<div class="row plain-element">
  <div class="row header details-header">
      <div class="col m1 text-left plain-element img-column">
          <img src="https://project-gamification.s3-eu-west-1.amazonaws.com/static/img/charity.jpg" class="img responsive img-header">
      </div>
      <div class="col s12 m10 l8 text-left plain-element">
          <div class="box box-details">
              <h5>Fundraising Events</h5>
              <router-link :to="{name: 'charity-create'}" v-if="getPosition() == 'admin'" class="btn-algorithm green">New Charity</router-link>
              <div class="plain element" v-if="this.inCart > 0">
                <router-link :to="{name: 'charity-donations', params: { cart: checkout , cartList: checkoutList}}" class="donation-button">
                  <i class="fas fa-donate"></i>{{ inCart }}

                </router-link>
              </div>

          </div>
          <p v-if="getPosition()">
            Fundraising is a great way to engage your friends, family and community to make a difference in the world.
            Today you can turn pretty much any activity into a charity event and start fundraising action for your
            favourite charities. If you want to start your own fundraising project, contact manager.
          </p>
          <p>
            Please Log In to visit the Charity Actions
          </p>
          <h6 v-if="getPosition()">We collected: <b class="counter">728</b> &euro;</h6>
      </div>
  </div>
  <div class="dashboard-cards">
    <div class="row row-form">
        <CharityComponent
          v-for="charity in getCharityList()"
          :charity="charity"
          :key="charity.id"
          @delete-charity="deleteCharity"
          @add-donation="addDonation"
        />
    </div>
  </div>
</div>
</template>



<script>
import CharityComponent from "@/components/CharityComponent.vue"

import { mapGetters, mapActions } from "vuex";

export default {
  name: 'Charity',
  components: {
    CharityComponent
  },
  data() {
    return {
      charities: [],
      requestUser: null,
      requestPosition: null,
      checkout: [],
      checkoutList: [],
    }
  },
  computed: {
    forSale() { return this.charities },
    inCart() { return this.checkout.length },
  },
  methods: {
    ...mapGetters([ "getCharityList", "getPosition"]),
    ...mapActions(["fetchCharityList", "performDeleteCharity"]),
    addDonation(charity) {
      if (!this.checkoutList.includes(charity.id)) {
        this.checkoutList.push(charity.id)
        this.checkout.push(charity);
      }
    },
    deleteCharity(charity) {
      this.performDeleteCharity(charity)
    }
  },
  created() {
    document.title = "Charity Donations";
    this.fetchCharityList()

  }
}
</script>