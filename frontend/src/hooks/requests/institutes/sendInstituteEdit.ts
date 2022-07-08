import axios from "axios";
import Post from "@/models/PostModel";

export default async function sendInstituteEdit(post: Post) {
    try {
        await axios.post(`/article_request/university/`, {
            title: post.title,
            content: post.text,
            university_article: post.id
        },{withCredentials: true});
    } catch (e) {
        // alert('Ошибка')
    }
}