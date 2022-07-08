import axios from "axios";
import {ref, onMounted} from 'vue';
import ModifiedPost from "@/models/ModifiedPostModel";
import backendRequestInstituteToModifiedPost from "@/hooks/converters/backendRequestInstituteToModifiedPost";

export default function getModifiedInstituteData(request_id: number){
    const modifiedInstitute = ref<ModifiedPost>({
        id: request_id,
        post_id: request_id,
        title: "Институт Лучшего вуза",
        text: "Какая-то новая информацие о институте",
        info: {img:"", blocks:[]}
    });

    const fetching = async () => {
        try {
            const response = await axios.get(`modified/institute/${request_id}`, {withCredentials: true});//TODO: url
            modifiedInstitute.value = backendRequestInstituteToModifiedPost(response.data);
        } catch (e) {
        }
    }
    onMounted(fetching)

    return { modifiedInstitute }
}