<template>
<div class="row plain-element">
  <div class="row header details-header">
    <div class="col-md-2 text-right plain-element img-column">
        <img src="@/assets/img/project-details.jpg" class="img responsive img-header">
    </div>
    <div class="col-md-10 text-left">
        <div class="box" v-if="project">
            <h5>{{ project.name }}</h5>
            <button @click="advanceProject()" class="btn-algorithm green">
                <b v-if="project.phase == 'proposed'">Launch Project</b>
                <b v-else>Advance Project</b>
            </button>
            <button @click="completeProject()" class="btn-algorithm green">Finish Project!</button>
            <button @click="terminateProject()" class="btn-algorithm red">Terminate Project</button>
            <button @click="issueCreate()" class="btn-algorithm red">Report Issue</button>
            <button @click="defineTeamRequirements()" class="btn-algorithm blue">Define Team Requirements</button>
        </div>
        <br>
        <table class="profile-details">
            <tr class>
                <td>Manager: &nbsp;</td>
                <td><b> &nbsp; {{ project.pm_name }}</b></td>
            </tr>
            <tr>
                <td>Budget: &nbsp;</td>
                <td><b><img src="@/assets/img/leancoin.png" class="icon"> {{ project.budget }}</b></td>
            </tr>
            <tr>
                <td>Phase:</td>
                <td><b>{{ project.phase }}</b></td>
            </tr>
        </table>


    </div>
  </div>
  <div class="dashboard-cards">
    <div class="row row-cards">
      <div class="col-md-3 plain-element">
        <div class="card insights-card">
          <div class="card-header">
            <img src="@/assets/img/team.png" class="img-responsive">
            <p><b> Project Team</b></p>
            <p>
              <button @click="rejectCandidate()" class="btn-insights red">Reject Candidate</button>
              <button @click="joinTeam()" class="btn-insights green">Join Team</button>

            </p>
          </div>
          <div class="row-image">
            <div class=" table-responsive table-profile">
              <table>
                <tr>
                  <td><b>MANAGER:</b></td>
                  <td class="box">
                  <div class="plain-element">
                    <img :src="pmPortrait" class="img responsive img-icon">
                    <p class="tooltip-hover">{{ project.pm_name }}</p>
                  </div>
                  </td>
                </tr>
                <tr>
                  <td><b>HTML</b>:</td>

                  <td class="box">
                    <div v-for="element in teamMembership" :key="element.id" class="plain-element">
                      <img v-if="element.committed_skill == 'html'" :src="element.member_portrait" class="img responsive img-icon">
                      <p class="tooltip-hover">{{element.member_name}}</p>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td><b>CSS</b>:</td>
                  <td class="box">
                    <div v-for="element in teamMembership" :key="element.id" class="plain-element">
                      <img v-if="element.committed_skill == 'css'" :src="element.member_portrait" class="img responsive img-icon">
                      <p class="tooltip-hover">{{element.member_name}}</p>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td><b>JS</b>:</td>
                  <td class="box">
                    <div v-for="element in teamMembership" :key="element.id" class="plain-element">
                      <img v-if="element.committed_skill == 'js'" :src="element.member_portrait" class="img responsive img-icon">
                      <p class="tooltip-hover">{{element.member_name}}</p>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td><b>DB</b>:</td>
                  <td class="box">
                    <div v-for="element in teamMembership" :key="element.id" class="plain-element">
                      <img v-if="element.committed_skill == 'db'" :src="element.member_portrait" class="img responsive img-icon">
                      <p class="tooltip-hover">{{element.member_name}}</p>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td><b>PYTHON</b>:</td>
                  <td class="box">
                    <div v-for="element in teamMembership" :key="element.id" class="plain-element">
                      <img v-if="element.committed_skill == 'python'" :src="element.member_portrait" class="img responsive img-icon">
                      <p class="tooltip-hover">{{element.member_name}}</p>
                    </div>
                  </td>
                </tr>
              </table>
              <br>
            </div>
          </div>
        </div>
        <div class="card insights-card">
          <div class="card-header">
            <img src="@/assets/img/icons/description.png" class="img-responsive">
            <p><b> Project Log </b></p>
          </div>
          <div class="row-image">
            <div class=" table-responsive table-log">
              <div class="table-div plain-element">
                <table>
                  <tr>
                    <th class="text-center">Date</th>
                    <th class="text-center">Log Entry</th>
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
      <div class="col-md-6 plain-element">
        <div class="card insights-card">
          <div class="card-header">
            <img src="@/assets/img/team.png" class="img-responsive">
            <p><b>Team Requirements </b> <br></p>
          </div>
          <div class="row-image">
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
                  <td class="text-center"><h5><b>{{ teamRequirements.html }}</b></h5></td>
                  <td class="text-center"><h5><b>{{ teamRequirements.css }}</b></h5></td>
                  <td class="text-center"><h5><b>{{ teamRequirements.js }}</b></h5></td>
                  <td class="text-center"><h5><b>{{ teamRequirements.db }}</b></h5></td>
                  <td class="text-center"><h5><b>{{ teamRequirements.python }}</b></h5></td>
                </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div class="card insights-card">
          <div class="card-header">
            <img src="@/assets/img/icons/gear.png" class="img-responsive">
            <p><b>Project Schedule </b> <br></p>
          </div>
          <div class="row-image">
            <img :src="projectSchedule" class="img-responsive">
          </div>
        </div>
      </div>
      <div class="col-md-3 plain-element">
        <div class="card insights-card">
          <div class="card-header">
            <img src="@/assets/img/icons/chart.png" class="img-responsive">
            <p><b>Team - Robot Factory</b></p>
          </div>
          <div class="row-image">
              <team-chart  :chart-data="teamCompositionData" :styles="chartStyles"></team-chart>
          </div>
          <br>
        </div>
        <div class="card insights-card">

          <div class="card-header">
            <img src="@/assets/img/icons/chart.png" class="img-responsive">
            <p><b>Team Insights </b> <br></p>
          </div>
          <div class="row-image">
            <div class=" table-responsive table-log">
              <table>
                <tr>
                  <th class="text-center">Area</th>
                  <th class="text-center">Insight</th>
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
    <div class="row row-cards">
      <div class="card insights-card">
        <div class="card-header">
          <img src="@/assets/img/issue.png" class="img-responsive">
          <p><b>Bugs & Issues </b> <br></p>
        </div>
        <div class="row-image">
          <div class="table-responsive table-profile">
            <table class="table">
              <thead>
              <tr>
                <th class="text-center">Issue</th>
                <th class="text-center">Description</th>
                <th class="text-center">Reward</th>
                <th class="text-center">Assigned to</th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="element in projectIssues" :key="element.id">
                <td class="text-center"><a target="_blank">{{element.name}}</a>
                <td class="text-center">{{element.description}}</td>
                <td class="text-center"><img src="@/assets/img/leancoin.png" class="icon"> {{element.cost}}
                </td>
                <td id="assignCell" class="text-center" v-if="project.pm_email == element.assignee">
                 <button id="buttonAssign" @click="assignIssue(element.id)" class="btn-inline red">Assign to Me</button>
                </td>
                <td class="text-center" v-else>{{element.assignee}}</td>
                <td class="text-center"></td>
              </tr>
              </tbody>
            </table>
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
            window.console.log(this.teamProfiles)
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
    this.setRequestUser()
    this.getProjectData()

  }

}
</script>
