<template>
<div v-if="requestUser == projectPM" class="row plain-element">
  <div class="row header details-header">
      <div class="col-md-1 text-left plain-element img-column">
          <img src="https://project-gamification.s3-eu-west-1.amazonaws.com/static/img/propose-project.jpg" class="img responsive img-header">
      </div>
      <div class="col-md-9 col-lg-6 text-left plain-element">
          <div class="box box-details">
              <h5>Report Project Issue</h5>
          </div>
      </div>
  </div>
  <div class="dashboard-cards">
        <div class="row row-form">
          <div class="col-sm-8 col-md-6 col-lg-5 plain-element">
              <div class="card form-card">
                  <div class="card-header">
                      <img src="https://project-gamification.s3-eu-west-1.amazonaws.com/static/img/icons/gear.png" class="img-responsive">
                      <h5> Report Project Issue </h5>
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
                                <input v-model="issueName" name="issueName" class="form-control"/>
                            </div>
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>Description:</h6>
                            </div>
                            <div class="input-field col s8">
                                <input v-model="issueDescription" name="issueDescription" class="form-control"/>
                            </div>
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>Cost:</h6>
                            </div>
                            <div class="input-field col s8">
                                <input v-model="issueCost" name="issueCost" type="number" min="0" max="450" class="form-control" style="text-align: left"/>
                            </div>
                          </div>
                          <div class="row"></div>
                          <button type="submit" class="btn-proceed"><span>Report Project Issue <i
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
import { apiService } from "@/common/api.service.js";
import NoPermissionComponent from "@/components/NoPermissionComponent.vue"
export default {
  name: 'IssueCreate',
  props: {
    id: {
      required: true,
    }
  },
  components: {
    NoPermissionComponent
  },
  data() {
    return {
      error: "",
      issueName: null,
      issueDescription: null,
      issueCost: null,
      projectPM: null,
      requestUser: null,
    }
  },
  methods: {
    setRequestUser() {
        this.requestUser = window.localStorage.getItem("email");
    },
    getProjectData() {
      let endpoint = `/api/projects/projects/${this.id}/`;
      apiService(endpoint)
          .then(data => {
            this.projectPM = data.pm_email;
          })
    },
    onSubmit() {
      if (!this.issueName || !this.issueDescription || !this.issueCost) {
        this.error = "Fields can't be empty";
      } else {
        let endpoint = `/api/projects/${this.id}/issue-create/`;
        let method = "POST";
        apiService(endpoint, method, {project: this.id,
                                      name: this.issueName,
                                      description: this.issueDescription,
                                      cost: this.issueCost, assigned_to: this.error})
          .then(data => {
             if (data.non_field_errors) {
                this.error = data.non_field_errors[0]
             } else if (!data) {
                this.error = "Something went wrong. Try again later"
            } else {
              this.$router.push({
                    name: "project-details",
                    params: { id: this.id }
              })
            }
        })
      }
    }
  },
  created() {
    this.setRequestUser();
    this.getProjectData();
    document.title = "Report Project Issue";
  }
}
</script>