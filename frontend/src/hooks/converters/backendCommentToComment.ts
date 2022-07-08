import BackendComment from "@/models/backendModels/BackendComment";
import CommentData from "@/models/CommentModel";

export default function backendCommentToComment(comment: BackendComment): CommentData{
    return {
        userId: comment.author,
        date: new Date(comment.created_at),
        text: comment.content,
        likes: comment.like.rate,
        dislikes: comment.dislike.rate,
        voted: comment.like.last_rate - comment.dislike.last_rate
    }
}