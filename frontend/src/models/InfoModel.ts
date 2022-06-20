export interface InfoBlock {
    title: string,
    value: string
}

export default interface Info {
    img: string,
    blocks: Array<InfoBlock>
}
