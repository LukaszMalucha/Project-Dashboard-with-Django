<template>
<div v-if="getUsername() == getProject().pm_email" class="row plain-element">
    <div class="row header details-header">
      <div class="col m1 text-left plain-element img-column">
          <img src="https://project-gamification.s3-eu-west-1.amazonaws.com/static/img/propose-project.jpg" class="img responsive img-header">
      </div>
      <div class="col m9 l6 text-left plain-element">
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
          <div class="col s6 m5 l4 plain-element">
              <div class="card form-card">
                  <div class="card-header">
                      <img src="https://project-gamification.s3-eu-west-1.amazonaws.com/static/img/icons/gear.png" class="img-responsive">
                      <h5> Reject Team Candidate </h5>
                  </div>
                  <form @submit.prevent="teamReject" class="form-content form-wide">
                      <fieldset class="form-box">
                          <div id="formError" class="row row-error text-center">
                          {{ error }}
                          </div>
                          <div class="row plain-element">
                          <ul>
                            <li v-for="element in getTeamMembership()" :key="element.member_id">
                              <label>
                                <input v-model="member" name="member" :value="element.member_id" type="radio"/>
                                <span class="span-radio">{{element.member_name}} - {{element.committed_skill}}</span>
                              </label>
                            </li>
                          </ul>
                          </div>
                          <div class="row"></div>

                      </fieldset>
                          <button type="submit" class="btn-proceed"><span>Reject Team Candidate <i
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
import NoPermissionComponent from "@/components/NoPermissionComponent.vue";
import { mapGetters, mapActions } from "vuex";

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
      member: "",

    }
  },
  methods: {
    ...mapGetters(["getUsername", "getPosition", "getProject", "getTeamMembership",
                    "getTeamRequirements", "getTeamComposition", "getProjectMessages"]),
    ...mapActions(["fetchProjectDetails", "performTeamReject"]),

    teamReject() {
      this.performTeamReject({"project" : this.id, "member" : this.member})
    }



  },
  created() {
    this.fetchProjectDetails(this.id);
    document.title = "Reject Team Candidate";
  }
}
</script>
