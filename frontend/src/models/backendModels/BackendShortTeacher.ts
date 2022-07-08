export default interface BackendShortTeacher {
    id: number,
    full_name: string,
    easy: {
        rate: number,
        last_rate: number
    },
    full_birthday: string
}