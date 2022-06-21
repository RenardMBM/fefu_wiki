import PostInfoColumnData from "@/models/PostInfoColumnModel";
export default interface Post {
    id: number,
    title : string,
    info: PostInfoColumnData
    text: string
}