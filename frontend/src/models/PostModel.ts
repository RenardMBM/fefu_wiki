import Info from "@/models/InfoModel";
export default interface Post {
    id: number,
    title : string,
    info: Info
    text: string
}