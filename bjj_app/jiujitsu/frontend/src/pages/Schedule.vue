<template>
<q-page>
      <div class="col">

        <h4>Horario Próximas Clases</h4>

        <q-toolbar>
            <q-btn stretch flat label="Anterior" @click="calendarPrev" />
            <q-separator vertical />
            <q-btn stretch flat label="Siguiente" @click="calendarNext" />
            <q-space />
        </q-toolbar>
        
        <q-separator />

        <q-calendar
            ref="calendar"
            v-model="selectedDate"
            view="week-agenda"
            locale="es-ES"
            short-weekday-label
            show-work-weeks
            animated
            v-touch-swipe.mouse.left.right="handleSwipe"
            transition-prev="slide-right"
            transition-next="slide-left"
            :resources="resources">

        
            <template #day-body="day">
                <template v-for="(agenda) in getAgenda(day)">
                <div
                    :key="day.date + agenda.time"
                    :label="agenda.time"
                    class="justify-start q-ma-sm shadow-5 bg-grey-2"
                >
                    <div v-if="agenda.avatar" class="row justify-center" style="margin-top: 30px; width: 100%;">
                    <q-avatar style="margin-top: -25px; margin-bottom: 10px; font-size: 60px; max-height: 50px;">
                        <img :src="agenda.avatar" style="border: #9e9e9e solid 5px;">
                    </q-avatar>
                    </div>
                    <div class="col-12 q-px-sm">
                    <strong>{{ agenda.time }}</strong>
                    </div>
                    <div v-if="agenda.desc" class="col-12 q-px-sm" style="font-size: 10px;">
                    {{ agenda.desc }}
                    </div>
                </div>
                </template>
            </template>

        </q-calendar>
      </div>
    </q-page>
</template>

<script>
import { QCalendar } from '@quasar/quasar-ui-qcalendar'

export default {
    name: 'Horario',
    components: {
        QCalendar
    },

    computed: {
        currentMonth() {
            return this.$refs.calendar
        }
    },

    methods: {
        getAgenda (day) {
        return this.agenda[parseInt(day.weekday, 10)]
        },


        calendarNext () {
            console.log(this.$refs.calendar)
        this.$refs.calendar.next()
        },
        calendarPrev () {
        this.$refs.calendar.prev()
        },
        handleSwipe ({ evt, ...info }) {
            if (this.dragging === false) {
                if (info.duration >= 30 && this.ignoreNextSwipe === false) {
                if (info.direction === 'right') {
                    this.calendarPrev()
                } else if (info.direction === 'left') {
                    this.calendarNext()
                }
                } else {
                this.ignoreNextSwipe = false
                }
            }
            // stopAndPrevent(evt)
            evt.cancelable !== false && evt.preventDefault()
            evt.stopPropagation()
        }
    },

    data () {
        return {
            selectedDate: '',
            dragging: false, // used for drag-and-drop
            ignoreNextSwipe: false, // used for drag-and-drop
            resources: [
                { label: 'BJJ Gi' },
                { label: 'BJJ No Gi' },
                { label: 'Físico' },
                { label: 'Olivia' },
                { label: 'Board Room' },
                { label: 'Room-1' },
                { label: 'Room-2' }
            ],

            agenda: {
        // value represents day of the week
        1: [
          {
            time: '08:30',
            avatar: 'https://cdn.quasar.dev/img/avatar.png',
            desc: 'Meeting with HR'
          },
          {
            time: '10:00',
            avatar: 'https://cdn.quasar.dev/img/avatar1.jpg',
            desc: 'Meeting with Karen'
          }
        ],
        2: [
          {
            time: '08:00',
            avatar: 'https://cdn.quasar.dev/img/boy-avatar.png',
            desc: 'Meeting with CEO'
          },
          {
            time: '11:30',
            avatar: 'https://cdn.quasar.dev/img/avatar2.jpg',
            desc: 'Meeting with Alisha'
          },
          {
            time: '17:00',
            avatar: 'https://cdn.quasar.dev/img/avatar3.jpg',
            desc: 'Meeting with Sarah'
          }
        ],
        3: [
          {
            time: '08:00',
            desc: 'Stand-up SCRUM',
            avatar: 'https://cdn.quasar.dev/img/material.png'
          },
          {
            time: '09:00',
            avatar: 'https://cdn.quasar.dev/img/boy-avatar.png'
          },
          {
            time: '10:00',
            desc: 'Sprint planning',
            avatar: 'https://cdn.quasar.dev/img/material.png'
          },
          {
            time: '13:00',
            avatar: 'https://cdn.quasar.dev/img/avatar1.jpg'
          }
        ],
        4: [
          {
            time: '09:00',
            avatar: 'https://cdn.quasar.dev/img/avatar3.jpg'
          },
          {
            time: '10:00',
            avatar: 'https://cdn.quasar.dev/img/avatar2.jpg'
          },
          {
            time: '13:00',
            avatar: 'https://cdn.quasar.dev/img/material.png'
          }
        ],
        5: [
          {
            time: '08:00',
            avatar: 'https://cdn.quasar.dev/img/boy-avatar.png'
          },
          {
            time: '09:00',
            avatar: 'https://cdn.quasar.dev/img/avatar2.jpg'
          },
          {
            time: '09:30',
            avatar: 'https://cdn.quasar.dev/img/avatar4.jpg'
          },
          {
            time: '10:00',
            avatar: 'https://cdn.quasar.dev/img/avatar5.jpg'
          },
          {
            time: '11:30',
            avatar: 'https://cdn.quasar.dev/img/material.png'
          },
          {
            time: '13:00',
            avatar: 'https://cdn.quasar.dev/img/avatar6.jpg'
          },
          {
            time: '13:30',
            avatar: 'https://cdn.quasar.dev/img/avatar3.jpg'
          },
          {
            time: '14:00',
            avatar: 'https://cdn.quasar.dev/img/linux-avatar.png'
          },
          {
            time: '14:30',
            avatar: 'https://cdn.quasar.dev/img/avatar.png'
          },
          {
            time: '15:00',
            avatar: 'https://cdn.quasar.dev/img/boy-avatar.png'
          },
          {
            time: '15:30',
            avatar: 'https://cdn.quasar.dev/img/avatar2.jpg'
          },
          {
            time: '16:00',
            avatar: 'https://cdn.quasar.dev/img/avatar6.jpg'
          }
        ]
      }
        }
    }
}
</script>

<style>

</style>