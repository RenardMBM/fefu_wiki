import axios from "axios";
import Post from "@/models/PostModel";


export default async function sendEditData(path:string, post: Post) {
    try {
        console.log("Send")
        console.log(post)
        const response = await axios.post(`${path}`, post);
        return 200;
        // return response.request.status;
    } catch (e) {
        console.log(e);
        // return e.request.staus;
        return 500
    }

}