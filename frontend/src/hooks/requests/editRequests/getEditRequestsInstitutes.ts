import axios from "axios";
import {onMounted, ref} from "vue";
import ShortPost from "@/models/ShortPostModel";
import shortRequestInstituteToShortPost from "@/hooks/converters/shortRequestInstituteToShortPost";

export default function getEditRequestsInstitutes(){
        const editRequestsInstitutes = ref<Array<ShortPost>>([])

        const fetching = async () => {
            try {
                const response = await axios.get(`/article_request/university/`, {withCredentials: true});
                editRequestsInstitutes.value = response.data.results.map(shortRequestInstituteToShortPost);
            } catch (e) {
            }
        }
        onMounted(fetching)

        return { editRequestsInstitutes }
}