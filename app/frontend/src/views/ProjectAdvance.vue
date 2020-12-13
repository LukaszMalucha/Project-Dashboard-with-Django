<template>
<div v-if="getPosition() == 'admin'" class="row plain-element">
  <div class="row header details-header">
      <div class="col m1 text-left plain-element img-column">
          <img src="@/assets/img/propose-project.jpg" class="img responsive img-header">
      </div>
      <div class="col m9 l6 text-left plain-element">
          <div class="box box-details">
              <h5>Advance Project</h5>
          </div>
      </div>
  </div>
  <div class="dashboard-cards">
      <div class="row row-form">
          <div class="col s8 m6 l3 plain-element">
              <div class="card form-card">
                  <div class="card-header">
                      <img src="@/assets/img/icons/gear.png" class="img-responsive">
                      <h5> Advance Project </h5>
                  </div>
                  <form @submit.prevent="advanceProject" class="form-content form-wide">
                      <fieldset class="form-box">
                          <div id="formError" class="row row-error text-center">
                          {{ error }}
                          </div>
                          <div class="row plain-element">
                          <ul>
                            <div  v-for="element in phaseList" :key="element" class="row">
                              <li>
                                <label>
                                  <input v-model="phase" name="phase" :value="element" type="radio"/>
                                  <span class="span-radio">{{element}}</span>
                                </label>
                              </li>
                              </div>
                          </ul>
                          </div>
                          <div class="row"></div>

                      </fieldset>
                      <button type="submit" class="btn-proceed"><span>Advance Project
                        <i class="far fa-arrow-alt-circle-right"></i></span>
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

import NoPermissionComponent from "@/components/NoPermissionComponent.vue"
import { mapGetters, mapActions } from "vuex";

export default {
  name: "ProjectAdvance",
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
      phase: null,
      phaseList: ["proposed", "analysis", "development", "testing", "deployment"],
    }
  },
  methods: {
    ...mapGetters(["getPosition"]),
    ...mapActions(["performAdvanceProject"]),
    advanceProject() {
      this.performAdvanceProject({"project": this.id, "phase": this.phase})
    }



  },
  created() {
    document.title = "Advance Project";
  }
}
</script>
