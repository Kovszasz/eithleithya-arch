<template>
  <div class="body">
    <div id="all" class="all">
      <div id="title" class="title">
        Step 1 - Choose your file
      </div>
      <form class="slide">
        <div
          id="slides_a"
          class="slides"
        >
          <div
            class="slides_a_bottom"
          >
            <v-file-input
              v-model="files"
              color="deep-purple accent-4"
              counter
              label="File input"
              multiple
              placeholder="Select your files"
              prepend-icon="mdi-paperclip"
              outlined
              :show-size="1000"
            >
              <template v-slot:selection="{ index, text }">
                <v-chip
                  v-if="index < 2"
                  color="deep-purple accent-4"
                  dark
                  label
                  small
                >
                  {{ text }}
                </v-chip>

                <span
                  v-else-if="index === 2"
                  class="overline grey--text text--darken-3 mx-2"
                >
                  +{{ files.length - 2 }} File(s)
                </span>
              </template>
            </v-file-input>
          </div>
        </div>
        <div
          id="slides_b"
          class="slides"
        >
          <div
            class="slides_b_bottom"
          >
            <v-card-text>
              <v-text-field
                id="first_name"
                v-model="payload.first_name"
                placeholder="First name"
                type="text"
              />
              <v-text-field
                id="last_name"
                v-model="payload.last_name"
                placeholder="Last name"
                type="text"
              />
              <v-text-field
                id="address_line"
                v-model="payload.address_1"
                placeholder="Address line"
                type="text"
              />
              <v-text-field
                id="email"
                v-model="email"
                placeholder="email"
                type="text"
              />
              <v-text-field
                id="zip_code"
                v-model="payload.ZIP_code"
                placeholder="ZIP code"
                type="text"
              />
              <v-text-field
                id="city"
                v-model="payload.city"
                placeholder="City"
                type="text"
              />
              <v-text-field
                id="country"
                v-model="payload.country"
                placeholder="Country"
                type="text"
              />
            </v-card-text>
          </div>
        </div>
        <div
          id="slides_c"
          class="slides"
        >
        </div>
        <div
          id="slides_d"
          class="slides"
        >
          <div
            class="slides_d_bottom"
          >
            <div
              class="radio-paypal"
            >
              <label class="container">
                <input type="radio" name="payment-option" value="alternate">
                <span class="checkmark"></span>
              </label>
              <img
                class="paypal-img"
                src="@/assets/paypal.png"
              />
            </div>
            <div
              class="radio-crditcard"
            >
              <label class="container">
                <input type="radio" name="payment-option" value="paypal">
                <span class="checkmark"></span>
              </label>
              Bank- vagy hitelkártya
            </div>
          </div>
        </div>
      </form>
      <div
        class="buttons"
      >
        <button
          class="backbutt"
          @click="SlideBack()"
        >
          back
        </button>
        <button
          id="nextbutt"
          class="nextbutt"
          @click="SlideNext()"
        >
          next
        </button>
      </div>
    </div>
    <div class="checkform">
      <form class="check">
        <p id="sayhi" class="bigletter"></p>
        <p class="letter">We have sent you an email with a validation number.<br>Please enter this number here to confirm your email:</p>
        <input id="validation" placeholder="123456" type="text" maxlength="6"/>
        <button type="button" @click="confirmbutt()">confirm</button>
        <p class="smallletter">Send new email</p>
        <p class="letter">Mailing address:</p>
        <div class="information">
          <p id="name" class="letter"></p>
          <p id="address" class="letter"></p>
          <p id="zipcodeb" class="letter"></p>
          <p id="cityb" class="letter"></p>
          <p id="countryb" class="letter"></p>
        </div>
        <div class="paybutt">
          <div id="paypal-button-container-a"></div>
          <div id="paypal-button-container-b"></div>
        </div>
      </form>
    </div>
  </div>
</template>
<script>
import api from '../api.js'
import axios from 'axios'
import LoadScript from 'vue-plugin-load-script'
import Vue from 'vue'
Vue.use(LoadScript)

export default {
  name: 'Register',
  props: {
  },
  data: () => ({
    val: 1,
    step: 0,
    payload: {
      package: 'cheap'
    },
    files: []
  }),
  computed: {
    currentTitle () {
      switch (this.step) {
        case 0: return 'Choose service'
        case 1: return 'Sign-up'
        case 2: return 'Create a password'
        default: return 'Account created'
      }
    }
  },
  mounted() {
    var FUNDING_SOURCESA = [
          paypal.FUNDING.PAYPAL
      ];
    var FUNDING_SOURCESB = [
          paypal.FUNDING.CARD
      ];
    document.querySelectorAll('input[name=payment-option]')
    .forEach(function (el) {
      el.addEventListener('change', function (event) {
        // If PayPal is selected, show the PayPal button
        if (event.target.value === 'paypal') {
          document.body.querySelector('#paypal-button-container-a')
            .style.display = 'none';
          document.body.querySelector('#paypal-button-container-b')
            .style.display = 'block';
        }

        // If alternate funding is selected, show a different button
        if (event.target.value === 'alternate') {
          document.body.querySelector('#paypal-button-container-a')
            .style.display = 'block';
          document.body.querySelector('#paypal-button-container-b')
            .style.display = 'none';
        }
      });
    });
    // Loop over each funding source / payment method
    FUNDING_SOURCESA.forEach(function(fundingSource) {
        // Initialize the buttons
        var button = paypal.Buttons({
            fundingSource: fundingSource
        });

        // Check if the button is eligible
        if (button.isEligible()) {
            // Render the standalone button for that funding source
            button.render('#paypal-button-container-a');
        }
    });
    FUNDING_SOURCESB.forEach(function(fundingSource) {
        // Initialize the buttons
        var button = paypal.Buttons({
            fundingSource: fundingSource
        });

        // Check if the button is eligible
        if (button.isEligible()) {
            // Render the standalone button for that funding source
            button.render('#paypal-button-container-b');
        }
    });
  },
  methods: {
    send_order () {
      console.log(this.files)
      console.log(this.payload)
      const formData = new FormData()
      formData.append('US', this.files[0])
      for (var key in this.payload) {
          formData.append(key, this.payload[key])
      }
      // axios.post('https://eithleithya-api.herokuapp.com/api/customer/', formData, {
      axios.post('api/customer/', formData, {
          headers: {
            'content-type': 'multipart/form-data'
         }
      }).then(() => {
          console.log('success')
        })
    },
    SlideBack() {
      if (this.val === 2) {
        $('.slide').css('transform', 'translateX(-0px)');
        $('.backbutt').css('opacity', '0');
        $('.all').css('height', '250px');
        document.getElementById('title').innerHTML = 'Step 1 - Choose your file';
        this.val = 1;
      } else if (this.val === 3) {
        $('.slide').css('transform', 'translateX(-400px)');
        $('.all').css('height', '90%');
        document.getElementById('title').innerHTML = 'Step 2 - Some information';
        this.val = 2;
      } else if (this.val === 4) {
        $('.slide').css('transform', 'translateX(-800px)');
        $('.all').css('height', '350px');
        document.getElementById('title').innerHTML = 'Step 2 - Choose service';
        document.getElementById('nextbutt').innerHTML = 'next';
        $('.backbutt').css('right', '100px');
        $('.nextbutt').css('width', '50px');
        $('.nextbutt').css('background-color', 'white');
        $('.nextbutt').css('color', 'gray');
        this.val = 3;
      }
    },
    SlideNext() {
      if (this.val === 1) {
        $('.slide').css('transform', 'translateX(-400px)');
        $('.backbutt').css('opacity', '1');
        $('.all').css('height', '90%');
        document.getElementById('title').innerHTML = 'Step 2 - Some information';
        this.val = 2;
      } else if (this.val === 2) {
        $('.slide').css('transform', 'translateX(-800px)');
        $('.all').css('height', '350px');
        document.getElementById('title').innerHTML = 'Step 3 - Choose service';
        this.val = 3;
      } else if (this.val === 3) {
        $('.slide').css('transform', 'translateX(-1200px)');
        $('.all').css('height', '350px');
        document.getElementById('title').innerHTML = 'Step 4 - Pay with';
        document.getElementById('nextbutt').innerHTML = 'check';
        $('.backbutt').css('right', '160px');
        $('.nextbutt').css('width', '100px');
        $('.nextbutt').css('background-color', '#37AEF2');
        $('.nextbutt').css('color', 'white');
        this.val = 4;
      } else if (this.val === 4) {
        var firstname = document.getElementById('first_name').value;
        var lastname = document.getElementById('last_name').value;
        var addressline = document.getElementById('address_line').value;
        var email = document.getElementById('email').value;
        var zipcode = document.getElementById('zip_code').value;
        var city = document.getElementById('city').value;
        var country = document.getElementById('country').value;
        document.getElementById('sayhi').innerHTML = 'Hi ' + firstname + '!';
        document.getElementById('name').innerHTML = firstname + ' ' + lastname;
        document.getElementById('address').innerHTML = addressline;
        document.getElementById('zipcodeb').innerHTML = zipcode;
        document.getElementById('cityb').innerHTML = city;
        document.getElementById('countryb').innerHTML = country;
        $('.checkform').show();
      }
    },
    confirmbutt() {
      var ertek = 123456;
      var code = document.getElementById('validation').value;
      if (parseInt(code) === ertek) {
        $('.paybutt').css('opacity', '1');
        $('.information').css('opacity', '1');
        $('.paybutt').css('pointer-events', 'auto');
      }
    }
  }
}
</script>
<style>
.body{
  width: 100%;
  height: 100%;
}
body::-webkit-scrollbar {
  display: none;
}
body {
  -ms-overflow-style: none;
}
.all{
  position: relative;
  margin: auto;
  margin-top: 40px;
  width: 400px;
  height: 250px;
  border: solid lightgray 2px;
  border-radius: 6px;
  overflow: hidden;
  transition: height 0.4s;
  background-color: white;
}
.title{
padding-top: 5px;
padding-left: 20px;
color: gray;
}
.slide{
  position: absolute;
  top: 40px;
  left: 0;
  width: 1602px;
  height: 86%;
  transform: translateX(-0px);
  transition: transform 0.2s;
}
.slides{
  position: relative;
  width: 400px;
  height: 100%;
  float: left;
}
#slides_a{
  /*background-color: white;*/
}
#slides_b{
  /*background-color: lightgray;*/
}
#slides_c{
  /*background-color: gray;*/
}
#slides_d{
  /*background-color: gray;*/
}
.slides_a_bottom{
  width: 350px;
  margin-top: 30px;
  margin-left: 20px;
}
.slides_d_bottom{
  width: 350px;
  margin-top: 50px;
  margin-left: 20px;
}
.slides_b_bottom{
  height: 100%;
  width: 350px;
  margin-left: 20px;
  overflow: auto;
}
.slides_b_bottom::-webkit-scrollbar {
    display: none;
}
.radio-crditcard{
  background-color: #2C2E2F;
  width: 100%;
  border-radius: 4px;
  height: 50px;
  text-align: center;
  color: white;
  line-height: 50px;
  margin-top: 18px;
}
.radio-paypal{
  background-color: #ffc439;
  width: 100%;
  border-radius: 4px;
  height: 50px;
  text-align: center;
  color: white;
  line-height: 50px;
}
.paypal-img{
  width: 90px;
  margin-top: 13px;
  margin-left: -25px;
}
.container input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}
.checkmark {
  position: absolute;
  height: 25px;
  width: 25px;
  background-color: #ccc;
  margin-top: 12px;
  left: 40px;
}
.container:hover input ~ .checkmark {
  background-color: #B2B2B2;
}
.container input:checked ~ .checkmark {
  background-color: #37AEF2;
}
.checkmark:after {
  content: "";
  position: absolute;
  display: none;
}
.container input:checked ~ .checkmark:after {
  display: block;
}
.container .checkmark:after {
  left: 9px;
  top: 5px;
  width: 7px;
  height: 13px;
  border: solid white;
  border-width: 0 3px 3px 0;
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
}
.buttons{
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 60px;
  background-color: white;
  border-top: solid 1px lightgray;
}
.backbutt{
  position: absolute;
  bottom: 15px;
  right: 100px;
  width: 50px;
  height: 30px;
  line-height: 27px;
  border-radius: 5px;
  color: gray;
  opacity: 0;
  transition: opacity 0.2s;
  box-shadow: 0px 2px 5px lightgray;
  font-weight: bold;
  transition: right 0.2s;
}
.nextbutt{
  position: absolute;
  bottom: 15px;
  right: 40px;
  width: 50px;
  height: 30px;
  line-height: 27px;
  border-radius: 5px;
  color: gray;
  box-shadow: 0px 2px 5px lightgray;
  font-weight: bold;
  transition: width 0.2s, background-color 0.2s;
}
.checkform{
  display: none;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.7);
  z-index: 10;
  vertical-align: bottom;
}
.check{
  position: absolute;
  top: 50%;
  left: 50%;
  margin-left: -400px;
  margin-top: -250px;
  width: 800px;
  height: 500px;
  background-color: white;
}
.smallletter{
  font-size: 14px;
  margin-left: 30px;
}
.letter{
  font-size: 17px;
  margin-left: 30px;
}
.bigletter{
  font-size: 20px;
  margin-left: 30px;
  margin-top: 30px;
}
#validation{
  border: 1px solid black;
  margin-left: 30px;
  border-radius: 10px;
  height: 30px;
  width: 100px;
  font-family: "Courier New", Courier, "Lucida Sans Typewriter";
  font-weight: bold;
  font-size: 18px;
  padding-left: 10px;
  letter-spacing: 2px;
}
::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
  color: gray;
  opacity: 0.5; /* Firefox */
}
.information{
  opacity: 0.4;
  width: 450px;
  height: 300px;
}
.paybutt{
  position: absolute;
  width: 300px;
  right: 40px;
  top: 60px;
  opacity: 0.4;
  pointer-events: none;
}
</style>
