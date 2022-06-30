import axios from "axios";

export default async function sendSolution(request_id: number, is_accept: boolean, reason: string) {
    try {
        const response = await axios.post(`/solve`, {
            request_id: request_id,
            accept: is_accept,
            reason: reason
        });
        return 200;
        // return response.request.status;
    } catch (e) {
        console.log(e);
        return 500
    }
}