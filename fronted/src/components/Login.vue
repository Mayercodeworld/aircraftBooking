<script setup lang="ts">import { ref } from 'vue';

const isRegisterMode = ref(false);

const onMounted = () => {
  isRegisterMode.value = false;
};

const toggleMode = () => {
  isRegisterMode.value = !isRegisterMode.value;
};
const handleSubmit = (event: Event) => {
  event.preventDefault();
  if (isRegisterMode.value) {
    // 处理注册逻辑
    console.log('Registering user');
  } else {
    // 处理登录逻辑
    console.log('Logging in user');
  }
};
</script>

<template>
    <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
      <div class="sm:mx-auto sm:w-full sm:max-w-sm">
        <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/plus-assets/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company" />
        <h2 class="mt-10 text-center text-2xl/9 font-bold tracking-tight text-gray-900">{{ isRegisterMode ? 'Register for an account' : 'Sign in to your account' }}</h2>
      </div>

      <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <form class="space-y-6" action="#" method="POST">

          <div v-if="isRegisterMode">
          <label for="name" class="block text-sm font-medium text-gray-900">Name</label>
          <div class="mt-2">
            <input type="text" name="name" id="name" autocomplete="name" required="" class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm" />
          </div>
        </div>

          <div>
            <label for="email" class="block text-sm/6 font-medium text-gray-900">Email address</label>
            <div class="mt-2">
              <input type="email" name="email" id="email" autocomplete="email" required="" class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6" />
            </div>
          </div>

          <div>
            <div class="flex items-center justify-between">
              <label for="password" class="block text-sm/6 font-medium text-gray-900">Password</label>
              <div class="text-sm">
                <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">Forgot password?</a>
              </div>
            </div>
            <div class="mt-2">
              <input type="password" name="password" id="password" autocomplete="current-password" required="" class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6" />
            </div>
          </div>

          <div>
            <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">{{ isRegisterMode ? 'Register' : 'Sign in' }}</button>
          </div>
        </form>

        <p class="mt-10 text-center text-sm/6 text-gray-500">
          {{ isRegisterMode ? 'have an account! ' : 'Not a account?' }}
        <button @click="toggleMode" class="font-semibold text-indigo-600 hover:text-indigo-500">
          {{ isRegisterMode ? 'Sign In' : 'Sign Up' }}
        </button>
        </p>
      </div>
    </div>
  </template>

  <style scoped>

  </style>
