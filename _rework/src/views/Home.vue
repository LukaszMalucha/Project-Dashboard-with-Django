<template>
  <div class="row plain-element">

    <div class="row header details-header">
      <div class="col-md-2 text-right plain-element img-column">
          <img src="@/assets/img/main.png" class="img responsive img-header">
      </div>

      <div class="col-md-8 text-left">
          <div class="box">
            <h5>Kanban Board</h5>
            <router-link :to="{name: 'project-create'}" class="btn-algorithm blue">Start New Project</router-link>
          </div>
          <h6>Active Projects:  &nbsp; <b class="counter">{{countProjects }} </b></h6>
          <h6>Issues Counter:  &nbsp; <b class="counter">14 </b></h6>
      </div>
    </div>
    <div class="dashboard-cards">
      <div class="row row-cards">
          <div class="col-sm-8 col-md-4 col-lg-25 text-center">
              <div class="card card-status">
                  <i class="fas fa-lightbulb"></i> Proposed
              </div>
          </div>
          <div class="col-sm-8 col-md-4 col-lg-25 text-center">
              <div class="card card-status">
                  <i class="fas fa-chart-line"></i> Analysis
              </div>
          </div>
          <div class="col-sm-8 col-md-4 col-lg-25 text-center">
              <div class="card card-status">
                  <i class="fas fa-cog"></i> Development
              </div>
          </div>
          <div class="col-sm-8 col-md-4 col-lg-25 text-center">
              <div class="card card-status">
                  <i class="fas fa-code"></i> Testing
              </div>
          </div>
          <div class="col-sm-8 col-md-4 col-lg-25 text-center">
              <div class="card card-status">
                  <i class="fas fa-space-shuttle"></i> Deployment
              </div>
          </div>
      </div>
      <div class="row row-cards">
        <div class="col-sm-8 col-md-4 col-lg-25 text-center">
            <ProjectCardComponent
              v-for="project in projects"
              :project="project"
              :key="project.id"
            />
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
      countProjects: 0,
      requestUser: null,
      requestPosition: null,

    }
  },
  computed: {
  },
  methods: {
    setRequestUser() {
        this.requestUser = window.localStorage.getItem("email");
    },
    setRequestPosition() {
        this.requestPosition = window.localStorage.getItem("position");
    },
    getProjectsData() {
      let endpoint = "/api/projects/projects/";
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.projects.push(...data.results);
              this.countProjects = this.projects.length

          }}).then (
              window.console.log(this.projects)
            )

    }
  },
  created() {
    this.getProjectsData();
    this.setRequestUser();
    this.setRequestPosition();
    document.title = "Project Dashboard | Septellar";
  }
}
</script>
