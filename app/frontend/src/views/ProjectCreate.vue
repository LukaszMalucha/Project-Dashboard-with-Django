<template>
<div v-if="getPosition()" class="row plain-element">
  <div class="row header details-header">
      <div class="col m1 text-left plain-element img-column">
          <img src="@/assets/img/propose-project.jpg" class="img responsive img-header">
      </div>
      <div class="col m9 l6 text-left plain-element">
          <div class="box box-details">
              <h5>Propose Project </h5>
          </div>
          <p>
            You can always create a new project from a template or another project. But if you need to start fresh,
            you can create a blank project by filling the form below. After your project is approved,
            you’ll be able to launch it and start gathering your team. Upon project completion,
            Reward will be distributed among team members.
          </p>
      </div>
  </div>
  <div class="dashboard-cards">
    <div class="row row-form">
        <div class="col s8 m6 l5 plain-element">
            <div class="card form-card">
                <div class="card-header">
                    <img src="@/assets/img/icons/gear.png" class="img-responsive">
                    <h5> Propose Project </h5>
                </div>
                 <form @submit.prevent="createProject" class="form-content form-wide" enctype="multipart/form-data">
                      <fieldset class="form-box">
                          <div id="formError" class="row row-error text-center">
                          {{ error }}
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>Name:</h6>
                            </div>
                            <div class="input-field col s8">
                                <input v-model="projectName" name="Name" class="form-control"/>
                            </div>
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>Description:</h6>
                            </div>
                            <div class="input-field col s8">
                                <input v-model="projectDescription" name="Description" class="form-control"/>
                            </div>
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>Project Schedule:</h6>
                            </div>
                            <div class="input-field col s8">
                                <input type="file" id="file" ref="file"
                                    v-on:change="handleFileUpload()"
                                      class="form-control file_input"  accept=".jpg,.png">
                            </div>
                          </div>
                          <div class="row"></div>

                      </fieldset>
                      <button type="submit" class="btn-proceed"><span>Propose Project <i
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
  name: 'project-create',
  components: {
    NoPermissionComponent
  },
  data() {
    return {
      error: "",
      projectName: null,
      projectDescription: null,
      projectSchedule: null,
    }
  },
   methods: {
    ...mapGetters(["getPosition"]),
    ...mapActions(["performCreateProject"]),
    handleFileUpload() {
      this.projectSchedule = this.$refs.file.files[0];
    },
    createProject() {
      if (!this.projectName || !this.projectDescription || !this.projectSchedule) {
        this.error = "Fields can't be empty";
      } else {
        this.performCreateProject({"projectName": this.projectName,
                                   "projectDescription": this.projectDescription,
                                   "projectSchedule": this.projectSchedule
                                  })
      }
    }
    
  },  
  created() {
    document.title = "Start New Project";
  }
}
</script>