import {onMounted, ref} from "vue";
import ShortPost from "@/models/ShortPostModel";
import axios from "axios";

export default function searchPost(searchQuery: String){
    const posts = ref<Array<ShortPost>>([]);

    const fetching = async () => {
        try {
            const response = await axios.post(
                '/search/',
                { searchQuery: searchQuery},
                {withCredentials: true});
            posts.value = response.data;
        } catch (e) {
            posts.value = [
                {
                    id: 0,
                    title : "Институт математики и компьютерных технологий",
                    blocks:[
                        {
                            title: "Общая оценка",
                            content: "5.0"
                        }
                    ]
                },
                {
                    id: 1,
                    title : "Политехнический институт",
                    blocks:[
                        {
                            title: "Общая оценка",
                            content: "4.5"
                        }
                    ]
                }
            ]
        }
    }
    onMounted(fetching);
    return {posts}
}