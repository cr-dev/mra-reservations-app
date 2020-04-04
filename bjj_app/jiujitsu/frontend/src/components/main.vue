<template>
  <div class="intro">
    <p>{{intro}}</p>
    <reservations></reservations>
  </div>
</template>

<script>
import Reservations from './reservations.vue'
export default {
  components: {
    Reservations
  },
  name: 'home',
  data () {
    return {
      intro: `Somos la primer filial de Roger Coelho BJJ en Costa Rica.

Donde las Estrellas y Human Weapon se unieron.

Instructores principales: José Gonzaléz y Adrian Gonzaléz.

Dirección: 2do piso del edificio Santa María en Santa Ana Centro.`
    }
  }
}
</script>
