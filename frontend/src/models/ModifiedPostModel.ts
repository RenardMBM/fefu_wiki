import PostInfoColumnData from "@/models/PostInfoColumnModel";
export default interface ModifiedPost {
    id: number,
    post_id: number,
    title : string,
    info: PostInfoColumnData
    text: string
}