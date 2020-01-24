<template>
  <div class="row plain-element">
    <div class="row header details-header">
      <div class="col-md-1 text-left plain-element img-column">
        <img src="@/assets/img/project-details.jpg" class="img responsive img-header">
      </div>
      <div class="col-md-10 text-left plain-element">
        <div class="box" v-if="project">
          <h5>{{ project.name }}</h5>
          <button v-if="requestPosition == 'admin'" @click="advanceProject()" class="btn-algorithm green">
            <b v-if="project.phase == 'proposed'">Launch Project</b>
            <b v-else>Advance Project</b>
          </button>
          <button v-if="requestPosition == 'admin'" @click="completeProject()" class="btn-algorithm green">Finish
            Project!
          </button>
        </div>
        <br>
        <table class="profile-details">
          <tr class>
            <td>Manager: &nbsp;</td>
            <td class="td-position"><b> &nbsp; {{ project.pm_name }}</b></td>
          </tr>
          <tr>
            <td>Budget: &nbsp;</td>
            <td class="td-position"><b><img src="@/assets/img/leancoin.png" class="icon"> {{ project.budget }}</b></td>
          </tr>
          <tr>
            <td>Phase:</td>
            <td class="td-position"><b>{{ project.phase }}</b></td>
          </tr>
        </table>


      </div>
    </div>
    <div class="dashboard-cards">
      <div class="row row-details">
        <div class="col-md-6 col-left plain-element">

          <div class="row plain-element">
            <div class="col-md-12 plain-element">
              <div class="card insights-card">
                <div class="card-header">
                  Project Team Requirements
                  <button v-if="requestUser == project.pm_email" @click="defineTeamRequirements()" class="btn-insights green">
                    Define Team Requirements
                  </button>
                </div>
                <div class="row row-content">
                  <div class="table-responsive table-skills">
                    <table>
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
                        <td class="text-center"><b>{{ teamRequirements.html }}</b></td>
                        <td class="text-center"><b>{{ teamRequirements.css }}</b></td>
                        <td class="text-center"><b>{{ teamRequirements.js }}</b></td>
                        <td class="text-center"><b>{{ teamRequirements.db }}</b></td>
                        <td class="text-center"><b>{{ teamRequirements.python }}</b></td>
                      </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row plain-element">
            <div class="col-md-12 plain-element">
              <div class="card insights-card">
                <div class="card-header">
                  Project Team
                    <button v-if="requestUser == project.pm_email" @click="rejectCandidate()" class="btn-insights red">
                      Reject Candidate
                    </button>
                    <button v-if="requestPosition == 'Coder' && project.phase == 'proposed'" @click="joinTeam()"
                            class="btn-insights green">Join Team
                    </button>
                </div>
                <div class="row row-content">
                  <div class="col-md-6 plain-element">
                    <div class=" table table-team">
                      <table>
                        <tr>
                          <td class="td-position"><b>Manager:</b></td>
                          <td class="box plain-element">
                            <div class="plain-element">
                              <img :src="pmPortrait" class="img responsive img-icon">
                              <p class="tooltip-hover">{{ project.pm_name }}</p>
                            </div>
                          </td>
                        </tr>
                        <tr>
                          <td class="td-position"><b>Html</b>:</td>

                          <td class="box">
                            <div v-for="element in teamMembership" :key="element.id" class="plain-element">
                              <img v-if="element.committed_skill == 'html'" :src="element.member_portrait"
                                   class="img responsive img-icon">
                              <p class="tooltip-hover">{{element.member_name}}</p>
                            </div>
                          </td>
                        </tr>
                        <tr>
                          <td class="td-position"><b>Css</b>:</td>
                          <td class="box">
                            <div v-for="element in teamMembership" :key="element.id" class="plain-element">
                              <img v-if="element.committed_skill == 'css'" :src="element.member_portrait"
                                   class="img responsive img-icon">
                              <p class="tooltip-hover">{{element.member_name}}</p>
                            </div>
                          </td>
                        </tr>
                        <tr>
                          <td class="td-position"><b>Js</b>:</td>
                          <td class="box">
                            <div v-for="element in teamMembership" :key="element.id" class="plain-element">
                              <img v-if="element.committed_skill == 'js'" :src="element.member_portrait"
                                   class="img responsive img-icon">
                              <p class="tooltip-hover">{{element.member_name}}</p>
                            </div>
                          </td>
                        </tr>
                        <tr>
                          <td class="td-position"><b>Db</b>:</td>
                          <td class="box">
                            <div v-for="element in teamMembership" :key="element.id" class="plain-element">
                              <img v-if="element.committed_skill == 'db'" :src="element.member_portrait"
                                   class="img responsive img-icon">
                              <p class="tooltip-hover">{{element.member_name}}</p>
                            </div>
                          </td>
                        </tr>
                        <tr>
                          <td class="td-position"><b>Python</b>:</td>
                          <td class="box">
                            <div v-for="element in teamMembership" :key="element.id" class="plain-element">
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
                  <div class="col-md-6 plain-element">
                    <div class="row plain-element">
                  <team-chart :chart-data="teamCompositionData" :styles="chartStyles"></team-chart>
                </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row plain-element">
            <div class="col-md-12 plain-element">
              <div class="card insights-card">
                <div class="card-header">
                  <p><b>Team Insights </b> <br></p>
                </div>
                <div class="row row-content">
                  <div class=" table-responsive table-insights">
                    <table>
                      <tr>
                        <th class="text-left">Area</th>
                        <th class="text-left">Summary</th>
                      </tr>
                      <tr>
                        <td>Team Type</td>
                        <td>{{ projectAdvices.team_type }}</td>
                      </tr>
                      <tr>
                        <td>Productivity</td>
                        <td>{{ projectAdvices.statement_1 }}</td>
                      </tr>
                      <tr>
                        <td>Innovation</td>
                        <td>{{ projectAdvices.statement_2 }}</td>
                      </tr>
                      <tr>
                        <td>Teamwork</td>
                        <td>{{ projectAdvices.statement_3 }}</td>
                      </tr>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-6 plain-element">
          <div class="row plain-element">
            <div class="col-md-12 plain-element">
              <div class="card insights-card">
                <div class="card-header">
                  <p>Bugs & Issues</p>
                    <button v-if="requestUser == project.pm_email" @click="issueCreate()" class="btn-insights red">Report Issue
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
                      <tr v-for="element in projectIssues" :key="element.id">
                        <td><a target="_blank">{{element.name}}</a>
                        <td>{{element.description}}</td>
                        <td><img src="@/assets/img/leancoin.png" class="icon"> {{element.cost}}
                        </td>
                        <td id="assignCell" v-if="project.pm_email == element.assignee">
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
            <div class="col-md-12 plain-element">
              <div class="card insights-card">
                <div class="card-header">
                  <p>Project Log</p>
                  <button v-if="requestPosition == 'admin'" @click="terminateProject()" class="btn-insights red">Terminate
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
                        <tr v-for="element in projectMessages" :key="element.id">
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
import TeamChart from "@/common/TeamChart.js";

export default {
  name: "ProjectDetails",
  components: {
    TeamChart
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
      requestUser: null,
      requestPosition: null,
      teamRequirements: {},
      teamMembership: [],
      projectMessages: [],
      projectIssues: [],
      projectAdvices: [],
      teamCompositionData: {},
      pmPortrait: "",
      projectSchedule: "",
    }
  },
  methods: {
    setRequestUser() {
        this.requestUser = window.localStorage.getItem("email");
    },
    setRequestPosition() {
        this.requestPosition = window.localStorage.getItem("position");
    },
  //  Date converter
    formatDate(value) {
      let val = (value).replace('T', ' at ')
      return val.toString().slice(0, -8)
    },
    getProjectData() {
      let endpoint = `/api/projects/projects/${this.id}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.project = data;
            this.teamRequirements = data.team_requirements;
            this.teamMembership = data.team_membership;
            this.projectMessages = data.project_messages;
            this.pmPortrait = data.portrait;
            this.projectSchedule = data.image_schedule;
            this.projectIssues = data.project_issues;
            this.projectAdvices = data.project_team_composition;
            this.teamProfiles = this.projectAdvices.team_profiles;
            this.fillTeamChart();
            document.title = this.project.name;
          } else {
            this.project = null;
            document.title = "404 - Page Not Found"
          }
        })
    },
    fillTeamChart(){
        var dataset = this.teamProfiles;
        var dataLabels = Object.keys(dataset);
        var dataValues = Object.values(dataset);
        this.teamCompositionData = {
        labels: dataLabels,
        datasets: [
          {
            backgroundColor: ["#2b5b89","#f28e2b", "#e15759", "#76b7b2"],
            data: dataValues
          }
        ]
      }
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
          document.getElementById('assignCell').textContent = this.requestUser,
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
    this.setRequestUser();
    this.setRequestPosition();
    this.getProjectData();

  }

}



</script>
