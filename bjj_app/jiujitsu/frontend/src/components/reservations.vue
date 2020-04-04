<template>
  <div>
  <header class="main-title">
      Listado de clases futuras:
  </header>
  <section>
      <div class="grid-container">
          <div class="card-item" v-for="item in reservations" :key="item.event_date">
              <p>{{item.event_name}}</p>
              <br>
              <p>{{item.event_date}}</p>
        </div>
      </div>
  </section>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'reservations',
  created () {
    axios.get('http://localhost:8000/api/reservations/').then(response=> {
        console.log('response from DRF', response)
    })
  },
  data () {
    return {
      reservations: [
        {event_name: 'Test Reservation', 'event_date': '29-Ago-2020'},
        {event_name: 'Test Reservation', 'event_date': '28-Ago-2020'},
        {event_name: 'Test Reservation', 'event_date': '27-Ago-2020'},
        {event_name: 'Test Reservation', 'event_date': '26-Ago-2020'},
        {event_name: 'Test Reservation', 'event_date': '25-Ago-2020'},
        {event_name: 'Test Reservation', 'event_date': '24-Ago-2020'},
        {event_name: 'Test Reservation', 'event_date': '23-Ago-2020'}
      ]
    }
  }
}
</script>

<style>

</style>
