import axios from "axios";


export default async function sendEditData(path:string, text: string) {
    try {
        const response = await axios.post(`${path}/edit`, {
            text: text
        });
    } catch (e) {

    }
}