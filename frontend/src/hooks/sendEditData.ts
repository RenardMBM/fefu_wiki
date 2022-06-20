import axios from "axios";


export default async function sendEditData(path:string, text: string) {
    try {
        const response = await axios.post(`${path}/edit`, {
            data: {
                text: text
            }
        });
        return 200;
        // return response.request.status;
    } catch (e) {
        console.log(e);
        // return e.request.staus;
        return 500
    }

}