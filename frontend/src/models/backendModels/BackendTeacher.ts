import BackendShortInstitute from "@/models/backendModels/BackendShortInstitute";

export default interface BackendTeacher {
    id: number,
    full_name: string,
    easy: {
        rate: number,
        last_rate: number
    },
    full_birthday: string,
    universities: Array<BackendShortInstitute>,
    image: string,
    academic_degree: string,
    content: string
}