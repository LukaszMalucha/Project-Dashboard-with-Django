<template>
<div v-if="getPosition() == 'admin'" class="row plain-element">
  <div class="row header details-header">
      <div class="col m1 text-left plain-element img-column">
          <img src="@/assets/img/charity.jpg" class="img responsive img-header">
      </div>
      <div class="col s12 m10 l7 text-left plain-element">
          <div class="box box-details">
              <h5>New Fundraising Action</h5>
          </div>
          <p>
            Fundraising is a great way to engage your friends, family and community to make a difference in the world.
            Today you can turn pretty much any activity into a charity event and start fundraising action for your
            favourite charities. If you want to start your own fundraising project, contact program manager.
          </p>
      </div>
  </div>
  <div class="dashboard-cards">
      <div class="row row-form">
          <div class="col s8 m6 l5 plain-element">
              <div class="card form-card">
                  <div class="card-header">
                      <img src="@/assets/img/icons/charity.png" class="img-responsive">
                      <h5> Start Fundraising Action </h5>
                  </div>
                  <form @submit.prevent="createCharity" class="form-content form-wide" enctype="multipart/form-data">
                      <fieldset class="form-box">
                          <div id="formError" class="row row-error text-center">
                          {{ error }}
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>Name:</h6>
                            </div>
                            <div class="input-field col s8">
                                <input v-model="charityName" name="Name" class="form-control"/>
                            </div>
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>Description:</h6>
                            </div>
                            <div class="input-field col s8">
                                <input v-model="charityDescription" name="Description" class="form-control"/>
                            </div>
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>Charity Image:</h6>
                            </div>
                            <div class="input-field col s8">
                                <input type="file" id="file" ref="file"
                                    v-on:change="handleFileUpload()"
                                      class="form-control file_input"  accept=".jpg,.png">
                            </div>
                          </div>
                          <div class="row"></div>

                      </fieldset>
                      <button type="submit" class="btn-proceed"><span>Propose Charity <i
                                  class="far fa-arrow-alt-circle-right"></i></span>
                          </button>
                  </form>
              </div>
          </div>
      </div>
  </div>
</div>
<div v-else class="row plain-element">
    <NoPermissionComponent/>
</div>
</template>



<script>


import NoPermissionComponent from "@/components/NoPermissionComponent.vue"
import { mapGetters, mapActions } from "vuex";

export default {
  name: 'CharityCreate',
  components: {
    NoPermissionComponent
  },
  data() {
    return {
      error: "",
      charityName: null,
      charityDescription: null,
      charityImage: null,
      requestPosition: null,
    }
  },
  methods: {
    ...mapGetters([ "getCharityList", "getPosition"]),
    ...mapActions(["fetchCharityList", "performCreateCharity"]),
    handleFileUpload() {
      this.charityImage = this.$refs.file.files[0];
    },
    createCharity() {
      if (!this.charityName || !this.charityDescription || !this.charityImage) {
        this.error = "Fields can't be empty";
      } else {
        this.performCreateCharity({"charityName": this.charityName,
                                   "charityDescription": this.charityDescription,
                                   "charityImage": this.charityImage
                                  })
      }
    }
  },
  created() {
    document.title = "New Fundraising Idea";
  }
}
</script>