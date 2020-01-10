import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Charity from "./views/Charity.vue";
import CharityCreate from "./views/CharityCreate.vue";
import CharityDonation from "./views/CharityDonation.vue";
import CharityDonationList from "./views/CharityDonationList.vue";

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
      path: "/charity-donation",
      name: "charity-donation",
      component: CharityDonation
    },
    {
      path: "/charity-donation-list",
      name: "charity-donation-list",
      component: CharityDonationList
    },
  ]
})

