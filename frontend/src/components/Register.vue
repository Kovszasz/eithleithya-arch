<template>
  <v-card
    class="mx-auto"
    max-width="500"
  >
    <v-card-title class="title font-weight-regular justify-space-between">
      <span>{{ currentTitle }}</span>
      <v-avatar
        color="primary lighten-2"
        class="subheading white--text"
        size="24"
        v-text="step"
      ></v-avatar>
    </v-card-title>
    <v-window v-model="step">
      <v-window-item :value="0">
        <div class="pa-4 text-center">
           <div
          @dragend="dialog = true"
        >
       <!-- <file-pond
          name="test"
          ref="pond"
          label-idle="Drop files here..."
          v-bind:allow-multiple="false"
          accepted-file-types="image/*, .txt"
          server="/api/customer/file/"
          v-bind:files="myFiles"
          v-on:init="handleFilePondInit"
          />-->
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
      </v-window-item>
      <v-window-item :value="1">
        <v-card-text>
          <v-text-field
            placeholder="Email"
            value="email..."
            v-model="payload.email"
          ></v-text-field>
          <span class="caption grey--text text--darken-1">
            This is the email you will use to login to your Vuetify account
          </span>
        </v-card-text>
      </v-window-item>
      <v-window-item :value="2">
        <v-card-text>
          <v-text-field
            placeholder="First name"
            type="text"
            v-model="payload.first_name"
          ></v-text-field>
          <v-text-field
            placeholder="Last name"
            type="text"
            v-model="payload.last_name"
          ></v-text-field>
          <v-text-field
            placeholder="Address line 1"
            type="text"
            v-model="payload.address_1"
          ></v-text-field>
          <v-text-field
            placeholder="Address line 2"
            type="text"
            v-model="payload.address_2"
          ></v-text-field>
          <v-text-field
            placeholder="ZIP code"
            type="text"
            v-model="payload.ZIP_code"
          ></v-text-field>
          <v-text-field
            placeholder="City"
            type="text"
            v-model="payload.city"
          ></v-text-field>
          <v-text-field
            placeholder="Country"
            type="text"
            v-model="payload.country"
          ></v-text-field>
          <span class="caption grey--text text--darken-1">
            Please enter a password for your account
          </span>
        </v-card-text>
      </v-window-item>
      <v-window-item :value="3">
  <v-row>
    <v-col cols="12" sm="6" offset-sm="3">
      <v-card>
        <v-container fluid>
          <v-row>
            <v-col
              v-for="n in 9"
              :key="n"
              class="d-flex child-flex"
              cols="4"
            >
              <v-card flat tile class="d-flex">
                <v-img
                  :src="`https://picsum.photos/500/300?image=${n * 5 + 10}`"
                  :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
                  aspect-ratio="1"
                  class="grey lighten-2"
                >
                  <template v-slot:placeholder>
                    <v-row
                      class="fill-height ma-0"
                      align="center"
                      justify="center"
                    >
                      <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                      </v-row>
                        </template>
                      </v-img>
                    </v-card>
                  </v-col>
                </v-row>
                </v-container>
            </v-card>
          </v-col>
        </v-row>
      </v-window-item>
    </v-window>
    <v-divider></v-divider>
    <v-card-actions>
      <v-btn
        :disabled="step === 1"
        text
        @click="step--"
      >
        Back {{ step }}
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn
       @click="send_order"
       >
       Send
       </v-btn>
       <v-btn
        color="primary"
        depressed
        @click="step++"
       >
        Next
      </v-btn>
    </v-card-actions>
  </v-card>
</template>
<script>
import api from '../api.js'
import axios from 'axios'
export default {
  name: 'Register',
  props: {
  },
  data: () => ({
    step: 0,
    payload: {
      email: '',
      ZIP_code: '',
      address_1: '',
      address_2: '',
      last_name: '',
      first_name: '',
      city: '',
      country: '',
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
  methods: {
    send_order () {
      console.log(this.files)
      console.log(this.payload)
      const formData = new FormData()
      formData.append('US', this.files[0])
      for (var key in this.payload) {
          formData.append(key, this.payload[key])
      }
      axios.post('api/customer/', formData, {
          headers: {
            'content-type': 'multipart/form-data'
         }
      }).then(() => {
          console.log('success')
        })
    }
  }
}
</script>
