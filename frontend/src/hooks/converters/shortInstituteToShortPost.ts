import ShortPost from "@/models/ShortPostModel";
import BackendShortInstitute from "@/models/backendModels/BackendShortInstitute";

export default function shortInstituteToShortPost(shortTeacher: BackendShortInstitute): ShortPost {
    return {
        id: shortTeacher.id,
        title: shortTeacher.title,
        blocks:[]
    }
}