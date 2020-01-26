<template>
<div v-if="requestUser == projectPM" class="row plain-element">
  <div class="row header details-header">
      <div class="col-md-1 text-left plain-element img-column">
          <img src="https://project-gamification.s3-eu-west-1.amazonaws.com/static/img/propose-project.jpg" class="img responsive img-header">
      </div>
      <div class="col-md-9 col-lg-6 text-left plain-element">
          <div class="box box-details">
              <h5>Define Project Skill Requirements</h5>
          </div>
          <p>
            Project team requirements is a skillset that must be completed to ensure the success of the project.
            They provide a clear picture of the work that needs to be done. The benefits of effectively gathering project
            team include cost reduction, higher project success rates, more effective change management,
            and improved communication.
          </p>
      </div>
  </div>
  <div class="dashboard-cards">
      <div class="row row-form">
          <div class="col-sm-6 col-md-4 col-lg-3 plain-element">
              <div class="card form-card">
                  <div class="card-header">
                      <img src="https://project-gamification.s3-eu-west-1.amazonaws.com/static/img/icons/gear.png" class="img-responsive">
                      <h5> Team Requirements </h5>
                  </div>
                  <form @submit.prevent="onSubmit" class="form-content form-wide">
                      <fieldset class="form-box">
                          <div id="formError" class="row row-error text-center">
                          {{ error }}
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>HTML:</h6>
                            </div>
                            <div class="input-field col s6">
                                <input v-model="html" name="html" type="number" min="0" max="12" class="form-control"/>
                            </div>
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>CSS:</h6>
                            </div>
                            <div class="input-field col s6">
                                <input v-model="css" name="css" type="number" min="0" max="12" class="form-control"/>
                            </div>
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>JS:</h6>
                            </div>
                            <div class="input-field col s6">
                                <input v-model="js" name="js" type="number" min="0" max="12" class="form-control"/>
                            </div>
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>DB:</h6>
                            </div>
                            <div class="input-field col s6">
                                <input v-model="db" name="db" type="number" min="0" max="12" class="form-control"/>
                            </div>
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>PYTHON:</h6>
                            </div>
                            <div class="input-field col s6">
                                <input v-model="python" name="python" type="number" min="0" max="12" class="form-control"/>
                            </div>
                          </div>
                          <div class="row"></div>
                          <button type="submit" class="btn-proceed"><span>Submit Requirements <i
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
  name: "ProjectTeamRequirements",
  components: {
    NoPermissionComponent
  },
  props: {
    id: {
      required: true,
    }
  },
  data() {
    return {
      error: null,
      html: null,
      css: null,
      js: null,
      db: null,
      python: null,
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
      let endpoint = `/api/projects/${this.id}/team-requirements/`;
      let method = "PUT";
      apiService(endpoint, method, {html: this.html, css: this.css, js: this.js, db: this.db, python: this.python})
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
  },
  created() {
    this.setRequestUser();
    this.getProjectData();
    document.title = "Project Team Requirements";
  }
}
</script>
