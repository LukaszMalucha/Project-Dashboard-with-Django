<template>
<div v-if="requestPosition == 'admin'" class="row plain-element">
  <div class="row header details-header">
      <div class="col-md-1 text-left plain-element img-column">
          <img src="@/assets/img/propose-project.jpg" class="img responsive img-header">
      </div>
      <div class="col-md-8 text-left plain-element">
          <div class="box">
              <h5>Advance Project</h5>
          </div>
      </div>
  </div>
  <div class="dashboard-cards">
      <div class="row row-form">
          <div class="col-md-4 plain-element">
              <div class="card form-card">
                  <div class="card-header">
                      <img src="@/assets/img/icons/gear.png" class="img-responsive">
                      <h5> Advance Project </h5>
                  </div>
                  <form @submit.prevent="onSubmit" class="form-content form-wide">
                      <fieldset class="form-box">
                          <div id="formError" class="row row-error text-center">
                          {{ error }}
                          </div>
                          <div class="row plain-element">
                          <ul>
                            <li v-for="element in phaseList" :key="element">
                              <label>
                                <input v-model="phase" name="phase" :value="element" type="radio"/>
                                <span>{{element}}</span>
                              </label>
                            </li>
                          </ul>
                          </div>
                          <div class="row"></div>
                          <button type="submit" class="btn-proceed"><span>Advance Project <i
                                  class="far fa-arrow-alt-circle-right"></i></span>
                          </button>
                      </fieldset>
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
import { apiService } from "@/common/api.service.js";
import NoPermissionComponent from "@/components/NoPermissionComponent.vue"

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
      requestPosition: null,
      phaseList: ["proposed", "analysis", "development", "testing", "deployment"],
    }
  },
  methods: {
    setRequestPosition() {
        this.requestPosition = window.localStorage.getItem("position");
    },
    onSubmit() {
      let endpoint = `/api/projects/${this.id}/project-phase/`;
      let method = "PATCH";
      apiService(endpoint, method, {phase: this.phase})
      .then(data => {
           if (data.non_field_errors) {
              this.error = data.non_field_errors[0]
           } else if (!data) {
              this.error = "Something went wrong. Try again later"
          } else {
            this.$router.push({
                  name: "project-details",
                  params: { id: this.id }
            })
          }
      })

    }
  },
  mounted() {

  },
  created() {
    this.setRequestPosition();
    document.title = "Advance Project";
  }
}
</script>
