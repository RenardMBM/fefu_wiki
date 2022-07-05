import getTopPosts from "@/hooks/requests/tops/getTopPosts";
import {ref} from 'vue';
import TopPost from "@/models/TopPostsModel";

export default function getTopsPosts(tops_types: Array<number>) {
    const tops = ref<Array<TopPost>>([]);
    for (let top_type of tops_types){
        const top = getTopPosts(top_type);
        if (top.value !== undefined) {
            tops.value.push(top.value);
        }
    }

    return {tops};
}