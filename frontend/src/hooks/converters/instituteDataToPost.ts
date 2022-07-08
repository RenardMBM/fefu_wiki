import BackendInstitute from "@/models/backendModels/BackendInstitute";
import Post from "@/models/PostModel";
export default function instituteDataToPost(institute: BackendInstitute) : Post{
    return {
        id: institute.id,
        title: institute.title,
        text: institute.content,
        info: {
            img: "",
            blocks: []
        }
    }
}
