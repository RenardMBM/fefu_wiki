import {onMounted, ref} from "vue";
import axios from "axios";
import CommentData from "@/models/CommentModel";
import backendCommentToComment from "@/hooks/converters/backendCommentToComment";

export default function getComments(post_id: number){
    const comments = ref(Array<CommentData>());

    const fetching = async () => {
        try {
            const response = await axios.get(
                '/comment/',
                {
                    withCredentials: true,
                    params: {teacher_article: post_id}
                });
            comments.value = response.data.results.map(backendCommentToComment);
            console.log(comments.value)
        } catch (e) {
            // alert('Ошибка')
        }
    }
    onMounted(fetching)

    return { comments }
}