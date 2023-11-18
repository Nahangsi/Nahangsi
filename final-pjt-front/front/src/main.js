import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

// 로컬스토리지
import PiniaPluginPersistedstate from "pinia-plugin-persistedstate";

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
