<template>
<div class="row plain-element">
  <div class="row header details-header">
      <div class="col-md-2 text-right plain-element img-column">
          <img src="@/assets/img/propose-project.jpg" class="img responsive img-header">
      </div>
      <div class="col-md-8 text-left">
          <div class="box">
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
      <div class="row row-cards">
          <div class="col-md-3 plain-element">
              <div class="card insights-card">
                  <div class="card-header">
                      <img src="@/assets/img/icons/gear.png" class="img-responsive">
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
</template>




<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "ProjectTeamRequirements",
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
    }
  },
  methods: {
    onSubmit() {
      let endpoint = `/projects/team-requirements/${this.id}/`;
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
}
</script>
