export default interface BackendComment{
    id: number,
    like: {
        rate: number,
        last_rate: number
    },
    dislike: {
        rate: number,
        last_rate: number
    },
    content: string,
    created_at : string,
    author: number | null,
    teacher_article: number
}