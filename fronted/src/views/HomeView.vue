import Login from "@/components/Login.vue";
<script setup>


</script>

<template>
    <div>
        <!-- Bg -->
        <div class="absolute top-0 -z-10 h-full w-full bg-white">
            <div class="absolute bottom-auto left-auto right-0 top-0 h-[500px] w-[500px] -translate-x-[30%] translate-y-[20%] rounded-full bg-[rgba(173,109,244,0.5)] opacity-50 blur-[80px]"></div>
        </div>

        <div class="relative mx-auto h-screen w-full max-w-7xl px-6 md:px-8 lg:px-12">
            <!-- hero -->
            <div class="pt-8">
                <div class="relative mx-auto flex max-w-3xl flex-col items-center">

                    <div class="border border-gray-600 inline-flex h-full cursor-pointer justify-center rounded-full bg-white px-3 py-1 text-xs font-medium leading-5 text-slate-600 backdrop-blur-xl dark:bg-black dark:text-slate-200">
                        已发布新的组件 ⚡️<span class="inline-flex items-center pl-2 text-black dark:text-white">查看
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="pl-0.5 text-black dark:text-white"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg></span>
                    </div>

                    <h2 class="text-center text-3xl mt-6 font-medium text-gray-900 dark:text-gray-50 sm:text-6xl">
                        Element UIX 背景模版库
                    </h2>

                    <p class="mt-6 text-center text-lg leading-6 text-gray-600 dark:text-gray-200">
                        只需复制粘贴到您的下一个项目中。所有代码均使用Tailwind CSS精心打造，便于集成
                    </p>

                    <div class="mt-10 flex gap-4">

                        <a href="#" target="_blank" rel="noopener noreferrer" class="inline-flex items-center">
                        <button class="inline-flex bg-gray-700 text-white items-center justify-center rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2">
                            注册
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"
                                 fill="none"
                                 stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                 class="pl-0.5">
                                <path d="M5 12h14"></path>
                                <path d="m12 5 7 7-7 7"></path>
                            </svg>
                        </button>
                    </a>
                        <button
                            class="inline-flex items-center justify-center rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-secondary text-secondary-foreground hover:bg-secondary/80 h-10 px-4 py-2">
                            查看演示
                        </button>
                    </div>
                </div>
            </div>

        </div>
    </div>

</template>

<style scoped>

</style>