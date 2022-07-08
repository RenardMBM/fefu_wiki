export interface PostInfoColumnRaw {
    type: string,
    title: string,
    content: Object
}

export default interface PostInfoColumnData {
    img: string,
    blocks: Array<PostInfoColumnRaw>
}
