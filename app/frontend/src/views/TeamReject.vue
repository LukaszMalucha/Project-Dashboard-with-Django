<template>
<div v-if="requestUser == projectPM" class="row plain-element">
    <div class="row header details-header">
      <div class="col-md-1 text-left plain-element img-column">
          <img src="@/assets/img/propose-project.jpg" class="img responsive img-header">
      </div>
      <div class="col-md-9 col-lg-6 text-left plain-element">
          <div class="box box-details">
              <h5>Reject Team Candidate</h5>
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
          <div class="col-sm-6 col-md-5 col-lg-4 plain-element">
              <div class="card form-card">
                  <div class="card-header">
                      <img src="@/assets/img/icons/gear.png" class="img-responsive">
                      <h5> Reject Team Candidate </h5>
                  </div>
                  <form @submit.prevent="onSubmit" class="form-content form-wide">
                      <fieldset class="form-box">
                          <div id="formError" class="row row-error text-center">
                          {{ error }}
                          </div>
                          <div class="row plain-element">
                          <ul>
                            <li v-for="element in teamMembership" :key="element.member_id">
                              <label>
                                <input v-model="member" name="member" :value="element.member_id" type="radio"/>
                                <span>{{element.member_name}} - {{element.committed_skill}}</span>
                              </label>
                            </li>
                          </ul>
                          </div>
                          <div class="row"></div>
                          <button type="submit" class="btn-proceed"><span>Reject Team Candidate <i
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
import NoPermissionComponent from "@/components/NoPermissionComponent.vue";

export default {
  name: "TeamReject",
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
      error: "",
      requestUser: null,
      member: "",
      projectPM: null,
      teamMembership: [],
      phaseList: ["proposed", "analysis", "development", "testing", "deployment"],
    }
  },
  methods: {
    setRequestUser() {
        this.requestUser = window.localStorage.getItem("email");
    },
    getProjectTeamData() {
      let endpoint = `/api/projects/projects/${this.id}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.teamMembership = data.team_membership;
            this.projectPM = data.pm_email;
          } else {
            this.teamMembership = null;
            document.title = "404 - Page Not Found"
          }
        })
    },
    onSubmit() {
      let endpoint = `/api/projects/${this.id}/team-reject/${this.member}/`;
      let method = "DELETE";
      apiService(endpoint, method)
        .then(data => {
           if (data.non_field_errors) {
              this.error = data.non_field_errors[0]
           } else if (!data) {
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
    this.getProjectTeamData();
    document.title = "Reject Team Candidate";
  }
}
</script>
