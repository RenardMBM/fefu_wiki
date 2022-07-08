import ShortPost from "@/models/ShortPostModel";
import BackendShortRequestTeacher from "@/models/backendModels/BackendShortRequestTeacher";

export default function shortRequestTeacherToShortPost(institute: BackendShortRequestTeacher): ShortPost{
    return {
        id: institute.id,
        title: institute.full_name,
        blocks: [
            {title:"Дата создания", content: new Date(institute.created_at).toLocaleDateString()}
        ]
    }
}