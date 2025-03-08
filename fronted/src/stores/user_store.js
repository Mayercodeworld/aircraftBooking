// src/stores/index.js
import { defineStore } from 'pinia';
import Cookies from 'js-cookie';
import axios from "axios";
// import CryptoJS from 'crypto-js'
// import enc from 'crypto-js/enc-utf8'
// useAuthStore 用户身份验证状态
export const useAuthStore = defineStore('auth', {
  state: () => ({
    isRegisterMode: false,
    loading: false,
    token: Cookies.get('token') || '',
    user_id: Cookies.get('user_id') || '',
    user_name: Cookies.get('user_name') || '',
    user_email: Cookies.get('user_email') || '',
    isPersonCenter : false,
  }),
  actions: {
    async CheckLogin() {
      if (this.user_id) {
        try {
          const response = await axios.get(`http://127.0.0.1:8000/api/user/${this.user_id}/`);
          const db_hash_password = response.data.password;
          if (this.token === db_hash_password) {
            console.log('通过cookie，登录成功');
            return true;
            // 可以在这里更新 UI 或进行其他操作
          } else {
            console.log('通过cookie，登录失败');
            // 清除 token 和 userid
            Cookies.remove('token');
            Cookies.remove('user_id');
            this.clearToken();
            this.clearUserId();
            return false;
          }
        } catch (error) {
          console.error('请求失败:', error);
          alert('请求失败');
          // 清除 token 和 userid
          Cookies.remove('token');
          Cookies.remove('user_id');
          this.clearToken();
          this.clearUserId();
          return false;
        }
      }else {
        console.log('user_id为空');
        return false;
      }

    },

    // //对称加密与解密函数
    // // 加密单个文本
    // encrypt(token, text) {
    //   return CryptoJS.AES.encrypt(text, token).toString();
    // },
    //
    // // 解密单个文本
    // decrypt(token, encryptedText) {
    //   const bytes = CryptoJS.AES.decrypt(encryptedText, token);
    //   return bytes.toString(CryptoJS.enc.Utf8);
    // },
    // // 加密文本对象
    // encrypt_text(token, id, name, email) {
    //   // 创建一个对象，包含要加密的数据
    //   const dataToEncrypt = {
    //     id: this.encrypt(token, id),
    //     name: this.encrypt(token, name),
    //     email: this.encrypt(token, email),
    //   };
    //   return dataToEncrypt;
    // },
    //
    // // 解密文本对象
    // decrypt_text(token, encryptedData) {
    //   // 解密对象中的每个字段
    //   const decryptedData = {
    //     id: this.decrypt(token, encryptedData.id),
    //     name: this.decrypt(token, encryptedData.name),
    //     email: this.decrypt(token, encryptedData.email),
    //   };
    //   return decryptedData;
    // },



    toggleRegisterMode() {
      this.isRegisterMode = !this.isRegisterMode;
    },
    setRegisterMode(mode) {
      this.isRegisterMode = mode;
    },
    TurnPersonCenterMode() {
      this.isPersonCenter = !this.isPersonCenter;
    },
    getPersonCenterMode() {
      return this.isPersonCenter;
    },
    clearCookies() {
      Cookies.remove('token');
      Cookies.remove('user_id');
      Cookies.remove('user_name');
      Cookies.remove('user_email');
      this.clearToken();
      this.clearUserId();
    },

    // 设置token
    setToken(token) {
      this.token = token;
    },
    clearToken() {
      this.token = null;
    },
    getToken() {
      return this.token;
    },
    getUserId() {
      return this.user_id;
    },
    clearUserId() {
      this.user_id = null;
    },


    toggleLoginMode() {
      this.loading = !this.loading;
    },
    setLoginMode(mode) {
      this.loading = mode;
    },
  },
});