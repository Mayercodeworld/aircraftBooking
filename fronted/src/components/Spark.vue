<script setup>
import { onMounted, onUnmounted, ref, watch, nextTick} from 'vue';
import axios from 'axios';
import { marked } from 'marked';

const newQuestion = ref('');
const conversation = ref([]);
const props = defineProps({
    place: {
        type: String,
        required: false
    }
});

function parseMarkdown(markdown) {
    try {
        return marked(markdown);
    } catch (error) {
        console.error('Error parsing markdown:', error);
        return '';
    }
}
// 一个自定义的组合式函数，用于处理 Markdown 内容的流式显示
function useStreamMarkdown() {
    // 用于存储流式显示的当前内容
    const streamedAnswer = ref('');
    let intervalId = null;
    // 用于启动流式显示
    function streamAnswer(html) {
        streamedAnswer.value = ''; // 清空旧内容
        let index = 0;
        intervalId = setInterval(() => {
            if (index < html.length) {
                streamedAnswer.value = html.substring(0, index + 1);
                index++;
            } else {
                window.clearInterval(intervalId); // 使用全局的 clearInterval
                intervalId = null;
                // 滚动到最底部
                nextTick(() => {
                    const chatbox = document.querySelector('.chatbox');
                    if (chatbox) {
                        chatbox.scrollTop = chatbox.scrollHeight;
                    }
                });
            }
        }, 20); // 每20毫秒输出一个字符
    }
    // 用于清理定时器
    function clearStreamInterval() {
        if (intervalId) {
            window.clearInterval(intervalId); 
            intervalId = null;
        }
    }

    return { streamedAnswer, streamAnswer, clearStreamInterval };
}

const { streamedAnswer, streamAnswer, clearStreamInterval } = useStreamMarkdown();

async function sendMessage() {
    if (newQuestion.value.trim()) {
        conversation.value.push({ question: newQuestion.value, answer: '' });
        newQuestion.value = '';
        try {
            const url = 'http://localhost:8000/api/sparkai/';
            const payload = {
                query: conversation.value[conversation.value.length - 1].question,
            };
            const headers = {
                'Content-Type': 'application/json',
            };

            const response = await axios.post(url, payload, { headers });
            console.log('Response data:', response.data);

            // 验证数据格式
            if (typeof response.data.data !== 'string') {
                console.error('Invalid response format:', response.data.data);
                conversation.value[conversation.value.length - 1].answer = '无法获取回答，请稍后再试。';
                return;
            }

            // 更新对话记录中的答案
            const answerHtml = parseMarkdown(response.data.data);
            conversation.value[conversation.value.length - 1].answer = answerHtml;

            // 流式显示答案
            streamAnswer(answerHtml);
        } catch (error) {
            console.error('Error sending POST request:', error);
            // 如果请求失败，设置错误消息作为答案
            conversation.value[conversation.value.length - 1].answer = '无法获取回答，请稍后再试。';
        }
    } else {
        alert('请输入问题');
    }
}

// // 监听 place 的变化
// watch(() => props.place, async (newPlace) => {
//     if (newPlace) {
//         newQuestion.value = `你是${newPlace}当地的资深导游,现在需要你简单介绍一下当地有什么值得游玩的地方,倡议大家过来游玩，最好使用几个表情`;
//         await sendMessage();
//     }
// });

// // 在组件挂载时检查 place 是否已经有值
// onMounted(async () => {
//     if (props.place) {
//         await sendMessage();
//     }
// });

onUnmounted(() => {
    clearStreamInterval();
});
</script>

<template>
    <div class="relative w-[48%] h-[450px]">
        <div class="chatbox relative p-0 h-[440px] max-w-3xl max-h-100 lg:px-8 lg:py-14 mx-auto overflow-y-auto rounded-lg">
            <div class="text-center">
                <h2 class="text-2xl min-h-1 font-bold text-gray-800">
                    🤗Hello, 我是星火旅游小助手，您当前浏览的是美丽的{{ props.place }}哦🥰
                </h2>
            </div>

            <div v-for="(item, index) in conversation" :key="index" class="mt-16 space-y-5">
                <!-- 我 -->
                <div v-if="index != 0" class="max-w-2xl ms-auto flex justify-end gap-x-2 sm:gap-x-4">
                    <div class="grow text-end space-y-3">
                        <div class="inline-block bg-blue-600 rounded-lg p-4 shadow-sm">
                            <p class="text-normal text-white">
                                {{ item.question }}
                            </p>
                        </div>
                    </div>
                    <span class="shrink-0 inline-flex items-center justify-center size-[38px] rounded-full bg-gray-600">
                        <span class="text-sm font-medium text-white leading-none">AZ</span>
                    </span>
                </div>
                <!-- AI -->
                <div class="flex gap-x-2 sm:gap-x-4">
                    <img class="shrink-0 size-[38px]" src="" alt=""/>
                    <div class="grow max-w-[90%] space-y-3">
                        <div class="chat bg-white border border-gray-200 rounded-lg p-4 space-y-3">
                            <div v-if="index === conversation.length-1" class="text-normal text-black">
                                <div v-if="item.answer === ''">正在思考中...</div>
                                <div v-else v-html="streamedAnswer"></div>
                            </div>
                            <div v-else class="text-normal text-black" v-html="item.answer">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="relative mt-[5px] max-w-4xl flex mx-auto rounded-xl shadow-lg">
            <input type="text" v-model="newQuestion" @keydown.enter="sendMessage"  class="w-full h-[48px] pl-[10px] border box-border-2 focus:outline-blue-500 focus:outline-offset-3 focus:border-none leading-[36px] bg-transparent text-[#3b3b3b] rounded-md placeholder:text-gray justify-between" placeholder="有问题请尽管问我哦🤔">
            <div class="absolute right-0 flex items-center gap-x-1">
                <button @click="sendMessage"
                        class="inline-flex mr-[2px] mt-[2px] justify-center items-center size-[44px] rounded-lg text-white bg-blue-600 hover:bg-blue-500 focus:z-10 focus:outline-none focus:bg-blue-500">
                    <svg class="shrink-0 size-3.5" xmlns="http://www.w3.org/2000/svg" width="16"
                         height="16" fill="currentColor" viewBox="0 0 16 16">
                        <path
                            d="M15.964.686a.5.5 0 0 0-.65-.65L.767 5.855H.766l-.452.18a.5.5 0 0 0-.082.887l.41.26.001.002 4.995 3.178 3.178 4.995.002.002.26.41a.5.5 0 0 0 .886-.083l6-15Zm-1.833 1.89L6.637 10.07l-.215-.338a.5.5 0 0 0-.154-.154l-.338-.215 7.494-7.494 1.178-.471-.47 1.178Z">
                        </path>
                    </svg>
                </button>
            </div>
        </div>
    </div>
</template>

<style scoped>
.chatbox {
    border: 1px solid #000;
    width: 100%;
    height: 400px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}
.sender {
    :deep(.el-textarea__inner) {
        box-shadow: none;
        border: solid lightgray 2px;
        padding: 12px 14px;
        border-bottom: none;
        border-radius: 10px;
        font-size: 15px;
    }

    & .sender-input:hover {
        :deep(.el-textarea__inner) {
            border: solid blue 2px;
            border-bottom: none;
        }

        .toobar {
            border: solid blue 2px;
        }
    }

    .toobar {
        padding: 12px;
        border: solid lightgray 2px;
        border-radius: 10px
    }
}

.chat {
    background-color: #f0f0f0;
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 10px;
    transition: background-color 0.3s ease, border-color 0.3s ease;
}

.chat p {
    margin: 5px 0 5px 0 ;
    font-size: 16px;
    color: #333;
}

.chat::before {
    content: '';
    position: absolute;
    top: -10px;
    left: 20px;
    border-width: 10px;
    border-style: solid;
    border-color: transparent transparent #f0f0f0 transparent;
}
</style>