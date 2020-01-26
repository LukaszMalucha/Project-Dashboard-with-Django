<template>
  <div class="row plain-element">

    <div class="row header details-header">
      <div class="col-md-1 col-lg-1 text-left plain-element img-column">
          <img src="https://project-gamification.s3-eu-west-1.amazonaws.com/static/img/main.png" class="img responsive img-header">
      </div>

      <div class="col-md-8 text-left plain-element">
          <div class="box box-details">
            <h5>Kanban Board</h5>
            <router-link :to="{name: 'project-create'}" class="btn-algorithm blue">Start New Project</router-link>
          </div>
          <h6>Active Projects:  &nbsp; <b v-if="countProjects">{{ countProjects }} </b></h6>
          <h6>Issues Counter:  &nbsp; <b v-if="countIssues">{{ countIssues }}</b></h6>
      </div>
    </div>
    <div class="dashboard-cards">
      <div class="row row-cards">
          <div class="col-sm-12 col-md-2 col-lg-2 text-center">
              <div class="row plain-element">
                <div class="card card-status">
                    <i class="fas fa-lightbulb"></i> Proposed
                </div>
              </div>
              <div v-for="project in projects"  :key="project.id" class="row plain-element">
                  <ProjectCardComponent v-if="project.phase == 'proposed'" :project="project"/>
              </div>
          </div>
          <div class="col-sm-12 col-md-2 col-lg-2 text-center">
              <div class="row plain-element">
                <div class="card card-status">
                    <i class="fas fa-chart-line"></i> Analysis
                </div>
              </div>
              <div v-for="project in projects"  :key="project.id" class="row plain-element">
                  <ProjectCardComponent v-if="project.phase == 'analysis'" :project="project"/>
              </div>
          </div>
          <div class="col-sm-12 col-md-2 col-lg-2 text-center">
              <div class="row plain-element">
                <div class="card card-status">
                    <i class="fas fa-cog"></i> Development
                </div>
              </div>
              <div v-for="project in projects"  :key="project.id" class="row plain-element">
                  <ProjectCardComponent v-if="project.phase == 'development'" :project="project"/>
              </div>
          </div>
          <div class="col-sm-12 col-md-2 col-lg-2 text-center">
              <div class="row plain-element">
                <div class="card card-status">
                    <i class="fas fa-code"></i> Testing
                </div>
              </div>
              <div v-for="project in projects"  :key="project.id" class="row plain-element">
                  <ProjectCardComponent v-if="project.phase == 'testing'" :project="project"/>
              </div>
          </div>
          <div class="col-sm-12 col-md-2 col-lg-2 text-center">
              <div class="row plain-element">
                <div class="card card-status">
                    <i class="fas fa-space-shuttle"></i> Deployment
                </div>
              </div>
              <div v-for="project in projects"  :key="project.id" class="row plain-element">
                  <ProjectCardComponent v-if="project.phase == 'deployment'" :project="project"/>
              </div>
          </div>
          <div class="col-sm-12 col-md-2 col-lg-2 text-center">
           <div class="row plain-element">
              <div class="card card-status">
                    <i class="fas fa-stop-circle"></i> On Hold
              </div>
              </div>
              <div v-for="project in projects"  :key="project.id" class="row plain-element">
                  <ProjectCardComponent v-if="project.phase == 'on hold'" :project="project"/>
              </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import ProjectCardComponent from "@/components/ProjectCardComponent.vue"

export default {
  name: 'Home',
  components: {
    ProjectCardComponent
  },
  data() {
    return {
      search: "",
      projects: [],
      countIssues: null,
      countProjects: null,
      requestUser: null,
      requestPosition: null,

    }
  },
  computed: {

  },
  mounted() {

  },
  methods: {
    setRequestUser() {
        this.requestUser = window.localStorage.getItem("email");
    },
    setRequestPosition() {
        this.requestPosition = window.localStorage.getItem("position");
    },
    async getProjectsData() {
      let endpoint = "/api/projects/projects/";
      await apiService(endpoint)
        .then(data => {
          if (data) {
            this.projects.push(...data.results);
              this.countProjects = this.projects.length
          }}).then (
              window.console.log(this.projects)
            )
    },
    async getIssueCount() {
      let endpoint = "/api/projects/issue-count/";
      await apiService(endpoint)
        .then(data => {
          this.countIssues = data.issue_count
      })
    },
  },
  created() {
    this.getProjectsData()
    this.getIssueCount();
    this.setRequestUser();
    this.setRequestPosition();
    document.title = "Project Dashboard | Septellar";

  }
}
</script>
