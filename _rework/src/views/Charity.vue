<template>
<div class="row plain-element">
  <div class="row header details-header">
      <div class="col-md-2 text-right plain-element img-column">
          <img src="@/assets/img/charity.jpg" class="img responsive img-header">
      </div>
      <div class="col-md-8 text-left">
          <div class="box">
              <h5>This month we support: </h5>
              <a href="" class="donation-button">
                  <i class="fas fa-donate"></i>
                  <label class="badge">12</label>
              </a>
              <router-link :to="{name: 'charity-create'}" v-if="this.requestPosition == 'admin'" class="btn-algorithm green">New Charity</router-link>
          </div>
          <p>
            Fundraising is a great way to engage your friends, family and community to make a difference in the world.
            Today you can turn pretty much any activity into a charity event and start fundraising action for your
            favourite charities. If you want to start your own fundraising project and you need some help, please contact your program manager.
          </p>
          <h6>Charities: &nbsp; <b class="counter">{{this.countCharities}}</b></h6>
          <h6>Donations: &nbsp; <b class="counter">768 </b> &euro;</h6>
      </div>
  </div>
  <div class="dashboard-cards">
    <div class="row row-cards">
        <CharityComponent
          v-for="charity in charities"
          :charity="charity"
          :key="charity.id"
          @delete-charity="deleteCharity"
        />
    </div>
  </div>
</div>
</template>



<script>
import { apiService } from "@/common/api.service.js";
import CharityComponent from "@/components/CharityComponent.vue"

export default {
  name: 'charity',
  components: {
    CharityComponent
  },
  data() {
    return {
      search: "",
      charities: [],
      countCharities: 0,
      requestUser: null,
      requestPosition: null,
    }
  },
  methods: {
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("email");
    },
    setRequestPosition() {
      this.requestPosition = window.localStorage.getItem("position");
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