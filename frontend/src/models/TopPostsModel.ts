import ShortPost from "@/models/ShortPostModel";

export default interface TopPosts{
    title: string,
    posts: Array<ShortPost>
}