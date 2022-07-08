import axios from "axios";
import {ref, onMounted} from 'vue';
import ShortPost from "@/models/ShortPostModel";
import shortTeacherToShortPost from "@/hooks/converters/shortTeacherToShortPost";
import BackendShortTeacher from "@/models/backendModels/BackendShortTeacher";

export default function getTeachers(){
    const teachers = ref(Array<ShortPost>());

    const fetching = async () => {
        try {
            const response = await axios.get('/article/teacher/', {withCredentials: true});
            const converter = (teacher : BackendShortTeacher) => shortTeacherToShortPost(teacher, false, true)
            teachers.value = response.data.results.map(converter);
            console.log(teachers.value)
        } catch (e) {
            // alert('Ошибка')
        }
    }
    onMounted(fetching)

    return { teachers }
}