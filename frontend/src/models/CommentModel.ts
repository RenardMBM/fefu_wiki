export default interface CommentData {
    userId: number | null,
    date: Date,
    text: string,
    likes: number,
    dislikes: number,
    voted: number,
}