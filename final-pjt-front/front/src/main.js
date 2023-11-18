<<<<<<< HEAD
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
=======
// import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
>>>>>>> develop_jik
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
})

const app = createApp(App)
const pinia = createPinia()

<<<<<<< HEAD
pinia.use(piniaPluginPersistedstate)

// app.use(createPinia())
=======
// pinia.use(piniaPluginPersistedstate)

app.use(pinia) 
>>>>>>> develop_jik
app.use(router)
app.use(pinia)
app.use(vuetify)

app.mount('#app')
