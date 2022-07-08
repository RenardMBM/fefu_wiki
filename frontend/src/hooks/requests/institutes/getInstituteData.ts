import axios from "axios";
import {ref, onMounted} from 'vue';
import Post from "@/models/PostModel";
import instituteDataToPost from "@/hooks/converters/instituteDataToPost";
export default function getInstituteData(institute_id: number){
    const institute = ref<Post>({
        id: institute_id,
        title: "Институт Лучшего вуза",
        info: {
            img: "/img/logo.9e4b96be.png",
            blocks: []
        },
        text: "Какая-то информацие о институте",
    });

    const fetching = async () => {
        try {
            const response = await axios.get(`/article/university/${institute_id}/`, {withCredentials: true});
            institute.value = instituteDataToPost(response.data);
        } catch (e) {
            // teacher.value = {
            //     id: teacher_id,
            //     title: "Фамилия Имя Отчество",
            //     info: {
            //         img: "url",
            //         blocks:[
            //             {
            //                 title: "дата рождения",
            //                 value: "12-01-2002"
            //             }
            //         ]
            //     },
            //     text: "Какая-то информацие о преподавателе",
            //
            // }
            // alert('Ошибка')
        }
    }
    onMounted(fetching)

    return {institute}
}