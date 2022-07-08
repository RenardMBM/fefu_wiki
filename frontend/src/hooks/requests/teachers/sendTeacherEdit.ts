import axios from "axios";
import Post from "@/models/PostModel";

export default async function sendTeacherEdit(post: Post) {
    try {
        await axios.post(`/article_request/teacher/`, {
            teacher_birthday: null,
            universities: post.info.blocks.find( block => block.type==='list_InstituteItem')?.content,
            full_name: post.title,
            image: null,
            academic_degree: post.info.blocks.find( block => block.title==='Ученая степень')?.content as string,
            content: post.text,
            teacher_article: post.id
        },{withCredentials: true});
    } catch (e) {
        // alert('Ошибка')
    }
}