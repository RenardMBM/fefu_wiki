import axios from "axios";
import {ref, onMounted} from 'vue';

import store from "@/store";

import TopType from "@/models/TopTypeModel";
import TopPost from "@/models/TopPostsModel"

export default function getTopPosts(id_top_type: number) {
    const top = ref<TopPost>({title: "", posts: []})

    const topType: TopType | undefined = store.getters.getTypesOfTops
        .find(
            (topType: TopType) => topType.id === id_top_type);

    if (topType === undefined) {
        return ref(undefined);
    }
    top.value.title = topType.title;

    const fetching = async () => {
        try {
            const response = await axios.get(`/top/${topType.request_url}`);
            top.value.posts = response.data;
        } catch (e) {
        }
    }
    onMounted(fetching);
    return top;
}