import axios from "axios";
import {ref, onMounted} from 'vue';
import ModifiedPost from "@/models/ModifiedPostModel";
import backendRequestInstituteToModifiedPost from "@/hooks/converters/backendRequestInstituteToModifiedPost";

export default function getModifiedInstituteData(request_id: number){
    const modifiedInstitute = ref<ModifiedPost>({
        id: 0,
        post_id: 0,
        title: "Институт Лучшего вуза",
        text: "Какая-то новая информацие о институте",
        info: {img:"", blocks:[]}
    });

    const fetching = async () => {
        try {
            const response = await axios.get(
                `/article_request/university/${request_id}/`,
                {withCredentials: true});
            modifiedInstitute.value = backendRequestInstituteToModifiedPost(response.data);
            console.log(modifiedInstitute.value)
        } catch (e) {
        }
    }
    onMounted(fetching)

    return { modifiedInstitute }
}