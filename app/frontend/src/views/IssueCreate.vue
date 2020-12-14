<template>
<div v-if="getUsername() == getProject().pm_email" class="row plain-element">
  <div class="row header details-header">
      <div class="col m1 text-left plain-element img-column">
          <img src="@/assets/img/propose-project.jpg" class="img responsive img-header">
      </div>
      <div class="col m9 l6 text-left plain-element">
          <div class="box box-details">
              <h5>Report Project Issue</h5>
          </div>
      </div>
  </div>
  <div class="dashboard-cards">
        <div class="row row-form">
          <div class="col s8 m6 l5 plain-element">
              <div class="card form-card">
                  <div class="card-header">
                      <img src="@/assets/img/icons/gear.png" class="img-responsive">
                      <h5> Report Project Issue </h5>
                  </div>
                  <form @submit.prevent="reportIssue" class="form-content form-wide" enctype="multipart/form-data">
                      <fieldset class="form-box">
                          <div id="formError" class="row row-error text-center">
                          {{ error }}
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>Name:</h6>
                            </div>
                            <div class="input-field col s8">
                                <input v-model="issueName" name="issueName" class="form-control"/>
                            </div>
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>Description:</h6>
                            </div>
                            <div class="input-field col s8">
                                <input v-model="issueDescription" name="issueDescription" class="form-control"/>
                            </div>
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>Cost:</h6>
                            </div>
                            <div class="input-field col s8">
                                <input v-model="issueCost" name="issueCost" type="number" min="0" max="450" class="form-control" style="text-align: left"/>
                            </div>
                          </div>
                          <div class="row"></div>

                      </fieldset>
                      <button type="submit" class="btn-proceed"><span>Report Project Issue <i
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
  name: 'IssueCreate',
  props: {
    id: {
      required: true,
    }
  },
  components: {
    NoPermissionComponent
  },
  data() {
    return {
      error: "",
      issueName: null,
      issueDescription: null,
      issueCost: null,
    }
  },
  methods: {
    ...mapGetters(["getUsername", "getPosition", "getProject"]),
    ...mapActions(["fetchProjectDetails", "performReportIssue"]),
    reportIssue() {
        this.performReportIssue({"project": this.id, "name": this.issueName, "description" : this.issueDescription, "cost" : this.issueCost  })
    },
  },
  created() {
    this.fetchProjectDetails(this.id);
    document.title = "Report Project Issue";
  }
}
</script>