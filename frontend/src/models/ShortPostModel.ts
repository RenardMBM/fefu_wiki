export interface SubInfo{
    title: string,
    content: string
}
export default interface ShortPost{
    id: number,
    title: string,
    blocks: Array<SubInfo>,
}