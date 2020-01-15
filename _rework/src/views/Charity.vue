<template>
<div class="row plain-element">
  <div class="row header details-header">
      <div class="col-md-2 text-right plain-element img-column">
          <img src="@/assets/img/charity.jpg" class="img responsive img-header">
      </div>
      <div class="col-md-8 text-left">
          <div class="box">
              <h5>Fundraising Events </h5>
              <router-link :to="{name: 'charity-create'}" v-if="this.requestPosition == 'admin'" class="btn-algorithm green">New Charity</router-link>
              <div class="plain element" v-if="this.inCart > 0">
                <router-link :to="{name: 'charity-donations', params: { cart: checkout }}" class="donation-button">
                  <i class="fas fa-donate"></i>
                  <label class="badge glow">{{ inCart }}</label>
                </router-link>
              </div>

          </div>
          <p>
            Fundraising is a great way to engage your friends, family and community to make a difference in the world.
            Today you can turn pretty much any activity into a charity event and start fundraising action for your
            favourite charities. If you want to start your own fundraising project and you need some help, please contact your program manager.
          </p>
          <h6>Total Events: <b class="counter">{{this.countCharities}}</b></h6>
          <h6>We collected: <b class="counter">728</b> &euro;</h6>
      </div>
  </div>
  <div class="dashboard-cards">
    <div class="row row-cards">
        <CharityComponent
          v-for="charity in charities"
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
import { apiService } from "@/common/api.service.js";
import CharityComponent from "@/components/CharityComponent.vue"

export default {
  name: 'Charity',
  components: {
    CharityComponent
  },
  data() {
    return {
      charities: [],
      countCharities: 0,
      requestUser: null,
      requestPosition: null,
      checkout: [],
      check: [],
    }
  },
  computed: {
    forSale() { return this.charities },
    inCart() { return this.checkout.length },
  },
  methods: {
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("email");
    },
    setRequestPosition() {
      this.requestPosition = window.localStorage.getItem("position");
    },
    addDonation(charity) {
      if (!this.check.includes(charity.id)) {
        this.check.push(charity.id)
        this.checkout.push(charity);
        window.console.log(this.check);
        window.console.log(this.checkout);
      }
    },
    getCharityData(){
      let endpoint = "charity/charities/";
      apiService(endpoint)
        .then(data => {
          this.charities.push(...data.results);
          this.countCharities = this.charities.length
        }).then (
          window.console.log(this.charities)
        )
    },
    async deleteCharity(charity) {
      let endpoint = `/charity/charities/${charity.id}/`;
      try {
        await apiService(endpoint, "DELETE")
        this.$delete(this.charities, this.charities.indexOf(charity))
      }
      catch (err) {
        window.console.log(err)
      }
    },

  },
  created() {
    this.getCharityData()
    this.setRequestUser();
    this.setRequestPosition();
    document.title = "Charity Donations";

  }
}
</script>