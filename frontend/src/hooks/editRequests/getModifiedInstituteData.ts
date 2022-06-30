import axios from "axios";
import {ref, onMounted} from 'vue';
import ModifiedPost from "@/models/ModifiedPostModel";

export default function getModifiedInstituteData(request_id: number){
    const modifiedInstitute = ref<ModifiedPost>({
        id: request_id,
        post_id: request_id,
        title: "Институт Лучшего вуза",
        info: {
            img: "/img/logo.9e4b96be.png",
            blocks: [
                {
                    title: "дата создания",
                    text: "12-01-2002"
                },
                {
                    title: "Ученая степень",
                    text: "Доктор наук …"
                }
            ]
        },
        text: "Какая-то новая информацие о институте",
    });

    const fetching = async () => {
        try {
            const response = await axios.get(`modified/institute/${request_id}`);
            modifiedInstitute.value = response.data;
        } catch (e) {
        }
    }
    onMounted(fetching)

    return { modifiedInstitute }
}