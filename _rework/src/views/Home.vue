<template>
  <div class="row plain-element">
    <div class="row header details-header">
      <div class="col-md-2 text-right plain-element img-column">
          <img src="@/assets/img/d.png" class="img responsive img-header">
      </div>

      <div class="col-md-10 text-left">
          <div class="box">
            <h4>Kanban Board</h4>
            <a href="" class="btn-algorithm blue">Propose Project</a>
          </div>
          <h6>Active Projects:  &nbsp; <b class="counter">12 </b></h6>
          <h6>Issues Counter:  &nbsp; <b class="counter">14 </b></h6>
      </div>
    </div>
    <div class="dashboard-cards">
      <div class="row row-cards">
          <div class="col-sm-8 col-md-4 col-lg-25 text-center">
              <div class="card card-status">
                  <i class="fas fa-lightbulb"></i> Proposed
              </div>
          </div>
          <div class="col-sm-8 col-md-4 col-lg-25 text-center">
              <div class="card card-status">
                  <i class="fas fa-chart-line"></i> Analysis
              </div>
          </div>
          <div class="col-sm-8 col-md-4 col-lg-25 text-center">
              <div class="card card-status">
                  <i class="fas fa-cog"></i> Development
              </div>
          </div>
          <div class="col-sm-8 col-md-4 col-lg-25 text-center">
              <div class="card card-status">
                  <i class="fas fa-code"></i> Test
              </div>
          </div>
          <div class="col-sm-8 col-md-4 col-lg-25 text-center">
              <div class="card card-status">
                  <i class="fas fa-space-shuttle"></i> Deployment
              </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'home',
  components: {
  },
  created() {
    document.title = "Project Dashboard | Septellar";
  }
}
</script>
