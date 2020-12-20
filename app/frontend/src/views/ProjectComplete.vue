<template>
<div v-if="getPosition() == 'admin'" class="row plain-element">
  <div class="row header details-header">
      <div class="col m1 text-left plain-element img-column">
          <img src="https://project-gamification.s3-eu-west-1.amazonaws.com/static/img/propose-project.jpg" class="img responsive img-header">
      </div>
      <div class="col m9 l6 text-left plain-element">
          <div class="box box-details">
              <h5>Finish Project </h5>
          </div>
      </div>
  </div>
  <div class="dashboard-cards">
    <div class="row row-form">
        <div class="col s8 m6 l4 plain-element">
            <div class="card form-card">
                <div class="card-header">
                    <img src="https://project-gamification.s3-eu-west-1.amazonaws.com/static/img/icons/gear.png" class="img-responsive">
                    <p><b> Finish Project </b></p>
                </div>
                 <form @submit.prevent="completeProject" class="form-content form-wide" enctype="multipart/form-data">
                      <fieldset class="form-box">
                          <div id="formError" class="row row-error text-center">
                          {{ error }}
                          </div>
                          <div class="row"></div>

                      </fieldset>
                      <button type="submit" class="btn-proceed green"><span>Finish Project <i
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
  name: "ProjectComplete",
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
        error: "",
    }
  },
  methods: {
    ...mapGetters(["getPosition"]),
    ...mapActions(["performCompleteProject"]),
    completeProject() {
      this.performCompleteProject(this.id)
    }

  },
  created() {
    document.title = "Finish Project";
  }
}
</script>
