<script setup>
import {ref} from 'vue';

const num = ref(0);
</script>
<template>
    <section
        class="ezy__travel7 light bg-white dark:bg-[#2E2F41] text-gray-700 dark:text-white py-10 md:p-[100px] overflow-hidden">
        <div class="container px-4 mx-auto">
            <div class="grid grid-cols-12 gap-4">
                <div class="col-span-12">
                    <div class="bg-[#404156] p-6 rounded-md text-center">
                        <h2 class="font-bold text-2xl md:text-4xl leading-tight text-white mb-0">旅客信息</h2>
                    </div>
                </div>
            </div>

            <form class="shadow-2xl mt-10 p-4 md:p-[50px] border-none rounded-md">
                <div class="border-none rounded-md">
                    <div>
                        <div class="grid grid-cols-12 gap-4">
                            <div class="col-span-12">
                                <div class="flex items-center">
                                    <div class="w-[4px] h-[27px] rounded-md bg-[#0D6EFD]"></div>
                                    <h4 class="text-2xl font-bold mb-0 ml-3">个人信息</h4>
                                </div>
                            </div>
                            <!-- name -->
                            <div class="col-span-12 md:col-span-6 lg:col-span-4">
                                <label class="text-[18px] opacity-80 mb-0 font-medium" for="lName">姓名</label>
                                <div class="mt-4 md:mt-3 mb-4">
                                    <input type="text"
                                        class="min-h-[48px] w-full leading-[36px] bg-transparent border boder-[#BBBFC8] dark:border-[#888993] pl-[24px] focus:outline focus:outline-blue-500 focus:border-none rounded-md opacity-75"
                                        id="lName" placeholder="姓名" />
                                </div>
                            </div>
                            <div class="col-span-12 md:col-span-6 lg:col-span-2">
                                <label class="text-[18px] opacity-80 mb-0 font-medium" for="bDate">出生日期</label>
                                <div class="mt-4 md:mt-3 mb-4">
                                    <input type="text"
                                        class="min-h-[48px] w-full leading-[36px] bg-transparent border boder-[#BBBFC8] dark:border-[#888993] pl-[24px] focus:outline focus:outline-blue-500 focus:border-none rounded-md opacity-75"
                                        id="bDate" placeholder="年/月/日" />
                                </div>
                            </div>
                            <div class="col-span-12 md:col-span-6 lg:col-span-2">
                                <label class="font-medium mb-0">性别</label>
                                <select
                                    class="min-h-[48px] leading-[36px] border border-[#BBBFC8] dark:border-[#888993] dark:bg-[#2E2F41] text-gray-400 px-4 w-full focus:outline focus:outline-blue-500 focus:border-none mt-3 mb-4 rounded-md"
                                    aria-label="Default select example">
                                    <option value="0" selected>男</option>
                                    <option value="1">女</option>
                                </select>
                            </div>
                        </div>

                        <div class="grid grid-cols-12 gap-4">
                            <!-- country -->
                            <div class="col-span-12 md:col-span-6 lg:col-span-4">
                                <label class="font-medium mb-0">国籍</label>
                                <select
                                    class="min-h-[48px] leading-[36px] border border-[#BBBFC8] dark:border-[#888993] dark:bg-[#2E2F41] text-gray-400 px-4 w-full focus:outline focus:outline-blue-500 focus:border-none mt-3 mb-4 rounded-md"
                                    aria-label="Default select example">
                                    <option value="0" selected>中国</option>
                                    <option value="1">美国</option>
                                    <option value="2">法国</option>
                                    <option value="3">英国</option>

                                </select>
                            </div>
                            <!-- passport no -->
                            <div class="col-span-12 md:col-span-6 lg:col-span-4">
                                <label class="text-[18px] opacity-80 mb-0 font-medium" for="passport">身份证/护照</label>
                                <div class="mt-4 md:mt-3 mb-4">
                                    <input type="password"
                                        class="min-h-[48px] w-full leading-[36px] bg-transparent border boder-[#BBBFC8] dark:border-[#888993] pl-[24px] focus:outline focus:outline-blue-500 focus:border-none rounded-md opacity-75"
                                        id="passport"/>
                                </div>
                            </div>
                            
                        </div>
                    </div>
                    <div class="grid grid-cols-12 gap-4 mt-6">
                        <div class="col-span-12">
                            <div class="flex items-center mb-4">
                                <div class="w-[4px] h-[27px] rounded-md bg-[#0D6EFD]"></div>
                                <h4 class="text-2xl font-bold mb-0 ml-3">行李托运</h4>
                            </div>
                            <div class="border border-[#888993] px-4 py-2 md:p-6">
                                <div class="grid grid-cols-12 gap-4 items-center">
                                    <div class="col-span-6 sm:col-span-4">
                                        <div>
                                            <h6 class="font-medium mb-0">小行李</h6>
                                        </div>
                                    </div>
                                    <div class="col-span-6 sm:col-span-4 md:col-span-5">
                                        <p class="mb-0 opacity-50">42x31x20cm</p>
                                    </div>
                                    <div class="col-span-6 sm:col-span-2">
                                        <div>
                                            <h6 class="mb-0 font-medium text-xl md:text-2xl">免费</h6>
                                        </div>
                                    </div>
                                    <div class="col-span-6 sm:col-span-2 md:col-span-1">
                                        <div
                                            class="w-10 h-10 rounded-full flex justify-center items-center text-[22px] cursor-pointer opacity-30 bg-[#4c4d5a] hover:opacity-75">
                                            <i class="fas fa-times"></i>
                                        </div>
                                    </div>
                                </div>

                                <div class="grid grid-cols-12 gap-4 items-center mt-8">
                                    <div class="col-span-6 sm:col-span-4">
                                        <div>
                                            <h6 class="font-medium mb-0">大行李</h6>
                                        </div>
                                    </div>
                                    <div class="col-span-6 sm:col-span-4 md:col-span-5">
                                        <p class="mb-0 opacity-50">23kg</p>
                                    </div>
                                    <div class="col-span-6 sm:col-span-2">
                                        <div>
                                            <h6 class="mb-0 font-medium text-xl md:text-2xl">￥80</h6>
                                        </div>
                                    </div>
                                    <div class="col-span-6 sm:col-span-2 md:col-span-1">
                                        <div
                                            class="w-10 h-10 rounded-full flex justify-center items-center text-[22px] cursor-pointer opacity-30 bg-[#4c4d5a] hover:opacity-75">
                                            <i class="fas fa-times"></i>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="grid grid-cols-12 gap-4 items-center mt-10">
                                <div class="col-span-6 sm:col-span-8">
                                    <div
                                        class="h-[48px] bg-[#F2F6FD] dark:bg-[#3E435A] flex flex-col justify-center px-[16px] w-full rounded-md">
                                        <div class="grid grid-cols-12 gap-4 items-center">
                                            <div class="col-span-6">
                                                <h6
                                                    class="mb-4 sm:mb-0 leading-none font-medium text-black dark:text-white">
                                                    确认行李</h6>
                                            </div>
                                            <div class="col-span-6">
                                                <p class="mb-0 opacity-50">23kg</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-span-2 sm:col-span-1">
                                    <div
                                        class="min-h-[48px] bg-[#F2F6FD] dark:bg-[#3E435A] flex flex-col justify-center px-[16px] w-full rounded-md">
                                        <input v-model="num" num type="number" placeholder="0" class=" bg-[#F2F6FD] dark:bg-[#3E435A]" />
                                    </div>
                                </div>
                                <div class="col-span-2 sm:col-span-3">
                                    <button
                                        class="text-white font-bold text-[20px] min-w-[90px] min-h-[48px] bg-blue-600 hover:bg-opacity-90 rounded">￥{{ num * 80 }}</button>
                                </div>
                            </div>

                        </div>
                    </div>

                    <div>
                        <div class="grid grid-cols-12 gap-4 mt-5">
                            <div class="col-span-12">
                                <div class="flex items-center mb-4">
                                    <div class="w-[4px] h-[27px] rounded-md bg-[#0D6EFD]"></div>
                                    <h4 class="text-2xl font-bold mb-0 ml-3">旅行保险</h4>
                                </div>
                            </div>
                            <div class="col-span-12 md:col-span-4">
                                <div
                                    class="border border-transparent hover:border-blue-600 bg-transparent p-[24px] md:p-0 xl:p-[48px] rounded-md">
                                    <div class="p-[24px] md:p-4 xl:p-[48px]">
                                        <div class="flex items-center justify-center w-full">
                                            <i class="fas fa-heart-broken text-3xl"></i>
                                        </div>
                                        <h4 class="text-2xl font-medium text-center my-6">基础</h4>
                                        <ul class="flex flex-col">
                                            <li class="flex items-center">
                                                <i class="fas fa-times opacity-50 mr-6"></i>
                                                <p class="mb-0 opacity-50">Medical Expense</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Trip Cancellatuon</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Lost Baggage</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Air Travel Insurance</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Libability</p>
                                            </li>
                                        </ul>
                                        <div class="text-center mt-8">
                                            <button
                                                class="text-white font-bold text-[20px] min-w-[90px] min-h-[48px] bg-blue-600 hover:bg-opacity-90 rounded">￥0</button>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="col-span-12 md:col-span-4">
                                <div
                                    class="border border-blue-600 bg-transparent p-[24px] md:p-0 xl:p-[48px] rounded-md">
                                    <div class="p-[24px] md:p-4 xl:p-[48px]">
                                        <div class="flex items-center justify-center w-full">
                                            <i class="fas fa-star text-3xl"></i>
                                        </div>
                                        <h4 class="text-2xl font-medium text-center my-6">高级</h4>
                                        <ul class="flex flex-col">
                                            <li class="flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Medical Expense</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-times opacity-50 mr-6"></i>
                                                <p class="mb-0 opacity-50">Trip Cancellatuon</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Lost Baggage</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Air Travel Insurance</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Libability</p>
                                            </li>
                                        </ul>
                                        <div class="text-center mt-8">
                                            <button
                                                class="text-white font-bold text-[20px] min-w-[90px] min-h-[48px] bg-blue-600 hover:bg-opacity-90 rounded">￥50</button>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="col-span-12 md:col-span-4">
                                <div
                                    class="border border-transparent hover:border-blue-600 bg-transparent p-[24px] md:p-0 xl:p-[48px] rounded-md">
                                    <div class="p-[24px] md:p-4 xl:p-[48px]">
                                        <div class="flex items-center justify-center w-full">
                                            <i class="fas fa-briefcase text-3xl"></i>
                                        </div>
                                        <h4 class="text-2xl font-medium text-center my-6">专业</h4>
                                        <ul class="flex flex-col">
                                            <li class="flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Medical Expense</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Trip Cancellatuon</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Lost Baggage</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-check text-blue-600 mr-6"></i>
                                                <p class="mb-0 opacity-50">Air Travel Insurance</p>
                                            </li>
                                            <li class="pt-2 flex items-center">
                                                <i class="fas fa-times opacity-50 mr-6"></i>
                                                <p class="mb-0 opacity-50">Libability</p>
                                            </li>
                                        </ul>
                                        <div class="text-center mt-8">
                                            <button
                                                class="text-white font-bold text-[20px] min-w-[90px] min-h-[48px] bg-blue-600 hover:bg-opacity-90 rounded">￥100</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </form>
            <div class="grid grid-cols-12 gap-2 md:gap-4 mt-10">
                <div class="col-span-12">
                    <div class="flex items-center">

                        <button type="submit"
                            class="text-[18px] text-white font-medium py-[12px] px-[30px] bg-blue-600 hover:bg-opacity-90 rounded text-center mt-5 md:mt-0">
                            提交
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section
  class="ezy__eporder1 light py-14 md:py-24 bg-white dark:bg-[#0b1727] text-zinc-900 dark:text-white relative overflow-hidden z-10"
>
  <div class="container px-4 mx-auto">
    <div class="flex justify-center max-w-md mx-auto">
      <div class="bg-gray-100 dark:bg-slate-800 rounded-md overflow-hidden">
        <div class="bg-slate-200 dark:bg-slate-700 relative p-6">
          <div
            class="absolute top-4 right-4 w-8 h-8 rounded-full cursor-pointer border border-black dark:border-white flex justify-center items-center"
          >
            <i class="fas fa-times"></i>
          </div>
          <h5 class="text-xl font-bold">Course Cloud Certificate</h5>
          <h6 class="font-medium opacity-60">TOTAL BILLED: $54</h6>
        </div>
        <div class="text-center py-12 px-4">
          <div
            class="relative left-1/2 -translate-x-1/2 w-10 h-10 text-[22px] rounded-full border border-blue-600 text-blue-600 flex justify-center items-center"
          >
            <i class="fas fa-check"></i>
          </div>
          <h1 class="text-2xl font-bold leading-none my-4">
            Your Certificate Order is Successful
          </h1>
          <p class="text-base opacity-80 px-12">
            In purus donec ac in nulla lobortis. Lectus massa erat odio
            turpis nulla sed.
          </p>
          <button
            class="bg-blue-600 text-white hover:bg-opacity-90 rounded-md px-6 py-3 mt-6 mb-3"
          >
            Back to Courses
          </button>
        </div>
        <div class="bg-slate-200 dark:bg-slate-700 text-center p-6">
          <div class="flex items-center justify-center">
            <i class="fas fa-lock mr-2"></i>
            <b>Secured with SSL</b>
          </div>
          <b>Have a question? 0123 4567 891</b>
        </div>
      </div>
    </div>
  </div>
</section>

</template>

