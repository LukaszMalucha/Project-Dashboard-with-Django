<template>
<div class="row plain-element">
    <div class="row header details-header">
      <div class="col-md-2 text-right plain-element img-column">
          <img src="@/assets/img/propose-project.jpg" class="img responsive img-header">
      </div>
      <div class="col-md-8 text-left">
          <div class="box">
              <h5>Join Team</h5>
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
          <div class="col-md-4 plain-element">
              <div class="card insights-card">
                  <div class="card-header">
                      <img src="@/assets/img/icons/gear.png" class="img-responsive">
                      <h5> Join Team </h5>
                  </div>
                  <form @submit.prevent="onSubmit" class="form-content form-wide">
                      <fieldset class="form-box">
                          <div id="formError" class="row row-error text-center">
                          {{ error }}
                          </div>
                          <div class="row plain-element">
                          <ul>
                            <li v-for="element in skillList" :key="element">
                              <label>
                                <input v-model="skill" name="skill" :value="element" type="radio"/>
                                <span>{{element}}</span>
                              </label>
                            </li>
                          </ul>
                          </div>
                          <div class="row"></div>
                          <button type="submit" class="btn-proceed"><span>Join Team <i
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
  name: "TeamJoin",
  props: {
    id: {
      required: true,
    }
  },
  data() {
    return {
      requestUser: null,
      error: null,
      skill: null,
      skillList: ['html', 'css', 'js', 'db', 'python']
    }
  },
  methods: {
    setRequestUser() {
        this.requestUser = window.localStorage.getItem("email");
    },
    onSubmit() {
      let endpoint = `/api/projects/${this.id}/team-join/`;
      let method = "POST";
      apiService(endpoint, method, {project: this.id, member: this.requestUser, committed_skill: this.skill})
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
    document.title = "Join Project Team";
  }
}
</script>
