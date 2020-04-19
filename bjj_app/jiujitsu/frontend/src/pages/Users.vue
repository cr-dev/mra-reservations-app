<template>
    <q-page>
      <div class="col">
        <q-table
          title="BJJ Santa Ana - Listado de Usuarios"
          :data="data"
          :columns="columns"
          row-key="name"
        />
        <div class="q-pa-md flex flex-center" v-if="errorMsg">
            <b>{{errorMsg}}</b>
        </div>
      </div>
    </q-page>
</template>

<script>
import moment from 'moment'


export default {
  name: 'Users',
  methods: {
    async loginUser () {
        try {
            const user = {
                username: 'admin',
                password: 'django2020',
            }
            const response = await this.$axios.post('http://127.0.0.1:8000/api/login/', user)
            return response.data
        } catch (error) {
            const { response } = error;
            const { request, ...errorObject } = response; // take everything but 'request'
            this.errorMsg = errorObject.data.detail
        }
    },
    async fetchUsers () {
        try {
            const response = await this.$axios.get('http://127.0.0.1:8000/api/users/')
            return response.data
        } catch (error) {
            const { response } = error;
            const { request, ...errorObject } = response; // take everything but 'request'
            this.errorMsg = errorObject.data.detail
        }
    }
  },

  created: async function() {
    this.userToken = await this.loginUser()
    this.$axios.defaults.headers.common['Authorization'] = `Token ${this.userToken.token}`
    this.data = await this.fetchUsers()
  },
  
  data: function() {
    return {
      columns: [
        {
          name: 'username',
          required: true,
          label: 'Nombre de usuario',
          align: 'left',
          format: val => `${val}`,
          field: 'username',
          sortable: true
        },
        { name: 'url', align: 'center', label: 'URL', field: 'url', sortable: true },
      ],
      data: this.data,
      errorMsg: this.errorMsg
    }
  }
}
</script>

<style>

</style>