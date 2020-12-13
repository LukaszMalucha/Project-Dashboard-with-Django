<template>
<div v-if="getPosition() == 'admin'" class="row plain-element">
  <div class="row header details-header">
      <div class="col m1 text-left plain-element img-column">
          <img src="@/assets/img/propose-project.jpg" class="img responsive img-header">
      </div>
      <div class="col m9 l6 text-left plain-element">
          <div class="box box-details">
              <h5>Terminate Project </h5>
          </div>
      </div>
  </div>
  <div class="dashboard-cards">
    <div class="row row-form">
        <div class="col s8 m6 l3 plain-element">
            <div class="card form-card">
                <div class="card-header">
                    <img src="@/assets/img/icons/bin.png" class="img-responsive">
                    <h5> Terminate Project </h5>
                </div>
                 <form @submit.prevent="deleteProject" class="form-content form-wide" enctype="multipart/form-data">
                      <fieldset class="form-box">
                          <div id="formError" class="row row-error text-center">
                          {{ error }}
                          </div>
                          <div class="row"></div>

                      </fieldset>
                      <button type="submit" class="btn-proceed red"><span>Terminate Project <i
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
import NoPermissionComponent from "@/components/NoPermissionComponent.vue"
import { mapGetters, mapActions } from "vuex";

export default {
  name: "ProjectTerminate",
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
    ...mapActions(["performDeleteProject"]),

    deleteProject() {
      this.performDeleteProject(this.id)
    }
  },
  created() {
    document.title = "Terminate Project";
  }
}
</script>
