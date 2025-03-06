// src/stores/index.js
import { defineStore } from 'pinia';

// useAuthStore 用户身份验证状态
export const useAuthStore = defineStore('auth', {
  state: () => ({
    isRegisterMode: false,
    isLoginMode: false,
  }),
  actions: {
    toggleRegisterMode() {
      this.isRegisterMode = !this.isRegisterMode;
    },
    setRegisterMode(mode) {
      this.isRegisterMode = mode;
    },
    toggleLoginMode() {
      this.isLoginMode = !this.isLoginMode;
    },
    setLoginMode(mode) {
      this.isLoginMode = mode;
    },
  },
});
