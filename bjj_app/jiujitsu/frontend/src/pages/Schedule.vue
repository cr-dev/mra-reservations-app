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
            view="month"
            locale="es-ES"
            show-day-of-year-label
            short-weekday-label
            show-work-weeks
            animated
            v-touch-swipe.mouse.left.right="handleSwipe"
            transition-prev="slide-right"
            transition-next="slide-left"
            :resources="resources">

            <template #scheduler-resource-day="{ day, index, resource }">
                <q-btn class="fit"><span class="ellipsis" style="font-size: 10px;">{{ resource.label }}:{{ day.day }}</span></q-btn>
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

    methods: {
        calendarNext () {
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
                { label: 'John' },
                { label: 'Mary' },
                { label: 'Susan' },
                { label: 'Olivia' },
                { label: 'Board Room' },
                { label: 'Room-1' },
                { label: 'Room-2' }
            ]
        }
    }
}
</script>

<style>

</style>