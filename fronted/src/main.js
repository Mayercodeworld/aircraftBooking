import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Buefy from 'buefy';
import 'buefy/dist/buefy.css';

const app = createApp(App)

app.use(router)
app.use(Buefy)
app.mount('#app')
