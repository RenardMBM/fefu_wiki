import BackendUserData from "@/models/backendModels/BackendUserData";
import User from "@/models/UserModel";

export default function userDataToUser(user: BackendUserData): User{
    return {
        permission: user.access_level,
        email: user.email
    }
}