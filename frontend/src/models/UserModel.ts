export default interface User {
    csrftoken: string,
    sessionid: string,
    permission: number,
    email: string
}