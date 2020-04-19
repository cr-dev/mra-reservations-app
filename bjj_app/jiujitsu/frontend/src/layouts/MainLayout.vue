<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>
          {{academy.name}}
        </q-toolbar-title>

        <div>
          TODO: UserInfo - Login/Logout
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-1"
    >
      <q-list>
        <q-item-label
          header
          class="text-grey-8"
        >
          {{academy.mainMenuTitle}}
        </q-item-label>
        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-footer elevated>
        <q-toolbar>
          <q-toolbar-title class="flex flex-center">
            <small>Derechos reservados <a class="text-white" href="mailto:cescalante2988@gmail.com">Carlos Escalante</a> 2020.</small>
          </q-toolbar-title>
        </q-toolbar>
      </q-footer>

    <q-page-container>
      <router-view class="q-pa-md" />
    </q-page-container>
  </q-layout>
</template>

<script>
import EssentialLink from 'components/EssentialLink'

export default {
  name: 'MainLayout',

  components: {
    EssentialLink
  },

  data () {

    return {
      academy: {
        name: 'Santa Ana BJJ',
        mainMenuTitle: 'Menu Principal',
      },
      leftDrawerOpen: false,
      essentialLinks: [
        {
          title: 'Inicio',
          caption: 'Ver clases y reservaciones',
          icon: 'home',
          link: ''
        },
        {
          title: 'Horario',
          caption: 'Ver próximas clases',
          icon: 'schedule',
          link: 'horario'
        },
        {
          title: 'Usuarios',
          caption: 'Agregar, borrar, y más...',
          icon: 'supervisor_account',
          link: 'usuarios'
        }
      ]
    }
  }
}
</script>
