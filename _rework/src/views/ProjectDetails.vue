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

            <a href="" class="btn-algorithm green">Finish
                Project!</a>
            <button @click="terminateProject()" class="btn-algorithm red">Terminate Project</button>
            <a href="" class="btn-algorithm red">Report Issue</a>
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
              <router-link :to="{name: 'project-create'}" class="btn-algorithm red">&nbsp;Reject
                &nbsp;
              </router-link>

              <router-link :to="{name: 'project-create'}" class="btn-algorithm green">&nbsp;&nbsp;
                Join &nbsp;&nbsp;
              </router-link>
            </p>
          </div>
          <div class="row-image">
            <div class=" table-responsive table-profile">
              <table>
                <tr>
                  <td><b>MANAGER:</b></td>
                  <td><img src="@/assets/img/team.png" class="img responsive img-icon"></td>

                </tr>
                <tr>
                  <td><b>HTML</b>:</td>
                  <td><img src="@/assets/img/team.png" class="img responsive img-icon"></td>

                </tr>
                <tr>
                  <td><b>CSS</b>:</td>
                  <td><img src="@/assets/img/team.png" class="img responsive img-icon"></td>
                </tr>
                <tr>
                  <td><b>JS</b>:</td>
                  <td><img src="@/assets/img/team.png" class="img responsive img-icon"></td>
                </tr>
                <tr>
                  <td><b>DB</b>:</td>
                  <td><img src="@/assets/img/team.png" class="img responsive img-icon"></td>
                </tr>
                <tr>
                  <td><b>PYTHON</b>:</td>
                  <td><img src="@/assets/img/team.png" class="img responsive img-icon"></td>
                </tr>
              </table>
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
                  <tr>
                    <td></td>
                    <td></td>
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
            <img src="" class="img-responsive">
          </div>
        </div>
      </div>
      <div class="col-md-3 plain-element">
        <div class="card insights-card">
          <div class="card-header">
            <img src="@/assets/img/icons/chart.png" class="img-responsive">
            <p><b>Team Personalities </b> <br></p>
          </div>
          <div class="row-image">
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
                  <td>asd</td>
                </tr>
                <tr>
                  <td>Innovation</td>
                  <td>zxc</td>
                </tr>
                <tr>
                  <td>Teamwork</td>
                  <td>xcgv</td>
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
              <tr>
                <td class="text-center"><a target="_blank">asd</a>
                <td class="text-center">zxc</td>
                <td class="text-center"><img src="@/assets/img/leancoin.png" class="icon"> 11
                </td>
                <td class="text-center"><a
                        href=""
                        class="btn-inline red">&nbsp; Assign to Me &nbsp;</a></td>
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

export default {
  name: "ProjectDetails",
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

    }
  },
  methods: {
    getProjectData() {
      let endpoint = `/projects/projects/${this.id}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.project = data;
            this.teamRequirements = data.team_requirements;
            document.title = this.project.name;
          } else {
            this.project = null;
            document.title = "404 - Page Not Found"
          }
        })
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

  },
  created() {
    this.getProjectData()
  }

}
</script>
