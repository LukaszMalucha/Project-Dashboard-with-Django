<template>
<div v-if="requestPosition == 'admin'" class="row plain-element">
  <div class="row header details-header">
      <div class="col-md-1 text-left plain-element img-column">
          <img src="@/assets/img/charity.jpg" class="img responsive img-header">
      </div>
      <div class="col-sm-12 col-md-10 col-lg-7 text-left plain-element">
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
          <div class="col-sm-8 col-md-6 col-lg-5 plain-element">
              <div class="card form-card">
                  <div class="card-header">
                      <img src="@/assets/img/icons/charity.png" class="img-responsive">
                      <h5> Start Fundraising Action </h5>
                  </div>
                  <form @submit.prevent="onSubmit" class="form-content form-wide" enctype="multipart/form-data">
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
                          <button type="submit" class="btn-proceed"><span>Propose Charity <i
                                  class="far fa-arrow-alt-circle-right"></i></span>
                          </button>
                      </fieldset>
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
import axios from 'axios'
import { CSRF_TOKEN } from "@/common/csrf_token.js"
import router from "@/router.js"
import NoPermissionComponent from "@/components/NoPermissionComponent.vue"
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
    ...mapActions(["fetchCharityList", "performDeleteCharity"]),
    handleFileUpload() {
      this.charityImage = this.$refs.file.files[0];
    },
    onSubmit() {
      if (!this.charityName || !this.charityDescription || !this.charityImage) {
        this.error = "Fields can't be empty";
      } else {
        let formData = new FormData();
        formData.append("name", this.charityName);
        formData.append("description", this.charityDescription);
        formData.append("image", this.charityImage)
        axios.post('/charity/charities/', formData,
        { headers: { 'Content-Type': undefined,'X-CSRFTOKEN': CSRF_TOKEN} } )
          .then(response => {
            window.console.log(response);
            router.push({
              name: 'charity',
            })
          })
          .catch(error => {
            window.console.log(error.response);
            document.getElementById("formError").textContent = error.response.statusText;
          })
        }
      }
  },
  created() {
    this.setRequestPosition();
    document.title = "New Fundraising Idea";
  }
}
</script>