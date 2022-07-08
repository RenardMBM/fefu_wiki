import axios from "axios";
import {onMounted, ref} from "vue";
import ShortPost from "@/models/ShortPostModel";
import shortRequestTeacherToShortPost from "@/hooks/converters/shortRequestTeacherToShortPost";

export default function getEditRequestsTeacher() {
    const editRequestsTeachers = ref<Array<ShortPost>>([])

    const fetching = async () => {
        try {
            const response = await axios.get(`/article_request/teacher/`, {withCredentials: true});
            editRequestsTeachers.value = response.data.results.map(shortRequestTeacherToShortPost);
        } catch (e) {
        }
    }
    onMounted(fetching)

    return {editRequestsTeachers}
}