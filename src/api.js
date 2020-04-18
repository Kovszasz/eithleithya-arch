import axios from 'axios'

const api = axios.create({
  baseURL: 'https://eithleithya-api.herokuapp.com/api/',
  // baseURL: 'http://127.0.0.1:8000',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
})

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `JWT ${token}`;
    }

    return config;
  },

  (error) => {
    return Promise.reject(error);
  }
)

export default api
