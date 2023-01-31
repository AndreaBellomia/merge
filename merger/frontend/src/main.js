import './assets/main.css'



// GEt CRSF Token From Django
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// Axisos Setup configuration 
import axios from 'axios'

axios.defaults.baseURL = "http://127.0.0.1:8000/"
axios.defaults.headers.common['X-CSRFToken'] = getCookie('csrftoken');


// Vue js Init app
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

createApp(App).use(router, axios).mount('#app')
