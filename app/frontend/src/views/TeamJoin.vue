<template>
<div v-if="getPosition() == 'Coder'" class="row plain-element">
    <div class="row header details-header">
      <div class="col m1 text-left plain-element img-column">
          <img src="@/assets/img/propose-project.jpg" class="img responsive img-header">
      </div>
      <div class="col m9 l6 text-left plain-element">
          <div class="box box-details">
              <h5>Join Team</h5>
          </div>
          <p>
            Project team requirements is a skillset that must be completed to ensure the success of the project.
            They provide a clear picture of the work that needs to be done. The benefits of effectively gathering project
            team include cost reduction, higher project success rates, more effective change management,
            and improved communication.
          </p>
      </div>
  </div>
  <div class="dashboard-cards">
      <div class="row row-form">
          <div class="col s8 m6 l5">
              <div class="card form-card">
                  <div class="card-header">
                      <img src="@/assets/img/icons/gear.png" class="img-responsive">
                      <h5> Join Team </h5>
                  </div>
                  <form @submit.prevent="teamJoin" class="form-content form-wide">
                      <fieldset class="form-box">
                          <div id="formError" class="row row-error text-center">
                          {{ error }}
                          </div>
                          <div class="row plain-element">
                          <ul>
                            <li v-for="element in skillList" :key="element">
                              <div class="row">
                                <label>
                                  <input v-model="skill" name="skill" :value="element" type="radio"/>
                                  <span class="span-radio">{{element}}</span>
                                </label>
                              </div>
                            </li>
                          </ul>
                          </div>
                          <div class="row"></div>
                      </fieldset>
                      <button type="submit" class="btn-proceed"><span>Join Team <i
                                  class="far fa-arrow-alt-circle-right"></i></span>
                          </button>
                  </form>
              </div>
          </div>
      </div>
  </div>
</div>
<div v-else class="row plain-element">
    <NoPermissionComponent/>
</div>
</template>


<script>
import { mapGetters, mapActions } from "vuex";
import NoPermissionComponent from "@/components/NoPermissionComponent.vue"

export default {
  name: "TeamJoin",
  components: {
    NoPermissionComponent
  },
  props: {
    id: {
      required: true,
    }
  },
  data() {
    return {
      error: null,
      skill: null,
      skillList: ['html', 'css', 'js', 'db', 'python']
    }
  },
  methods: {
    ...mapGetters(["getPosition", "getUsername"]),
    ...mapActions(["performTeamJoin"]),
    teamJoin() {
      this.performTeamJoin({"project" : this.id, "member" : this.getUsername(), "committed_skill" : this.skill})
    }
  },
  created() {
    document.title = "Join Project Team";
  }
}
</script>
