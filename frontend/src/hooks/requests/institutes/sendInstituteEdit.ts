import axios from "axios";
import Post from "@/models/PostModel";

export default async function sendInstituteEdit(post: Post) {
    try {
        await axios.post(`/article/university/${post.id}/`, {
            title: post.title,
            content: post.text
        },{withCredentials: true});
    } catch (e) {
        // alert('Ошибка')
    }
}