import axios from "axios";
import {ref, onMounted} from 'vue';
import Institute from "@/models/InstituteItemModel";
export default function getInstitutes(){
    const institutes = ref(Array<Institute>());

    const fetching = async () => {
        try {
            const response = await axios.get('/GetAllInstitutes');
            // institutes.value = response.data;
        } catch (e) {
            institutes.value = [
                {
                    id: 0,
                    title : "Институт математики и компьютерных технологий",
                },
                {
                    id: 1,
                    title : "Политехнический институт",
                }
            ]
            // alert('Ошибка')
        }
    }
    onMounted(fetching)

    return {institutes}
}