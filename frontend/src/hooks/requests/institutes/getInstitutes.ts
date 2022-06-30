import axios from "axios";
import {ref, onMounted} from 'vue';
import ShortPost from "@/models/ShortPostModel";
export default function getInstitutes(){
    const institutes = ref(Array<ShortPost>());

    const fetching = async () => {
        try {
            const response = await axios.get('/GetAllInstitutes');
            institutes.value = response.data;
        } catch (e) {
            institutes.value = [
                {
                    id: 0,
                    title : "Институт математики и компьютерных технологий",
                    blocks: []
                },
                {
                    id: 1,
                    title : "Политехнический институт",
                    blocks: []
                }
            ]
            // alert('Ошибка')
        }
    }
    onMounted(fetching)

    return {institutes}
}