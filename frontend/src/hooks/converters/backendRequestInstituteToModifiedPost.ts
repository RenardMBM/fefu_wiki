import BackendRequestInstitute from "@/models/backendModels/BackendRequestInstitute";
import ModifiedPost from "@/models/ModifiedPostModel";

export default function backendRequestInstituteToModifiedPost(requestInstitute: BackendRequestInstitute): ModifiedPost{
    return {
        id: requestInstitute.id,
        post_id: requestInstitute.university_article,
        title: requestInstitute.title,
        text: requestInstitute.content,
        info: {img:"", blocks:[]}
    }
}