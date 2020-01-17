import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Charity from "./views/Charity.vue";
import CharityCreate from "./views/CharityCreate.vue";
import CharityDonate from "./views/CharityDonate.vue";
import CharityDonations from "./views/CharityDonations.vue";
import ProjectCreate from "./views/ProjectCreate.vue";
import ProjectDetails from "./views/ProjectDetails.vue";
import ProjectTeamRequirements from "./views/ProjectTeamRequirements.vue";
import ProjectAdvance from "./views/ProjectAdvance.vue";
import ProjectTerminate from "./views/ProjectTerminate.vue";
import TeamJoin from "./views/TeamJoin.vue";
import TeamReject from "./views/TeamReject.vue";

import NotFound from "./views/NotFound.vue";

Vue.use(Router)

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/charity",
      name: "charity",
      component: Charity
    },
    {
      path: "/charity-create",
      name: "charity-create",
      component: CharityCreate
    },
    {
      path: "/charity-donate",
      name: "charity-donate",
      component: CharityDonate,
      props: true
    },
    {
      path: "/charity-donations",
      name: "charity-donations",
      component: CharityDonations,
      props: true
    },
    {
      path: "/project-create",
      name: "project-create",
      component: ProjectCreate
    },
    {
      path: "/projects/:id",
      name: "project-details",
      component: ProjectDetails,
      props: true
    },
    {
      path: "/projects-advance/:id",
      name: "project-advance",
      component: ProjectAdvance,
      props: true
    },
    {
      path: "/projects-terminate/:id",
      name: "project-terminate",
      component: ProjectTerminate,
      props: true
    },
    {
      path: "/team-requirements/:id",
      name: "team-requirements",
      component: ProjectTeamRequirements,
      props: true
    },
    {
      path: "/team-join/:id",
      name: "team-join",
      component: TeamJoin,
      props: true
    },
    {
      path: "/team-reject/:id",
      name: "team-reject",
      component: TeamReject,
      props: true
    },
    {
      path: "*",
      name: "page-not-found",
      component: NotFound,
    },
  ]
})

