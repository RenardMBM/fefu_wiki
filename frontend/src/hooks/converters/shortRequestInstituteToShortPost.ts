import BackendShortRequestInstitute from "@/models/backendModels/BackendShortRequestInstituteModel";
import ShortPost from "@/models/ShortPostModel";

export default function shortRequestInstituteToShortPost(institute: BackendShortRequestInstitute): ShortPost{
    return {
        id: institute.id,
        title: institute.title,
        blocks: [
            {title:"Дата создания", content: new Date(institute.created_at).toLocaleDateString()}
        ]
    }
}