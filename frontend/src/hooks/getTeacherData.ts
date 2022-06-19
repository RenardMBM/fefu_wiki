import axios from "axios";
import {ref, onMounted} from 'vue';
import Post from "@/models/PostModel";
export default function getTeacherData(teacher_id: number){
    const teacher = ref<Post>({
        id: teacher_id,
        title: "Фамилия Имя Отчество",
        info: {
            img: "/img/logo.9e4b96be.png",
            blocks:[
                {
                    title: "дата рождения",
                    value: "12-01-2002"
                },
                {
                    title: "Ученая степень",
                    value: "Доктор наук …"
                }
            ]
        },
        text: "Какая-то информацие о преподавателе",

    });

    const fetching = async () => {
        try {
            const response = await axios.get(`/teacher/${teacher_id}`);
            teacher.value = response.data;
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

    return {teacher}
}