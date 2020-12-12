import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";

import Charity from "./views/Charity.vue";
import CharityCreate from "./views/CharityCreate.vue";
import CharityDonate from "./views/CharityDonate.vue";
import CharityDonations from "./views/CharityDonations.vue";

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
      path: "*",
      name: "page-not-found",
      component: NotFound,
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
  ]
})

