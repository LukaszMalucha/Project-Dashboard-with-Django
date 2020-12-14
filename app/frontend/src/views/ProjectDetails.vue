<template>
  <div class="row plain-element">
    <div class="row header details-header">
      <div class="col m1 text-left plain-element img-column">
        <img src="@/assets/img/project-details.jpg" class="img responsive img-header">
      </div>
      <div class="col m9 l9 text-left plain-element">
        <div class="box box-details" v-if="project">
          <h5>{{ getProject().name }}</h5>
          <button v-if="getPosition() == 'admin'" @click="advanceProject()" class="btn-algorithm green">
            <b v-if="getProject().phase == 'proposed'">Launch Project</b>
            <b v-else>Advance Project</b>
          </button>
          <button v-if="getPosition() == 'admin' && getProject().phase == 'deployment'"
              @click="completeProject()" class="btn-algorithm green">Finish Project!
          </button>
        </div>
        <br>
        <table class="profile-details">
          <tr class>
            <td>Manager:</td>
            <td><b> {{ getProject().pm_name }}</b></td>
          </tr>
          <tr>
            <td>Budget: &nbsp;</td>
            <td><b><img src="@/assets/img/leancoin.png" class="icon"> {{ getProject().budget }}</b></td>
          </tr>
          <tr>
            <td>Phase:</td>
            <td><b>{{ getProject().phase }}</b></td>
          </tr>
        </table>


      </div>
    </div>
    <div class="dashboard-cards">
      <div class="row row-details">
        <div class="col m6 col-left plain-element">

          <div class="row plain-element">
            <div class="col m12 plain-element">
              <div v-if="getProject().phase == 'proposed'" class="card insights-card">
                <div class="card-header">
                  Team Requirements
                  <button v-if="getUsername() == getProject().pm_email" @click="defineTeamRequirements()" class="btn-insights green">
                    Define Team Requirements
                  </button>
                </div>
                <div class="row row-content">
                  <div class="table-responsive table-skills">
                    <table v-if="getTeamRequirements()">
                      <thead>
                      <tr>
                        <th class="text-center"><img src="@/assets/img/icons/html.png"
                                                     class="img responsive img-skill"></th>
                        <th class="text-center"><img src="@/assets/img/icons/css.png"
                                                     class="img responsive img-skill"></th>
                        <th class="text-center"><img src="@/assets/img/icons/js.png"
                                                     class="img responsive img-skill"></th>
                        <th class="text-center"><img src="@/assets/img/icons/db.png"
                                                     class="img responsive img-skill"></th>
                        <th class="text-center"><img src="@/assets/img/icons/python.png"
                                                     class="img responsive img-skill"></th>
                      </tr>
                      </thead>
                      <tbody>
                      <tr>
                        <td class="text-center"><b>{{ getTeamRequirements().html }}</b></td>
                        <td class="text-center"><b>{{ getTeamRequirements().css }}</b></td>
                        <td class="text-center"><b>{{ getTeamRequirements().js }}</b></td>
                        <td class="text-center"><b>{{ getTeamRequirements().db }}</b></td>
                        <td class="text-center"><b>{{ getTeamRequirements().python }}</b></td>
                      </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row plain-element">
            <div class="col m12 plain-element">
              <div class="card insights-card">
                <div class="card-header">
                  Project Team
                    <button v-if="getUsername() == getProject().pm_email" @click="rejectCandidate()" class="btn-insights red">
                      Reject Candidate
                    </button>
                    <button v-if="getPosition() == 'Coder' && getProject().phase == 'proposed'" @click="joinTeam()"
                            class="btn-insights green">Join Team
                    </button>
                </div>
                <div class="row row-content">
                  <div class="col m6 plain-element">
                    <div class=" table table-team">
                      <table>
                        <tr>
                          <td class="td-position"><b>Manager:</b></td>
                          <td class="box plain-element">
                            <div class="plain-element">
                              <img :src="getProject().portrait" class="img responsive img-icon">
                              <p class="tooltip-hover">{{ getProject().pm_name }}</p>
                            </div>
                          </td>
                        </tr>
                        <tr>
                          <td class="td-position"><b>Html</b>:</td>

                          <td class="box">
                            <div v-for="element in getTeamMembership()" :key="element.id" class="plain-element">
                              <img v-if="element.committed_skill == 'html'" :src="element.member_portrait"
                                   class="img responsive img-icon">
                              <p class="tooltip-hover">{{element.member_name}}</p>
                            </div>
                          </td>
                        </tr>
                        <tr>
                          <td class="td-position"><b>Css</b>:</td>
                          <td class="box">
                            <div v-for="element in getTeamMembership()" :key="element.id" class="plain-element">
                              <img v-if="element.committed_skill == 'css'" :src="element.member_portrait"
                                   class="img responsive img-icon">
                              <p class="tooltip-hover">{{element.member_name}}</p>
                            </div>
                          </td>
                        </tr>
                        <tr>
                          <td class="td-position"><b>Js</b>:</td>
                          <td class="box">
                            <div v-for="element in getTeamMembership()" :key="element.id" class="plain-element">
                              <img v-if="element.committed_skill == 'js'" :src="element.member_portrait"
                                   class="img responsive img-icon">
                              <p class="tooltip-hover">{{element.member_name}}</p>
                            </div>
                          </td>
                        </tr>
                        <tr>
                          <td class="td-position"><b>Db</b>:</td>
                          <td class="box">
                            <div v-for="element in getTeamMembership()" :key="element.id" class="plain-element">
                              <img v-if="element.committed_skill == 'db'" :src="element.member_portrait"
                                   class="img responsive img-icon">
                              <p class="tooltip-hover">{{element.member_name}}</p>
                            </div>
                          </td>
                        </tr>
                        <tr>
                          <td class="td-position"><b>Python</b>:</td>
                          <td class="box">
                            <div v-for="element in getTeamMembership()" :key="element.id" class="plain-element">
                              <img v-if="element.committed_skill == 'python'" :src="element.member_portrait"
                                   class="img responsive img-icon">
                              <p class="tooltip-hover">{{element.member_name}}</p>
                            </div>
                          </td>
                        </tr>
                      </table>
                      <br>
                    </div>
                  </div>
                  <div class="col m6 plain-element">
                    <div class="row plain-element">
                  
                </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row plain-element">
            <div class="col m12 plain-element">
              <div class="card insights-card">
                <div class="card-header">
                  Team Insights
                </div>
                <div class="row row-content">
                  <div class=" table-responsive table-insights">
                    <table v-if="getTeamComposition()">
                      <tr>
                        <th class="text-left">Area</th>
                        <th class="text-left">Summary</th>
                      </tr>
                      <tr>
                        <td>Team Type</td>
                        <td>{{ getTeamComposition().team_type }}</td>
                      </tr>
                      <tr>
                        <td>Productivity</td>
                        <td>{{ getTeamComposition().statement_1 }}</td>
                      </tr>
                      <tr>
                        <td>Innovation</td>
                        <td>{{ getTeamComposition().statement_2 }}</td>
                      </tr>
                      <tr>
                        <td>Teamwork</td>
                        <td>{{ getTeamComposition().statement_3 }}</td>
                      </tr>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col m6 plain-element">
          <div class="row plain-element">
            <div class="col m12 plain-element">
              <div class="card insights-card">
                <div class="card-header">
                  Bugs & Issues
                    <button v-if="getUsername() == getProject().pm_email" @click="issueCreate()" class="btn-insights red">Report Issue
                    </button>
                </div>
                <div class="row row-content">
                  <div class="table-responsive table-insights">
                    <table>
                      <thead>
                      <tr>
                        <th class="text-left">Issue</th>
                        <th class="text-left">Description</th>
                        <th class="text-left">Reward</th>
                        <th class="text-left">Assigned to</th>
                      </tr>
                      </thead>
                      <tbody>
                      <tr v-for="element in getProject().project_issues" :key="element.id">
                        <td>{{element.name}}</td>
                        <td>{{element.description}}</td>
                        <td><img src="@/assets/img/leancoin.png" class="icon"> {{element.cost}}
                        </td>
                        <td id="assignCell" v-if="getProject().pm_email == element.assignee">
                          <button id="buttonAssign" @click="assignIssue(element.id)" class="btn-table green">Assign to Me
                          </button>
                        </td>
                        <td v-else>{{element.assignee}}</td>

                      </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row plain-element">
            <div class="col m12 plain-element">
              <div class="card insights-card">
                <div class="card-header">
                  Project Log
                  <button v-if="getPosition() == 'admin'" @click="terminateProject()" class="btn-insights red">Terminate
                    Project
                  </button>
                </div>
                <div class="row row-content">
                  <div class=" table-responsive table-insights">
                    <div class="table-div plain-element">
                      <table>
                        <tr>
                          <th class="text-left">Date</th>
                          <th class="text-left">Log Entry</th>
                        </tr>
                        <tr v-for="element in getProjectMessages()" :key="element.id">
                          <td>{{ formatDate (element.message_date) }}</td>
                          <td>{{element.message}}</td>
                        </tr>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { apiService } from "@/common/api.service.js";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "ProjectDetails",
  components: {
  },
  props: {
    id: {
      required: true
    }
  },
  data() {
    return {
      project: {},
      error: null,
    }
  },
  methods: {
    ...mapGetters(["getUsername", "getPosition", "getProject", "getTeamMembership",
                    "getTeamRequirements", "getTeamComposition", "getProjectMessages"]),
    ...mapActions(["fetchProjectDetails"]),
    
  //  Date converter
    formatDate(value) {
      let val = (value).replace('T', ' at ')
      return val.toString().slice(0, -8)
    },
    getProjectData() {
      this.fetchProjectDetails(this.id)

    },


    advanceProject(){
      this.$router.push({
        name: "project-advance",
        params: { id: this.id }
      })
    },
    defineTeamRequirements(){
      this.$router.push({
        name: "team-requirements",
        params: { id: this.id }
      })
    },
    terminateProject(){
      this.$router.push({
        name: "project-terminate",
        params: { id: this.id }
      })
    },
    completeProject(){
      this.$router.push({
        name: "project-complete",
        params: { id: this.id }
      })
    },
    joinTeam(){
      this.$router.push({
        name: "team-join",
        params: { id: this.id }
      })
    },
    rejectCandidate(){
      this.$router.push({
        name: "team-reject",
        params: { id: this.id }
      })
    },
    issueCreate(){
      this.$router.push({
        name: "issue-create",
        params: { id: this.id }
      })
    },
    assignIssue(issue_id){
    let endpoint = `/api/projects/issues/${issue_id}/issue-assign/`;
        let method = "PATCH";
        apiService(endpoint, method, {})
        .then(
          document.getElementById('buttonAssign').style.display = "none",
//          document.getElementById('assignCell').textContent = "this.requestUser"
        )
    }
  },
  mounted() {
  },
  computed: {
    chartStyles () {
      return {
        height: `100%`,
        position: "relative"
      }
    }
  },
  created() {
    this.getProjectData();
  }

}



</script>
