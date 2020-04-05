<template>
  <div>
    <header class="main-title">
          Próximas Clases:
        </header>
      <div class="grid-container" v-if="hasReservations">
              <div class="card-item" v-for="item in reservations" :key="item.event_date">
                <p class="card-title">
                <i class="fa fa-dumbbell"></i>
                {{item.event_name}}
                </p>
                <p class="card-description">
                  <i class="fa fa-clock"></i>
                  {{moment(item.event_date).format('LLL')}}
                </p>
              </div>

      </div>
          <div v-else>
            No existen datos o no tiene permiso para verlos
          </div>
  </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'

export default {
  name: 'reservations',
  methods: {
    moment: () => {
      return moment()
    }
  },
  computed: {
    hasReservations () {
      return this.reservations.length > 0
    }
  },
  async created () {
    try {
      const response = await axios.get('http://localhost:8000/api/reservations/')
      console.log('response', response)
      this.reservations = response.data || []
    } catch (error) {
      if (error.response) {
        console.log('error', error)
      }
    }
  },
  data () {
    return {
      reservations: [
        // {event_name: 'Test Reservation', 'event_date': '29-Ago-2020'},
        // {event_name: 'Test Reservation', 'event_date': '28-Ago-2020'},
        // {event_name: 'Test Reservation', 'event_date': '27-Ago-2020'},
        // {event_name: 'Test Reservation', 'event_date': '26-Ago-2020'},
        // {event_name: 'Test Reservation', 'event_date': '25-Ago-2020'},
        // {event_name: 'Test Reservation', 'event_date': '24-Ago-2020'},
        // {event_name: 'Test Reservation', 'event_date': '23-Ago-2020'}
      ]
    }
  }
}
</script>

<style>

</style>
