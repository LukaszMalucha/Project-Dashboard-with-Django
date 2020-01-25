<template>
<div v-if="requestPosition == 'admin'" class="row plain-element">
  <div class="row header details-header">
      <div class="col-md-1 text-left plain-element img-column">
          <img src="@/assets/img/propose-project.jpg" class="img responsive img-header">
      </div>
      <div class="col-md-9 col-lg-6 text-left plain-element">
          <div class="box box-details">
              <h5>Terminate Project </h5>
          </div>
      </div>
  </div>
  <div class="dashboard-cards">
    <div class="row row-form">
        <div class="col-sm-8 col-md-6 col-lg-5 plain-element">
            <div class="card form-card">
                <div class="card-header">
                    <img src="@/assets/img/icons/bin.png" class="img-responsive">
                    <p><b> Terminate Project </b></p>
                </div>
                 <form @submit.prevent="onSubmit" class="form-content form-wide" enctype="multipart/form-data">
                      <fieldset class="form-box">
                          <div id="formError" class="row row-error text-center">
                          {{ error }}
                          </div>
                          <div class="row"></div>
                          <button type="submit" class="btn-proceed red"><span>Terminate Project <i
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
        requestPosition: null,
    }
  },
  methods: {
    setRequestPosition() {
        this.requestPosition = window.localStorage.getItem("position");
    },
    onSubmit() {
      let endpoint = `/api/projects/projects/${this.id}/`;
      let method = "DELETE"
      try {
        apiService(endpoint, method).then(
            this.$router.push({
              name: 'home',
            })
        )
      }
      catch (err) {
        this.error = err
      }
    },
  },
  created() {
    this.setRequestPosition();
    document.title = "Terminate Project";
  }
}
</script>
