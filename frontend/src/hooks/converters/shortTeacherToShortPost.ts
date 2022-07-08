import BackendShortTeacher from "@/models/backendModels/BackendShortTeacher";
import ShortPost from "@/models/ShortPostModel";

export default function shortTeacherToShortPost(shortTeacher: BackendShortTeacher,
                                                isEasy=true,
                                                isBirthday=true): ShortPost {
    if (isEasy && isBirthday)
    return {
        id: shortTeacher.id,
        title: shortTeacher.full_name,
        blocks: [
            {title:"Халявность", content:shortTeacher.easy.rate.toString()} ,
            {title:"День рождения", content:shortTeacher.full_birthday}
        ]
    }
    else if (isEasy){
        return {
            id: shortTeacher.id,
            title: shortTeacher.full_name,
            blocks:[
                {title:"Халявность", content:shortTeacher.easy.rate.toString()} ,
            ]
        }
    }
    else if (isBirthday){
        return {
            id: shortTeacher.id,
            title: shortTeacher.full_name,
            blocks: [
                {title:"День рождения", content:shortTeacher.full_birthday}
            ]
        }
    }
    return {
        id: shortTeacher.id,
        title: shortTeacher.full_name,
        blocks: [
        ]
    }
}