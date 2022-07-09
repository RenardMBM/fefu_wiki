import axios from "axios";

export default async function sendSolution(type: string, request_id: number, is_accept: boolean, reason: string) {
    try {
        const response = await axios.post(
            `/article_request/${type}/${request_id}/answer/`,
            {
                accept: is_accept,
                message: reason
            },
            {withCredentials: true}
            );
        return 200;
        // return response.request.status;
    } catch (e) {
        console.log(e);
        return 500
    }
}