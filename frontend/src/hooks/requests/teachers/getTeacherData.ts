import axios from "axios";
import {ref, onMounted} from 'vue';
import Post from "@/models/PostModel";
import teacherDataToPost from "@/hooks/converters/teacherDataToPost";

export default function getTeacherData(teacher_id: number){
    const teacher = ref<Post>({
        id: teacher_id,
        title: "Фамилия Имя Отчество",
        info: {
            img: "/img/logo.9e4b96be.png",
            blocks:[
                {
                    type: "date",
                    title: "дата рождения",
                    content: "2002-12-01"
                },
                {
                    type: "string",
                    title: "Ученая степень",
                    content: "Доктор наук …"
                },
                {
                    type:"rates",
                    title: "Рейтинг",
                    content: [
                        {
                            title: "Халявность",
                            rate: 4.5,
                            last_rate: 0
                        },
                        {
                            title: "Гениальность",
                            rate: 1,
                            last_rate: 0
                        }
                    ]
                },
                {
                    type: "list_InstituteItem",
                    title: "Школы",
                    content: [
                        {
                            id: 0,
                            title: "Институт математики и комп",
                            blocks:[]
                        },
                        {
                            id: 1,
                            title: "Политех",
                            blocks:[]
                        }
                    ]
                }
            ]
        },
        text: "Какая-то информацие о преподавателе",

    });
    const fetching = async () => {
        try {
            const response = await axios.get(
                `/article/teacher/${teacher_id}/`,
                {withCredentials: true}
            );
            teacher.value = teacherDataToPost(response.data);
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

    return { teacher }
}