import { reactive } from 'vue'

export const formData = reactive({
        from: '',
        to: '',
        depart: '',
        inputWay: '直达',
        passengers: '1人',
        type: '经济'
});