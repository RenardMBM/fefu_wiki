import BackendTeacher from "@/models/backendModels/BackendTeacher";
import Post from "@/models/PostModel";
import Rate from "@/models/RateModel";
import shortInstituteToShortPost from "@/hooks/converters/shortInstituteToShortPost";

export default function teacherDataToPost(teacher: BackendTeacher) :Post{
    return {
        id: teacher.id,
        title: teacher.full_name,
        text: teacher.content,
        info: {
            img: teacher.image,
            blocks: [
                {
                    type: "rates",
                    title: "Рейтинг",
                    content: [
                        {
                            title: "Халявность",
                            rate: teacher.easy.rate,
                            last_rate: teacher.easy.last_rate
                        }
                    ] as Array<Rate>
                },
                {
                    type: "date",
                    title: "Дата рождения",
                    content: teacher.full_birthday
                },
                {
                    type: "string",
                    title: "Ученая степень",
                    content: teacher.academic_degree
                },
                {
                    type: "list_InstituteItem",
                    title: "Институты",
                    content: teacher.universities.map(shortInstituteToShortPost)
                },
            ]
        }
    }
}