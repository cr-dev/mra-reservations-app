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
                <div class="card-buttons">
                  <el-row>
                    <el-col :span="12">
                      <div class="grid-content">
                       <el-button type="primary">Reservar</el-button>
                    </div>
                  </el-col>
                    <el-col :span="12">
                      <div class="grid-content">
                        <el-select v-model="value" placeholder="Select">
                          <el-option
                            v-for="item in options"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                          </el-option>
                        </el-select>
                      </div>
                    </el-col>
                  </el-row>

                </div>

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
      ],
      options: [{
        value: 'Option1',
        label: 'Option1'
      }, {
        value: 'Option2',
        label: 'Option2'
      }, {
        value: 'Option3',
        label: 'Option3'
      }, {
        value: 'Option4',
        label: 'Option4'
      }, {
        value: 'Option5',
        label: 'Option5'
      }],
      value: ''
    }
  }
}
</script>

<style>

</style>
