import { createApp } from "vue";
import { createPinia } from "pinia";
import PiniaPluginPersistedstate from "pinia-plugin-persistedstate";

import App from "./App.vue";
import router from "./router";

// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

const vuetify = createVuetify({
  components,
  directives,
});

const app = createApp(App);
const pinia = createPinia();

pinia.use(PiniaPluginPersistedstate);

app.use(router);
app.use(pinia);
app.use(vuetify);

app.mount("#app");
