import BackendTeacher from "@/models/backendModels/BackendTeacher";
import Post from "@/models/PostModel";

export default function teacherDataToPost(teacher: BackendTeacher) :Post{
    return {
        id: teacher.id,
        title: teacher.full_name,
        text: "",
        info: {
            img: "",
            blocks: [
            ]
        }
    }
} //TODO: Incorrect converter