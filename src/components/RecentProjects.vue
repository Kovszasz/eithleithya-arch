<template>
  <section
    id="recent-projects"
    class="hide-overflow"
  >
    <v-layout>
      <v-flex
        xs12
        md6
        primary
        text-xs-center
        pa-5
        white--text
      >
        <base-bubble-1
          style="transform: rotate(180deg) translateX(25%)"
        />
        <base-heading>
          Recent Projects
        </base-heading>

        <base-text class="mb-5">
          Lorem ipsum dolor sit amet, consectetur adipi<br>
          scin elit. Etiam vulputate augue vel felis gravida<br>
          porta. Lorem ipsum dolor sit amet.
        </base-text>

        <v-card color="secondary">
          <v-container
            grid-list-md
            pa-2
          >
            <v-layout wrap>
              <v-flex
                v-for="project in projects"
                :key="project"
                xs12
                md6
              >
                <a href="#">
                  <v-img
                    :src="require(`@/assets/${project}.jpeg`)"
                    max-height="300"
                  />
                </a>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card>
      </v-flex>
      <v-flex
        hidden-sm-and-down
        md6
      >
        <v-img
          :src="require('@/assets/recentprojects.png')"
          height="100%"
          @click="order"
        />
      </v-flex>
    </v-layout>
      <v-row justify="center">
    <v-dialog
      v-model="dialog"
      width="600px"
    >
    <register  />
    <v-btn
      color="primary"
      text
      @click="dialog = false"
      >
        Cancel
      </v-btn>
    </v-dialog>
  </v-row>
  </section>
</template>

<script>
/* import vueFilePond from 'vue-filepond'
import 'filepond/dist/filepond.min.css'
import 'filepond-plugin-image-preview/dist/filepond-plugin-image-preview.min.css'
import FilePondPluginFileValidateType from 'filepond-plugin-file-validate-type'
import FilePondPluginImagePreview from 'filepond-plugin-image-preview'
import mdbFileUpload from 'mdb-file-upload';
const FilePond = vueFilePond(FilePondPluginFileValidateType, FilePondPluginImagePreview)
*/
export default {
  components: {
    register: () => import('@/components/Register')
   // FilePond
  },
  data: () => ({
    myFiles: [],
    files: [],
    dialog: false,
    projects: [
      'project1',
      'project2',
      'project3',
      'project4'
    ]
  }),
  methods: {
   // handleFilePondInit: function () {
   //   console.log('FilePond has initialized')
      // FilePond instance methods are available on `this.$refs.pond`
   // }
    order() {
      this.$router.push({ name: 'order' })
    }
  }
}
</script>
