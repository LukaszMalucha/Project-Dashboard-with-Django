<template>
  <div class="row plain-element">

    <div class="row header details-header">
      <div class="col m1 col l1 text-left plain-element img-column">
          <img src="@/assets/img/main.png" class="img responsive img-header">
      </div>

      <div class="col m8 text-left plain-element">
          <div class="box box-details">
            <h5>Kanban Board</h5>
            <router-link :to="{name: 'project-create'}" class="btn-algorithm blue">Start New Project</router-link>
          </div>
          <h6>Active Projects:  &nbsp; <b v-if="countProjects">{{ countProjects }} </b></h6>
          <h6>Issue Counter:  &nbsp; <b v-if="countIssues">{{ countIssues }}</b></h6>
      </div>
    </div>
    <div class="dashboard-cards">
      <div class="row row-cards">
          <div class="col s12 m2 l2 text-center">
              <div class="row plain-element">
                <div class="card card-status">
                    <i class="fas fa-lightbulb"></i> Proposed
                </div>
              </div>
              <div v-for="project in getProjectList()"  :key="project.id" class="row plain-element">
                  <ProjectCardComponent v-if="project.phase == 'proposed'" :project="project"/>
              </div>
          </div>
          <div class="col s12 m2 l2 text-center">
              <div class="row plain-element">
                <div class="card card-status">
                    <i class="fas fa-chart-line"></i> Analysis
                </div>
              </div>
              <div v-for="project in getProjectList()"  :key="project.id" class="row plain-element">
                  <ProjectCardComponent v-if="project.phase == 'analysis'" :project="project"/>
              </div>
          </div>
          <div class="col s12 m2 l2 text-center">
              <div class="row plain-element">
                <div class="card card-status">
                    <i class="fas fa-cog"></i> Development
                </div>
              </div>
              <div v-for="project in getProjectList()"  :key="project.id" class="row plain-element">
                  <ProjectCardComponent v-if="project.phase == 'development'" :project="project"/>
              </div>
          </div>
          <div class="col s12 m2 l2 text-center">
              <div class="row plain-element">
                <div class="card card-status">
                    <i class="fas fa-code"></i> Testing
                </div>
              </div>
              <div v-for="project in getProjectList()"  :key="project.id" class="row plain-element">
                  <ProjectCardComponent v-if="project.phase == 'testing'" :project="project"/>
              </div>
          </div>
          <div class="col s12 m2 l2 text-center">
              <div class="row plain-element">
                <div class="card card-status">
                    <i class="fas fa-space-shuttle"></i> Deployment
                </div>
              </div>
              <div v-for="project in getProjectList()"  :key="project.id" class="row plain-element">
                  <ProjectCardComponent v-if="project.phase == 'deployment'" :project="project"/>
              </div>
          </div>
          <div class="col s12 m2 l2 text-center">
           <div class="row plain-element">
              <div class="card card-status">
                    <i class="fas fa-stop-circle"></i> On Hold
              </div>
              </div>
              <div v-for="project in getProjectList()"  :key="project.id" class="row plain-element">
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
import { mapGetters, mapActions } from "vuex";

export default {
  name: 'Home',
  components: {
    ProjectCardComponent
  },
  data() {
    return {
      search: "",
      countIssues: null,
      countProjects: null,
    }
  },
  computed: {

  },
  mounted() {

  },
  methods: {
    ...mapGetters([ "getProjectList", "getPosition"]),
    ...mapActions(["fetchProjectList", ]),
    async getIssueCount() {
      let endpoint = "/api/projects/issue-count/";
      await apiService(endpoint)
        .then(data => {
          this.countIssues = data.issue_count
      })
    },
  },
  created() {
    this.fetchProjectList();
    this.getIssueCount();
    document.title = "Project Dashboard | Septellar";

  }
}
</script>
