import axios from "axios";
import Post from "@/models/PostModel";


export default async function sendEditData(path:string, post: Post) {
    try {
        const response = await axios.post(`${path}/edit`, post);
        return 200;
        // return response.request.status;
    } catch (e) {
        console.log(e);
        // return e.request.staus;
        return 500
    }

}