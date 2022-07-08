import axios from "axios";

export default async function sendComments(post_id: number, text: string) {
    try {
        await axios.post(`/comment/`, {
            content: text,
            teacher_article: post_id
        },{withCredentials: true});
    } catch (e) {
        // alert('Ошибка')
    }
}