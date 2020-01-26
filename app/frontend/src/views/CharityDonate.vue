<template>
<div v-if="total == 0" class="row plain-element">
  <div class="row header details-header">
      <div class="col-md-1 text-left plain-element img-column">
          <img src="https://project-gamification.s3-eu-west-1.amazonaws.com/static/img/charity.jpg" class="img responsive img-header">
      </div>
      <div class="col-md-9 col-lg-6 text-left plain-element">
          <div class="box box-details">
              <h5>Your Donation List is Empty </h5>
              <router-link :to="{name: 'charity'}" class="btn-algorithm green"><i class="fas fa-1x fa-donate"></i> Back to Charities</router-link>
          </div>
        <p>
            After a successful transaction, for each LeanCoin Token you spend, the company will donate 1 &euro; for the selected Fundraising action.
            Fundraising is a great way to engage your friends, family and community to make a difference in the world. If you want to start your own fundraising project and need help, contact your program manager.
        </p>
    </div>
  </div>
</div>
<div v-else class="row plain-element">
  <div class="row header details-header">
      <div class="col-md-1 text-left plain-element img-column">
          <img src="https://project-gamification.s3-eu-west-1.amazonaws.com/static/img/charity.jpg" class="img responsive img-header">
      </div>
      <div class="col-md-8 text-left plain-element">
          <div class="box box-details">
              <h5>Donation Checkout</h5>
          </div>
          <p>
              After a successful transaction, for each LeanCoin Token you spend, the company will donate 1 &euro; for the selected Fundraising action.
              Fundraising is a great way to engage your friends, family and community to make a difference in the world. If you want to start your own fundraising project and need help, contact your program manager.
          </p>
          <h6>LeanCoins Total: <b class="counter"> {{total}} </b></h6>
      </div>
  </div>
  <div class="dashboard-cards">
    <div class="row row-form" id="rowTransactionForm">
      <div class="col-md-4 no-padding">
              <div class="card form-card">
                  <div class="card-header">
                      <img src="https://project-gamification.s3-eu-west-1.amazonaws.com/static/img/icons/charity.png" class="img-responsive">
                      <h5> Proceed with Donation </h5>
                  </div>
                  <div class="card-image">
                  <form @submit.prevent="onSubmit" class="form-content form-wide form-payment">
                      <fieldset class="form-box">
                          <div id="formError" class="row row-error text-center">
                            {{ error }}
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>Card Number:</h6>
                            </div>
                            <div class="input-field col s8">
                                <input v-model="creditCardNumber" name="creditCardNumber" class="form-control"/>
                            </div>
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>CVV Code:</h6>
                            </div>
                            <div class="input-field col s8">
                                <input v-model="cvvCode" name="cvvCode" class="form-control"/>
                            </div>
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>Expiry Month:</h6>
                            </div>
                            <div class="input-field col s8">
                                <input v-model="expiryMonth" name="expiryMonth" type="number" min="1" max="12" class="form-control"/>
                            </div>
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>Expiry Year:</h6>
                            </div>
                            <div class="input-field col s8">
                                <input v-model="expiryYear" name="expiryYear" type="number" min="2020" max="2037" class="form-control"/>
                            </div>
                          </div>
                          <input v-model="stripe_id" value="123456789" hidden/>
                          <button type="submit" class="btn-proceed"><span>Submit <i
                                  class="far fa-arrow-alt-circle-right"></i></span>
                          </button>
                      </fieldset>
                  </form>
                  </div>
              </div>
          </div>
      </div>
      <div class="row row-cards" id="rowTransactionReceipt">
        <div class="col-md-4 plain-element">
            <div class="card card-receipt">
                <div class="row row-blue">
                </div>
                <br>
                <div class="row plain-element">

                    <table>
                        <tr>
                            <td class="text-left">Donor: <b>{{ requestUser }}</b></td>
                            <td class="text-right">Date: <b>{{ date }}</b></td>
                        </tr>



                    </table>
                </div>

                <div class="row plain-element">
                    <div class="row plain-element row-total">
                        <div class="col-md-6 plain-element text-left">
                            <h4>Receipt Total</h4>
                        </div>
                        <div class="col-md-6 plain-element text-right">
                            <h4>{{ total }} &euro;</h4>
                        </div>
                    </div>
                </div>

                <div class="row plain-element">
                    <table>
                          <tr >
                            <th class="text-left">Supported Event</th>
                            <th class="text-right"> Amount</th>
                          </tr>
                          <tr v-for="element in checkout" :key="element.id">
                            <td class="text-left">{{element.name}}</td>
                            <td class="text-right">5 &euro;</td>
                          </tr>
                    </table>
                </div>
                <br><br>
                <div class="row plain-element row-blue">
                </div>
            </div>
        </div>
    </div>
  </div>
</div>
</template>



<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: 'CharityDonate',
  props: {
    checkout: {
      type: Array,
    },
    checkoutList: {
      type: Array,
    }
  },
  components: {
  },
  data() {
    return {
      error: "",
      creditCardNumber: null,
      cvvCode: null,
      expiryMonth: null,
      expiryYear: null,
      stripe_id: 123456789,
      requestUser: null,

    }
  },
  computed: {
    date() { return Date().substring(4,15) },
    total()  { if (this.checkout) {
                  return this.checkout.length * 5
                } else {
                  return 0
                }
               }

  },
  methods: {
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("email");
    },
    onSubmit() {
      if (!this.creditCardNumber || !this.cvvCode || !this.expiryMonth || !this.expiryYear || !this.stripe_id) {
        this.error = "Fields can't be empty";
      } else if (!this.checkoutList){
        this.error = "Your donation list is empty";
      } else {
        let endpoint = "/charity/donate/";
        let method = "POST";
        apiService(endpoint, method, { checkout: this.checkoutList})
        .then(data => {
          if (data.error) {
            this.error = data.error

          } else {
            document.getElementById("rowTransactionForm").style.display="none";
            document.getElementById("rowTransactionReceipt").style.display="block";
          }
        })
        }
      }

  },

  created() {
    this.setRequestUser();
    document.title = "Donate";
    window.console.log(this.checkout)
    window.console.log(this.checkoutList)
  }
}
</script>