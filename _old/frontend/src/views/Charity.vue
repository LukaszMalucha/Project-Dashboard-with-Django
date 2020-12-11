<template>
<div class="row plain-element">
  <div class="row header details-header">
      <div class="col-md-1 text-left plain-element img-column">
          <img src="@/assets/img/charity.jpg" class="img responsive img-header">
      </div>
      <div class="col-sm-12 col-md-10 col-lg-7 text-left plain-element">
          <div class="box box-details">
              <h5>Fundraising Events </h5>
              <router-link :to="{name: 'charity-create'}" v-if="this.requestPosition == 'admin'" class="btn-algorithm green">New Charity</router-link>
              <div class="plain element" v-if="this.inCart > 0">
                <router-link :to="{name: 'charity-donations', params: { cart: checkout , cartList: checkoutList}}" class="donation-button">
                  <i class="fas fa-donate"></i>
                  <label class="badge glow">{{ inCart }}</label>
                </router-link>
              </div>

          </div>
          <p>
            Fundraising is a great way to engage your friends, family and community to make a difference in the world.
            Today you can turn pretty much any activity into a charity event and start fundraising action for your
            favourite charities. If you want to start your own fundraising project, contact program manager.
          </p>
          <h6>We collected: <b class="counter">728</b> &euro;</h6>
      </div>
  </div>
  <div class="dashboard-cards">
    <div class="row row-form">
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
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("email");
    },
    setRequestPosition() {
      this.requestPosition = window.localStorage.getItem("position");
    },
    addDonation(charity) {
      if (!this.checkoutList.includes(charity.id)) {
        this.checkoutList.push(charity.id)
        this.checkout.push(charity);
      }
    },
    getCharityData(){
      let endpoint = "charity/charities/";
      apiService(endpoint)
        .then(data => {
          this.charities.push(...data.results);
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