<template>
  <div class="row plain-element">

    <div class="row header details-header">
      <div class="col m1 col l1 text-left plain-element img-column">
          <img src="https://project-gamification.s3-eu-west-1.amazonaws.com/static/img/main.png" class="img responsive img-header">
      </div>

      <div class="col m8 text-left plain-element">
          <div class="box box-details">
            <h5>Kanban Board <span v-if="!getUsername()" style="color: green">(Create fake profile and log in For Full Experience)   </span></h5>
            <router-link v-if="getPosition()"  :to="{name: 'project-create'}" class="btn-algorithm blue">Start New Project</router-link>
          </div>
          <h6>Project Count:
            <b v-if="getProjectList()" style="margin-left: 7.5px">
            <i-count-up
                    :start="0"
                    :endVal="getProjectList().length"
                    :duration="2"
                    :callback="callback"
            ></i-count-up>
            </b>
          </h6>
          <h6>Issue Counter:
            <b v-if="getIssueCount()">
            <i-count-up
                    :start="0"
                    :endVal="getIssueCount()"
                    :duration="2"
                    :callback="callback"
            ></i-count-up>
            </b>
          </h6>
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
import ProjectCardComponent from "@/components/ProjectCardComponent.vue"
import { mapGetters, mapActions } from "vuex";
import ICountUp from 'vue-countup-v2';

export default {
  name: 'Home',
  components: {
    ProjectCardComponent,
    ICountUp,
  },
  data() {
    return {
    }
  },
  computed: {

  },
  mounted() {

  },
  methods: {
    ...mapGetters([ "getUsername", "getProjectList", "getPosition", "getIssueCount"]),
    ...mapActions(["fetchProjectList", "performIssueCount"]),
    callback: function (ins) {
        ins.update(ins.endVal + 100)
    },

  },
  created() {
    this.fetchProjectList();
    this.performIssueCount();
    document.title = "Project Dashboard | Septellar";
    window.console.log(this.getPosition())
  },
}
</script>
