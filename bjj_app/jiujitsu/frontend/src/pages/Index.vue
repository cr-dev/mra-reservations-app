<template>
  <q-page>
     <div class="row">
      <div class="col flex flex-center">
        <img alt="Santa Ana BJJ Logo" height="400px" src="~assets/logo.jpg">
        <!-- <q-table
          title="BJJ Santa Ana - Proximas Clases"
          :data="data"
          :columns="columns"
          row-key="name"
        /> -->
      </div>
    </div>
  </q-page>
</template>

<script>
import moment from 'moment'

export default {
  name: 'PageIndex',
  methods: {
    async fetchClasses () {
      const response = await this.$axios.get('http://localhost:8000/api/reservations/')
      return response.data
    },
  },
  created: async function() {
    this.msg = "Hellooo!"
    this.loading = true
    this.data = [] //await this.fetchClasses()
    this.loading = false
  },
  data: function() {
    return {
      msg: this.msg,
      columns: [
        {
          name: 'name',
          required: true,
          label: 'Nombre de la clase',
          align: 'left',
          field: row => row.event_name,
          format: val => `${val}`,
          sortable: true
        },
        { name: 'date', align: 'center', label: 'Fecha', field: row => moment(row.event_date).format('LLL'), sortable: true },
      ],
      data: this.data
    }
  }
}
</script>
