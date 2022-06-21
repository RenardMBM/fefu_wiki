export interface PostInfoColumnRaw {
    title: string,
    text: string
}

export default interface PostInfoColumnData {
    img: string,
    blocks: Array<PostInfoColumnRaw>
}
