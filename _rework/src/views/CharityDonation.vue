<template>
<div class="row header details-header">
    <div class="col-md-2 text-right plain-element img-column">
        <img src="@/assets/img/charity.jpg" class="img responsive img-header">
    </div>
    <div class="col-md-10 text-left">
        <div class="box">
            <h4>My Donations</h4>
            <a href="" class="btn-algorithm green"><i class="fas fa-1x fa-donate"></i>Proceed</a>
        </div>
    </div>
</div>
</template>



<script>

export default {
  name: 'charity-donation',
  components: {
  },
  created() {
    document.title = "Donate";
  }
}
</script>